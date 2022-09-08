// Auto-generated. Do not edit!

// (in-package vision_no_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let panel_object = require('./panel_object.js');

//-----------------------------------------------------------

class object_list {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.detected_objects = null;
    }
    else {
      if (initObj.hasOwnProperty('detected_objects')) {
        this.detected_objects = initObj.detected_objects
      }
      else {
        this.detected_objects = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type object_list
    // Serialize message field [detected_objects]
    // Serialize the length for message field [detected_objects]
    bufferOffset = _serializer.uint32(obj.detected_objects.length, buffer, bufferOffset);
    obj.detected_objects.forEach((val) => {
      bufferOffset = panel_object.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type object_list
    let len;
    let data = new object_list(null);
    // Deserialize message field [detected_objects]
    // Deserialize array length for message field [detected_objects]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.detected_objects = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.detected_objects[i] = panel_object.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 42 * object.detected_objects.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'vision_no_ros/object_list';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '93cc90f8ec35aa397138799e59c6bb47';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    panel_object[] detected_objects
    ================================================================================
    MSG: vision_no_ros/panel_object
    int8 id
    int8 reliability
    float32 x_pos
    float32 y_pos
    float32 z_pos
    float32 x_rot
    float32 y_rot
    float32 z_rot
    float32 w_quaternion
    float32 x_quaternion
    float32 y_quaternion
    float32 z_quaternion
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new object_list(null);
    if (msg.detected_objects !== undefined) {
      resolved.detected_objects = new Array(msg.detected_objects.length);
      for (let i = 0; i < resolved.detected_objects.length; ++i) {
        resolved.detected_objects[i] = panel_object.Resolve(msg.detected_objects[i]);
      }
    }
    else {
      resolved.detected_objects = []
    }

    return resolved;
    }
};

module.exports = object_list;
