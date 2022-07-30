// Auto-generated. Do not edit!

// (in-package custom_msg_python.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class move_base_action_goal {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.currId = null;
      this.moveBaseGoal = null;
    }
    else {
      if (initObj.hasOwnProperty('currId')) {
        this.currId = initObj.currId
      }
      else {
        this.currId = new std_msgs.msg.Int8();
      }
      if (initObj.hasOwnProperty('moveBaseGoal')) {
        this.moveBaseGoal = initObj.moveBaseGoal
      }
      else {
        this.moveBaseGoal = new geometry_msgs.msg.Pose();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type move_base_action_goal
    // Serialize message field [currId]
    bufferOffset = std_msgs.msg.Int8.serialize(obj.currId, buffer, bufferOffset);
    // Serialize message field [moveBaseGoal]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.moveBaseGoal, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type move_base_action_goal
    let len;
    let data = new move_base_action_goal(null);
    // Deserialize message field [currId]
    data.currId = std_msgs.msg.Int8.deserialize(buffer, bufferOffset);
    // Deserialize message field [moveBaseGoal]
    data.moveBaseGoal = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 57;
  }

  static datatype() {
    // Returns string type for a message object
    return 'custom_msg_python/move_base_action_goal';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '512860f1cd6d90bb8cf7bd87927bb3d7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    std_msgs/Int8 currId
    geometry_msgs/Pose moveBaseGoal
    
    ================================================================================
    MSG: std_msgs/Int8
    int8 data
    
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new move_base_action_goal(null);
    if (msg.currId !== undefined) {
      resolved.currId = std_msgs.msg.Int8.Resolve(msg.currId)
    }
    else {
      resolved.currId = new std_msgs.msg.Int8()
    }

    if (msg.moveBaseGoal !== undefined) {
      resolved.moveBaseGoal = geometry_msgs.msg.Pose.Resolve(msg.moveBaseGoal)
    }
    else {
      resolved.moveBaseGoal = new geometry_msgs.msg.Pose()
    }

    return resolved;
    }
};

module.exports = move_base_action_goal;
