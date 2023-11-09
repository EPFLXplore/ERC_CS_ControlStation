// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/MassConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_RESPONSE__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_RESPONSE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/MassConfigResponse in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__MassConfigResponse
{
  uint16_t id;
  float offset[4];
  float scale[4];
  float alpha;
  bool enabled_channels[4];
  bool remote_command;
  bool set_offset;
  bool set_scale;
  bool set_alpha;
  bool set_channels_status;
  bool success;
} avionics_interfaces__msg__MassConfigResponse;

// Struct for a sequence of avionics_interfaces__msg__MassConfigResponse.
typedef struct avionics_interfaces__msg__MassConfigResponse__Sequence
{
  avionics_interfaces__msg__MassConfigResponse * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__MassConfigResponse__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_RESPONSE__STRUCT_H_
