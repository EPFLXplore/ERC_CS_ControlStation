// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/AccelConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_RESPONSE__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_RESPONSE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/AccelConfigResponse in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__AccelConfigResponse
{
  uint16_t id;
  float bias[3];
  float transform[9];
  bool remote_command;
  bool set_bias;
  bool set_transform;
  bool success;
} avionics_interfaces__msg__AccelConfigResponse;

// Struct for a sequence of avionics_interfaces__msg__AccelConfigResponse.
typedef struct avionics_interfaces__msg__AccelConfigResponse__Sequence
{
  avionics_interfaces__msg__AccelConfigResponse * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__AccelConfigResponse__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_RESPONSE__STRUCT_H_
