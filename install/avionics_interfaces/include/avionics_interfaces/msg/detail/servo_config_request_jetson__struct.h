// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/ServoConfigRequestJetson.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_REQUEST_JETSON__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_REQUEST_JETSON__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/ServoConfigRequestJetson in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__ServoConfigRequestJetson
{
  uint16_t destination_id;
  float min_duty[4];
  float max_duty[4];
  float min_angles[4];
  float max_angles[4];
  bool remote_command;
  bool set_min_duty;
  bool set_max_duty;
  bool set_min_angles;
  bool set_max_angles;
} avionics_interfaces__msg__ServoConfigRequestJetson;

// Struct for a sequence of avionics_interfaces__msg__ServoConfigRequestJetson.
typedef struct avionics_interfaces__msg__ServoConfigRequestJetson__Sequence
{
  avionics_interfaces__msg__ServoConfigRequestJetson * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__ServoConfigRequestJetson__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_REQUEST_JETSON__STRUCT_H_
