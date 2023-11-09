// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/ServoConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_RESPONSE__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_RESPONSE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/ServoConfigResponse in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__ServoConfigResponse
{
  uint16_t id;
  float min_duty[4];
  float max_duty[4];
  float min_angles[4];
  float max_angles[4];
  bool remote_command;
  bool set_min_duty;
  bool set_max_duty;
  bool set_min_angles;
  bool set_max_angles;
  bool success;
} avionics_interfaces__msg__ServoConfigResponse;

// Struct for a sequence of avionics_interfaces__msg__ServoConfigResponse.
typedef struct avionics_interfaces__msg__ServoConfigResponse__Sequence
{
  avionics_interfaces__msg__ServoConfigResponse * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__ServoConfigResponse__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_RESPONSE__STRUCT_H_
