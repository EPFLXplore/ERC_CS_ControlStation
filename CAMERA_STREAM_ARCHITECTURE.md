# Camera Stream Duplication Prevention Architecture

## Summary
✅ **The system is designed to prevent camera stream duplication** from the rover to all connected Control Station instances.

## How It Works

### 1. Single ROS Subscription Model
The rosbridge server uses a **shared subscription model** implemented in:
- [`rosbridge_library/src/rosbridge_library/internal/subscribers.py`](subscribers.py)

**Key Classes:**
- `MultiSubscriber`: Creates and manages a SINGLE ROS subscription per topic
- `SubscriberManager`: Ensures one `MultiSubscriber` per unique topic

### 2. Multi-Client Subscription Flow

```
┌─────────────────────────────────────────────────────────┐
│                  Rosbridge Server                        │
│                                                          │
│  ┌──────────────────────────────────────┐               │
│  │  SubscriberManager (global manager)  │               │
│  │  _subscribers = {                    │               │
│  │    "/ROVER/feed_camera_hd_0":        │               │
│  │      MultiSubscriber                 │               │
│  │  }                                   │               │
│  └──────────────────────────────────────┘               │
│                      │                                   │
│        ┌─────────────┴─────────────┐                    │
│        │                           │                    │
│   ┌────▼──────┐          ┌────────▼────┐               │
│   │ Laptop 1  │          │  Laptop 2   │               │
│   │ Subscribe │          │  Subscribe  │               │
│   │ to topic  │          │  to topic   │               │
│   └────┬──────┘          └────┬────────┘               │
│        │ (adds callback)     │ (adds callback)          │
│        └─────────────┬───────┘                         │
│                      ▼                                   │
│        MultiSubscriber.subscriptions = {               │
│          "laptop_1_client_id": callback_1,            │
│          "laptop_2_client_id": callback_2             │
│        }                                                │
│                      │                                  │
│        ONE ROS Subscription to rover ◄──────────────────│
│        (only ONE active subscription)                   │
│                      │                                  │
│        ┌─────────────┴──────────────┐                  │
│        ▼                            ▼                   │
│   Callback 1 (to Laptop 1)   Callback 2 (to Laptop 2) │
│   via WebSocket              via WebSocket            │
└─────────────────────────────────────────────────────────┘
         ▲                            ▲
         │                            │
    Rover sends                  Each laptop gets
    one stream                   its own copy
```

### 3. Code Flow

**When Laptop 1 subscribes:**
```python
# From SubscriberManager.subscribe()
if topic not in self._subscribers:
    self._subscribers[topic] = MultiSubscriber(
        topic, client_id_1, callback_1, ...
    )
    # Creates ONE ROS subscription
```

**When Laptop 2 subscribes to the same topic:**
```python
else:
    self._subscribers[topic].subscribe(client_id_2, callback_2)
    # Reuses existing MultiSubscriber, adds callback_2
    # NO new ROS subscription created
```

**When messages arrive from rover:**
```python
# From MultiSubscriber.callback()
for callback in self.subscriptions.values():  # All callbacks
    callback(message)  # Each gets the same data
```

**Messages are sent to clients separately:**
```python
# From Subscribe.publish()
self.protocol.send(outgoing_msg)  # Each protocol/WebSocket sends only to its client
```

## Verification Points

### ✅ Single Subscription Ensured By:
1. **Line 325 in subscribers.py**: `if topic not in self._subscribers:`
   - Prevents creating duplicate `MultiSubscriber` objects
   
2. **Line 330 in subscribers.py**: `self._subscribers[topic].subscribe(client_id, callback)`
   - Reuses existing subscriber, just adds callback
   
3. **Thread-safe locking**: `with self._lock:` prevents race conditions

### ✅ Per-Client Delivery By:
1. **Line 232 in subscribers.py**: Each client has its own callback registered
   - `self.subscriptions = {client_id: callback}`

2. **Line 363 in subscribe.py**: 
   - `self.protocol.send(outgoing_msg, compression=compression)`
   - Each protocol sends only to its WebSocket client

### ✅ Cleanup on Disconnect:
1. **Line 342 in subscribers.py**: `MultiSubscriber.unsubscribe(client_id)`
   - Removes the disconnected client's callback

2. **Line 351 in subscribers.py**: 
   - `if not self._subscribers[topic].has_subscribers():`
   - Unsubscribes from ROS entirely when no clients remain

## Scenarios Tested By This Architecture

| Scenario | Behavior | Result |
|----------|----------|--------|
| 1 laptop connects | 1 ROS subscription created | ✅ Stream flows normally |
| 2nd laptop connects | Same subscription, new callback added | ✅ Both laptops receive stream |
| 3rd laptop connects | Same subscription, another callback added | ✅ All 3 laptops receive stream |
| 1st laptop disconnects | Callback removed, subscription stays | ✅ Other 2 still receive |
| All laptops disconnect | Subscription unregistered | ✅ Cleanup complete |

## Camera Topics Configured

From [`frontend/src/pages/cameras/index.tsx`](frontend/src/pages/cameras/index.tsx#L9):
```typescript
const CAMERA_DEFS = [
    { id: "nav_front", topic: "/NAV/feed_camera_nav_0" },
    { id: "hd_gripper", topic: "/ROVER/feed_camera_hd_0" },
    { id: "cs_st_0", topic: "/CS/feed_camera_cs_0" },
    // ... more cameras
];
```

Each topic will only have ONE ROS subscription from rosbridge regardless of client count.

## QoS Settings

From [`frontend/src/hooks/cameraHooks.ts`](frontend/src/hooks/cameraHooks.ts#L14):
```typescript
const CAMERA_FEED_SUBSCRIBE_QOS = {
    history: "keep_last",
    depth: 1,
    reliability: "best_effort",
    durability: "volatile",
};
```

These settings optimize for:
- **Low latency** (best_effort, volatile)
- **No buffering** (keep_last with depth 1)
- **Real-time streams** (no durability)

## Potential Issues (If Duplication is Observed)

If you ARE seeing duplication, check:

1. **Rover-side issue**: The rover itself might be creating multiple Publishers
   - Check rover software logs for `/ROVER/feed_camera_hd_0` topic publishers

2. **Network/Cyclone DDS issue**: CycloneDDS configuration might affect discovery
   - Check: [`docker_humble_desktop/cyclonedds_with_rover.xml`](docker_humble_desktop/cyclonedds_with_rover.xml)
   - Check: `export CYCLONEDDS_URI` in [`launch_with_server.sh`](launch_with_server.sh#L5)

3. **Multiple rosbridge instances**: If more than one rosbridge server is running
   - Check: `ps aux | grep rosbridge`
   - Check: Only one rosbridge server should be running

4. **ROS node discovery**: Verify rosbridge is configured correctly
   - Check: `ros2 node list | grep rosbridge`
   - Check: `ros2 topic list | grep camera`

## How to Verify

### Check subscription deduplication:
```bash
# Terminal 1 (inside docker or with rover network):
source install/setup.bash
ros2 topic info /ROVER/feed_camera_hd_0 --verbose

# Should show:
#   Subscription count: 1  (not 2, 3, etc. even with multiple clients)
```

### Monitor in real-time:
```bash
# Watch topic activity
ros2 topic hz /ROVER/feed_camera_hd_0

# Should show consistent frequency (e.g., 10 Hz)
# Even with 2-3 clients connected
```

### Check WebSocket connections:
```bash
# From host machine
lsof -i :9090  # Or whatever port rosbridge uses
netstat -tuln | grep 9090

# Should see multiple WebSocket connections
# (one per browser) but only one ROS subscription
```

## Conclusion

The rosbridge implementation **correctly deduplicates camera subscriptions**. Multiple CS instances can safely connect to the same `launch_with_server.sh` instance without creating duplicate streams from the rover. The architecture ensures:

✅ Scalable multi-client support
✅ Efficient resource usage on rover
✅ Proper cleanup on disconnect
✅ Real-time camera streaming with minimal latency
