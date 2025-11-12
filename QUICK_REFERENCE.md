# Quick Reference: Direct Subsystem Communication

## Topic Naming Pattern
```
/[SUBSYSTEM]/[Command]
```

## Subsystem Prefixes
- **NAV** - Navigation
- **HD** - Handling Device  
- **DRILL** - Drilling System
- **EL** - Electronics
- **CS** - Control Station (internal only)

## State Topics (Subscribe - 1 Hz)
```typescript
/NAV/State           // Navigation state
/HD/State            // Handling Device state
/DRILL/State         // Drill state
/EL/State            // Electronics state
```

## Command Topics (Publish)
```typescript
/NAV/GamepadCmds     // Navigation gamepad
/HD/GamepadCmds      // HD gamepad
/NAV/ChangeSpeed     // Speed adjustment
/EL/LedCommands      // LED control
```

## Services (Call)
```typescript
/NAV/ChangeModeSystem      // Change NAV mode
/HD/ChangeModeSystem       // Change HD mode
/DRILL/ChangeModeSystem    // Change DRILL mode

/NAV/ResetMotors          // Reset motor faults
/NAV/ResetHome            // Set home position

/HD/HumanVerification     // Request user confirmation
/HD/ControlStationSelection  // Request image selection

/EL/mass_req_hd           // Tare HD mass sensor
/EL/mass_req_drill        // Tare drill mass sensor
```

## Actions (Send Goals)
```typescript
/NAV/ReachGoal        // Autonomous navigation
/HD/Manipulation      // Arm manipulation tasks
/DRILL/DrillCmd       // Drilling operations
```

## Usage in Code

### Always Use Topics Enum
```typescript
import { Topics } from "../data/topics.type";

// Good ✅
const topic = new ROSLIB.Topic({
    ros: ros,
    name: Topics.NAV_GAMEPAD_CMDS,
    messageType: "sensor_msgs/Joy"
});

// Bad ❌
const topic = new ROSLIB.Topic({
    ros: ros,
    name: "/NAV/GamepadCmds",  // Hardcoded string
    messageType: "sensor_msgs/Joy"
});
```

### Safe Data Access
```typescript
import { getSubsystemData } from "../utils/roverStateParser";

// Get subsystem data safely
const navData = getSubsystemData(roverState, 'navigation');

if (!navData || !navData['wheels']) {
    return "NO DATA";
}

// Now safe to access
const speed = navData['wheels']['front_left']['speed'];
```

### Check Subsystem Availability
```typescript
// In rosbridgeHooks.ts - already implemented
ros.getNodes((nodes) => {
    const hasNAV = nodes.some(n => n.includes("/NAV"));
    const hasHD = nodes.some(n => n.includes("/HD"));
    // ... use to enable/disable features
});
```

## ROS2 CLI Quick Commands

### Check Running Nodes
```bash
ros2 node list | grep -E "NAV|HD|DRILL|EL"
```

### Monitor State Topics
```bash
# Check if publishing
ros2 topic list | grep State

# Check rate (should be ~1 Hz)
ros2 topic hz /NAV/State

# See content
ros2 topic echo /NAV/State
```

### Test Services
```bash
# List available services
ros2 service list | grep NAV

# Call service
ros2 service call /NAV/ResetMotors std_srvs/srv/SetBool "{data: true}"
```

### Test Actions
```bash
# List actions
ros2 action list

# Send goal
ros2 action send_goal /NAV/ReachGoal custom_msg/action/NAVReachGoal \
  "{mode: 2, goal: {x: 1.0, y: 2.0, theta: 0.0}}" --feedback
```

## Troubleshooting

### Frontend Not Receiving Data?
1. Check rosbridge running: `ros2 node list | grep rosbridge`
2. Check subsystem nodes running: `ros2 node list | grep -E "NAV|HD"`
3. Check topics publishing: `ros2 topic hz /NAV/State`
4. Check browser console for ROS connection errors

### Commands Not Working?
1. Verify topic names match: `ros2 topic list`
2. Check message types: `ros2 topic info /NAV/GamepadCmds`
3. Test with CLI first: `ros2 topic pub /NAV/GamepadCmds ...`
4. Check rosbridge logs for errors

### Subsystem Shows Offline?
1. Check node running: `ros2 node list`
2. Check namespace correct: Topics should start with `/NAV/`, `/HD/`, etc.
3. Restart subsystem node
4. Check ROS_DOMAIN_ID matches

## File Locations

- **Topic Definitions:** `frontend/src/data/topics.type.ts`
- **State Subscription:** `frontend/src/hooks/roverStateHooks.ts`
- **State Parsing:** `frontend/src/utils/roverStateParser.ts`
- **Gamepad Publishing:** `frontend/src/hooks/gamepadHooks.ts`
- **Mode Changes:** `frontend/src/utils/changeSystemMode.ts`
- **Action Management:** `frontend/src/hooks/actionsHooks.ts`

## Adding a New Subsystem

1. **Add to Topics enum** (`topics.type.ts`):
```typescript
NEWSUB_STATE = "/NEWSUB/State",
NEWSUB_GAMEPAD_CMDS = "/NEWSUB/GamepadCmds",
NEWSUB_CHANGE_MODE = "/NEWSUB/ChangeModeSystem",
```

2. **Add state subscription** (`roverStateHooks.ts`):
```typescript
const newsubListener = new ROSLIB.Topic({
    ros: ros,
    name: Topics.NEWSUB_STATE,
    messageType: "std_msgs/String",
    queue_length: 1,
});

newsubListener.subscribe((message) => {
    const data = JSON.parse((message as any).data);
    setRoverState(prev => ({ ...prev, new_subsystem: data }));
});
```

3. **Add parser functions** (`roverStateParser.ts`):
```typescript
const getNewSubData = (data: any) => {
    const newsubData = getSubsystemData(data, 'new_subsystem');
    
    if (!newsubData) {
        return "NO DATA";
    }
    
    return newsubData['some_field'];
};
```

4. **Add mode change mapping** (`changeSystemMode.ts`):
```typescript
[SubSystems.NEW_SUBSYSTEM]: {
    topic: Topics.NEWSUB_CHANGE_MODE,
    type: "custom_msg/srv/ChangeModeSystem",
},
```

5. **Update connection check** (`rosbridgeHooks.ts`):
```typescript
const hasNEWSUB = nodes.some(n => n.includes("/NEWSUB"));
// Add to connection logic
```

That's it! The subsystem is now integrated.

---

**Last Updated:** November 12, 2025
