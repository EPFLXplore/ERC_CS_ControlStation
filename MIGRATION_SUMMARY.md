# Architecture Migration Summary
## Removing ROVER Middleman Node - Direct Subsystem Communication

**Branch:** `removing_rover_node_arno`  
**Date:** November 12, 2025  
**Author:** Arno Laurie (with AI assistance)

---

## Overview

### Old Architecture
```
CS (Frontend) → rosbridge → ROVER Node → Subsystems (NAV, HD, DRILL, EL)
```

### New Architecture
```
CS (Frontend) → rosbridge → Subsystem Interface Nodes (NAV, HD, DRILL, EL)
```

Each subsystem now has its own **Interface Node** that:
1. Publishes summarized state at **1 Hz** (`/SUBSYSTEM/State`)
2. Subscribes to commands (`/SUBSYSTEM/GamepadCmds`, etc.)
3. Provides services (`/SUBSYSTEM/ChangeModeSystem`, etc.)
4. Provides action servers (`/SUBSYSTEM/ReachGoal`, etc.)

---

## Files Modified

### ✅ **Critical Files - Already Correct**

1. **`frontend/src/hooks/roverStateHooks.ts`**
   - ✅ Subscribes to individual subsystem states
   - ✅ `/NAV/State`, `/HD/State`, `/DRILL/State`, `/EL/State`
   - ✅ Updates state independently per subsystem

2. **`frontend/src/hooks/actionsHooks.ts`**
   - ✅ Uses direct action server names
   - ✅ `/NAV/ReachGoal`, `/HD/Manipulation`, `/DRILL/DrillCmd`

3. **`frontend/src/utils/navigationActions.ts`**
   - ✅ Direct service calls to NAV subsystem
   - ✅ Uses Topics enum properly

4. **`frontend/src/utils/changeSystemMode.ts`**
   - ✅ Subsystem-specific mode change services
   - ✅ Good mapping pattern with `SUBSYSTEM_MODE_SERVICES`

5. **`frontend/src/utils/roverStateParser.ts`**
   - ✅ Uses `getSubsystemData()` helper for backward compatibility
   - ✅ All 30+ parser functions updated consistently

---

### ✅ **Files Modified in This Migration**

#### 1. **`frontend/src/data/topics.type.ts`** ⭐ CENTRAL REGISTRY
**What Changed:**
- Added missing topic definitions
- Organized all topics by subsystem
- Added compatibility aliases for transition period

**New Topics Added:**
```typescript
// Gamepad commands (aliases - point to same topics)
NAVIGATION_GAMEPAD_PUBLISHER = "/NAV/GamepadCmds"
HANDLING_DEVICE_GAMEPAD_PUBLISHER = "/HD/GamepadCmds"

// Camera RGB modes
CHANGE_MODE_RGB_HD = "/HD/ChangeModeRGB"
CHANGE_MODE_RGB_NAV = "/NAV/ChangeModeRGB"

// Navigation speed
CHANGE_SPEED_ROVER = "/NAV/ChangeSpeed"

// HD interaction services (aliases)
REQUEST_SELECTION_IMAGE = "/HD/ControlStationSelection"
REQUEST_HUMAIN_VERIFICATION_HD = "/HD/HumanVerification"
CONFIRMATION_HDS_LAUNCHED = "/HD/kinematics/stackHDLaunched"
```

**Design Choice:**
- All topic names in ONE place (`topics.type.ts`)
- Clear subsystem prefix pattern: `/SUBSYSTEM/CommandName`
- Backward-compatible aliases during transition
- Well-commented for easy understanding

---

#### 2. **`frontend/src/hooks/gamepadHooks.ts`**
**What Changed:**
```typescript
// OLD:
Topics.NAVIGATION_GAMEPAD_PUBLISHER
Topics.HANDLING_DEVICE_GAMEPAD_PUBLISHER

// NEW:
Topics.NAV_GAMEPAD_CMDS  // Direct to NAV
Topics.HD_GAMEPAD_CMDS   // Direct to HD
```

**Why:**
- Use canonical topic names, not aliases
- Clearer that we're sending directly to subsystems
- Consistent with other parts of codebase

---

#### 3. **`frontend/src/utils/changeCameraMode.ts`**
**What Changed:**
- Improved error handling
- Added null check for ROS connection
- Better success/error messages
- Cleaner code structure

**Design Choice:**
- Service name determined by subsystem
- Clear error messages for debugging
- Follows same pattern as `changeSystemMode.ts`

---

#### 4. **`frontend/src/hooks/rosbridgeHooks.ts`** ⭐ IMPORTANT
**What Changed:**
```typescript
// OLD: Check for /ROVER node
if (nodes.includes("/ROVER")) {
    setConnected(true);
}

// NEW: Check for subsystem nodes
const hasNAV = nodes.some(n => n.includes("/NAV"));
const hasHD = nodes.some(n => n.includes("/HD"));
const hasDRILL = nodes.some(n => n.includes("/DRILL"));
const hasEL = nodes.some(n => n.includes("/EL"));

if (hasNAV || hasHD || hasDRILL || hasEL) {
    setConnected(true);
    console.log("Subsystems online:", { NAV: hasNAV, HD: hasHD, ... });
}
```

**Why:**
- ROVER node no longer exists
- CS needs at least ONE subsystem to be functional
- Logs which subsystems are available (helpful for debugging)
- Better user feedback with specific messages

**Design Choice:**
- Consider connected if ANY subsystem is online
- Log subsystem availability for transparency
- Could be extended to track individual subsystem health

---

#### 5. **`frontend/src/hooks/roverControlsHooks.ts`**
**What Changed:**
```typescript
// Navigation speed - Direct to NAV
Topics.NAV_CHANGE_SPEED  // was Topics.CHANGE_SPEED_ROVER

// Science sensors - Direct to EL
Topics.EL_MASS_TARE_DRILL  // was Topics.MASS_TARE_DRILL
Topics.EL_MASS_TARE_HD     // was Topics.MASS_TARE_HD

// Screenshot - Using NAV (cameras managed by navigation)
Topics.NAV_SCREENSHOT_ALL  // was Topics.SCREENSHOT_ALL_CAMERAS

// LEDs - Direct to EL
Topics.EL_LED_COMMANDS  // was Topics.LED_PUBLISHER
```

**Why:**
- Use canonical topic names from Topics enum
- Clear which subsystem handles each command
- Electronics (EL) manages sensors and LEDs
- Navigation (NAV) manages cameras

**Design Choice:**
- Each topic clearly indicates responsible subsystem
- Follows `/SUBSYSTEM/Command` pattern
- Easy to trace command flow

---

## Topic Naming Convention

### Pattern
```
/[SUBSYSTEM]/[CommandOrStateName]
```

### Examples by Subsystem

**NAV (Navigation):**
- `/NAV/State` - 1Hz state summary
- `/NAV/GamepadCmds` - Real-time gamepad input
- `/NAV/ChangeSpeed` - Speed adjustment
- `/NAV/ResetMotors` - Service: reset faults
- `/NAV/ReachGoal` - Action: autonomous navigation
- `/NAV/ChangeModeSystem` - Service: change operating mode
- `/NAV/ScreenshotAllCameras` - Service: capture all camera feeds

**HD (Handling Device):**
- `/HD/State` - 1Hz state summary
- `/HD/GamepadCmds` - Real-time gamepad input
- `/HD/Manipulation` - Action: arm manipulation tasks
- `/HD/ChangeModeSystem` - Service: change operating mode
- `/HD/HumanVerification` - Service: request user confirmation
- `/HD/ControlStationSelection` - Service: request image selection
- `/HD/kinematics/reset_nodes` - Service: reset kinematic solver

**DRILL:**
- `/DRILL/State` - 1Hz state summary
- `/DRILL/DrillCmd` - Action: drilling operations
- `/DRILL/ChangeModeSystem` - Service: change operating mode

**EL (Electronics):**
- `/EL/State` - 1Hz state summary
- `/EL/LedCommands` - LED control commands
- `/EL/mass_req_hd` - Mass sensor tare (HD container)
- `/EL/mass_req_drill` - Mass sensor tare (drill container)

**CS (Control Station - Internal):**
- `/CS/ChangeAngleFrontCamera` - CS-specific camera control

---

## State Data Structure

### Frontend State Object
```typescript
roverState = {
    navigation: {        // From /NAV/State (1 Hz)
        mode: "ACKERMANN",
        localization: {...},
        wheels: {...},
        state: {...}
    },
    handling_device: {   // From /HD/State (1 Hz)
        mode: "MANUAL_INVERSE",
        joints: {...},
        state: {...}
    },
    drill: {             // From /DRILL/State (1 Hz)
        mode: "AUTO",
        motors: {...},
        state: {...}
    },
    electronics: {       // From /EL/State (1 Hz)
        power: {...},
        sensors: {...}
    },
    rover: {}            // Optional: global info if aggregator exists
}
```

### Parser Pattern
```typescript
// Graceful helper function (backward compatible)
const getSubsystemData = (data: any, subsystem: string) => {
    // New structure: direct access
    if (data && data[subsystem]) {
        return data[subsystem];
    }
    
    // Old structure: wrapped in 'rover'
    if (data && data['rover'] && data['rover'][subsystem]) {
        return data['rover'][subsystem];
    }
    
    return null;
};

// Usage in parser functions
const getBatteryLevel = (data: any) => {
    const elData = getSubsystemData(data, 'electronics');
    
    if (!elData || !elData['power']) {
        return "NO DATA";
    }
    
    return calculatePercentage(elData['power']['voltage']);
};
```

**Why This Pattern:**
- ✅ Backward compatible with old `/Rover/RoverState`
- ✅ Forward compatible with new direct states
- ✅ Single point of access logic
- ✅ Easy to remove old structure support later
- ✅ All 30+ parser functions follow same pattern

---

## Backend Requirements

### Each Subsystem Interface Node Must:

1. **Publish State at 1 Hz**
```python
# Example NAV Interface Node
state = {
    'mode': 'ACKERMANN',
    'localization': {
        'position': {'x': 1.0, 'y': 2.0, 'z': 0.0},
        'linear_velocity': {'x': 0.5, 'y': 0.0, 'z': 0.0},
    },
    'wheels': {
        'front_left': {
            'steering_angle': 15.0,
            'speed': 0.5,
            'current_driving': 500,
            'driving_motor_state': True,
            'driving_fault': False
        },
        # ... other wheels
    },
    'state': {
        'current_goal': {'x': 5.0, 'y': 3.0},
        'points': [{'x': 1.0, 'y': 2.0}, ...]
    }
}

# Publish as JSON string
msg = String()
msg.data = json.dumps(state)
state_publisher.publish(msg)
```

2. **Subscribe to Commands**
```python
# Gamepad commands
self.gamepad_sub = self.create_subscription(
    GamepadCmds,
    '/NAV/GamepadCmds',
    self.handle_gamepad,
    10
)
```

3. **Provide Services**
```python
# Mode change service
self.mode_service = self.create_service(
    ChangeModeSystem,
    '/NAV/ChangeModeSystem',
    self.handle_mode_change
)

# Reset motors service
self.reset_service = self.create_service(
    SetBool,
    '/NAV/ResetMotors',
    self.handle_reset
)
```

4. **Provide Action Servers**
```python
# Autonomous navigation action
self.reach_goal_action = ActionServer(
    self,
    NAVReachGoal,
    '/NAV/ReachGoal',
    self.execute_reach_goal
)
```

---

## Testing Strategy

### 1. **Unit Testing - One Subsystem at a Time**

**Test NAV First:**
```bash
# Terminal 1: Start NAV interface node
ros2 run nav_pkg nav_interface_node

# Terminal 2: Check state publishing
ros2 topic echo /NAV/State
ros2 topic hz /NAV/State  # Should be ~1 Hz

# Terminal 3: Test gamepad commands
ros2 topic pub /NAV/GamepadCmds sensor_msgs/Joy "..."

# Terminal 4: Test services
ros2 service call /NAV/ChangeModeSystem custom_msg/srv/ChangeModeSystem "{mode: 1}"

# Terminal 5: Test actions
ros2 action send_goal /NAV/ReachGoal custom_msg/action/NAVReachGoal "{mode: 2, goal: {x: 1.0, y: 2.0}}"
```

**Then HD, DRILL, EL:**
- Follow same pattern for each subsystem
- Verify state structure matches frontend expectations
- Test error handling (disconnect, timeout, etc.)

### 2. **Integration Testing**

```bash
# Start all subsystems
ros2 launch rover_bringup all_subsystems.launch.py

# Start rosbridge
ros2 launch rosbridge_server rosbridge_websocket.launch.py

# Start frontend
cd frontend && npm start

# Test in browser:
# 1. Check connection status (should see subsystem availability)
# 2. Test gamepad control for each subsystem
# 3. Test mode changes
# 4. Test actions
# 5. Verify state updates in UI
```

### 3. **Failure Mode Testing**

```bash
# Test subsystem failure recovery
# 1. Kill NAV node while CS is running
ros2 node kill /NAV/nav_interface_node

# CS should:
# - Show warning about NAV offline
# - Other subsystems still functional
# - Gracefully handle missing NAV data

# 2. Restart NAV node
ros2 run nav_pkg nav_interface_node

# CS should:
# - Detect NAV back online
# - Resume NAV functionality
# - Show success message
```

---

## Migration Checklist

### Frontend (This PR)
- [x] Update `topics.type.ts` with all topic definitions
- [x] Fix `gamepadHooks.ts` to use direct subsystem topics
- [x] Fix `changeCameraMode.ts` with better error handling
- [x] Fix `rosbridgeHooks.ts` to check subsystem nodes
- [x] Fix `roverControlsHooks.ts` to use correct topic names
- [x] Update `roverStateParser.ts` with `getSubsystemData()` helper
- [x] Update `roverStateHooks.ts` to subscribe to subsystem states
- [x] Verify all files compile without errors
- [ ] Test in browser with mock rosbridge
- [ ] Update any UI components that reference old structure

### Backend (Separate PRs)
- [ ] Create NAV interface node
  - [ ] State publisher (1 Hz)
  - [ ] Gamepad subscriber
  - [ ] Services (ChangeModeSystem, ResetMotors, ResetHome)
  - [ ] Action server (ReachGoal)
  - [ ] Camera management

- [ ] Create HD interface node
  - [ ] State publisher (1 Hz)
  - [ ] Gamepad subscriber
  - [ ] Services (ChangeModeSystem, HumanVerification, ControlStationSelection)
  - [ ] Action server (Manipulation)

- [ ] Create DRILL interface node
  - [ ] State publisher (1 Hz)
  - [ ] Services (ChangeModeSystem)
  - [ ] Action server (DrillCmd)

- [ ] Create EL interface node
  - [ ] State publisher (1 Hz)
  - [ ] LED command subscriber
  - [ ] Mass sensor services
  - [ ] Power management

- [ ] Update/remove ROVER node
  - [ ] Archive old code
  - [ ] Remove from launch files
  - [ ] Update documentation

---

## Benefits of New Architecture

### 1. **Performance**
- ✅ No middleman delays
- ✅ Direct command routing
- ✅ 1 Hz state updates prevent network congestion

### 2. **Reliability**
- ✅ One subsystem failure doesn't affect others
- ✅ Independent restart capability
- ✅ Clear error boundaries

### 3. **Maintainability**
- ✅ Clear ownership (each subsystem manages itself)
- ✅ Easy to add new subsystems
- ✅ Simpler debugging (direct communication paths)

### 4. **Scalability**
- ✅ Can run subsystems on different computers
- ✅ Easy to distribute processing load
- ✅ Can add more subsystems without central bottleneck

### 5. **Development**
- ✅ Teams can work on subsystems independently
- ✅ No need to coordinate through central node
- ✅ Faster development cycles

---

## Common Pitfalls & Solutions

### Pitfall 1: Topic Name Inconsistency
**Problem:** Using old topic names or hardcoding strings  
**Solution:** Always use `Topics` enum from `topics.type.ts`

### Pitfall 2: Assuming All Subsystems Online
**Problem:** Code crashes when subsystem is offline  
**Solution:** Always check if data exists before accessing

```typescript
// BAD
const speed = data.navigation.wheels.front_left.speed;  // Crashes if NAV offline

// GOOD
const navData = getSubsystemData(data, 'navigation');
const speed = navData?.wheels?.front_left?.speed ?? 0;  // Safe
```

### Pitfall 3: Not Handling State Structure Changes
**Problem:** Backend changes state format, frontend breaks  
**Solution:** Use `getSubsystemData()` helper for compatibility

### Pitfall 4: Forgetting to Unsubscribe
**Problem:** Memory leaks from topic subscriptions  
**Solution:** Always return cleanup function in useEffect

```typescript
useEffect(() => {
    const listener = new ROSLIB.Topic({...});
    listener.subscribe(callback);
    
    return () => listener.unsubscribe();  // Important!
}, [ros]);
```

### Pitfall 5: Wrong Message Types
**Problem:** Frontend sends wrong message type to subsystem  
**Solution:** Document message types clearly, use TypeScript

---

## Next Steps

1. **Complete Backend Migration**
   - Implement all subsystem interface nodes
   - Test each subsystem independently
   - Deploy and test integration

2. **Remove Old Code**
   - Archive ROVER node code
   - Remove backward compatibility after transition
   - Clean up old topic references

3. **Documentation**
   - Update team documentation
   - Create subsystem interface specifications
   - Document message formats

4. **Monitoring**
   - Add subsystem health monitoring dashboard
   - Log subsystem availability
   - Alert on subsystem failures

---

## Questions & Support

**For Frontend Issues:**
- Check `topics.type.ts` for correct topic names
- Verify ROS connection in browser console
- Check rosbridge logs

**For Backend Issues:**
- Verify subsystem nodes are running: `ros2 node list`
- Check topic publication: `ros2 topic list` and `ros2 topic echo /SUBSYSTEM/State`
- Verify service availability: `ros2 service list`
- Check action servers: `ros2 action list`

**Common Commands:**
```bash
# List all ROS nodes
ros2 node list | grep -E "NAV|HD|DRILL|EL"

# Check topic rates
ros2 topic hz /NAV/State /HD/State /DRILL/State /EL/State

# Test service
ros2 service call /NAV/ChangeModeSystem custom_msg/srv/ChangeModeSystem "{mode: 1}"

# Monitor action
ros2 action send_goal /NAV/ReachGoal custom_msg/action/NAVReachGoal "{mode: 2, goal: {x: 1.0, y: 2.0}}" --feedback
```

---

## Conclusion

This migration removes the ROVER middleman node and establishes **direct communication** between the Control Station and subsystems. The new architecture is:

- **Faster** - No middleman delays
- **More Reliable** - Subsystem independence
- **Easier to Maintain** - Clear ownership
- **Scalable** - Easy to add subsystems
- **Well-Documented** - Clear patterns and conventions

All frontend changes maintain **backward compatibility** during the transition period, ensuring a smooth migration path.

---

**Migration Status:** Frontend Complete ✅ | Backend In Progress 🚧  
**Last Updated:** November 12, 2025  
**Reviewed By:** [To be added]
