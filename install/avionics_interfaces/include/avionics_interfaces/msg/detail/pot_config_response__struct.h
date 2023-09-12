// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/PotConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_RESPONSE__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_RESPONSE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/PotConfigResponse in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__PotConfigResponse
{
  uint16_t id;
  float min_voltages[4];
  float max_voltages[4];
  float min_angles[4];
  float max_angles[4];
  bool enabled_channels[4];
  bool remote_command;
  bool set_min_voltages;
  bool set_max_voltages;
  bool set_min_angles;
  bool set_max_angles;
  bool set_channels_status;
  bool success;
} avionics_interfaces__msg__PotConfigResponse;

// Struct for a sequence of avionics_interfaces__msg__PotConfigResponse.
typedef struct avionics_interfaces__msg__PotConfigResponse__Sequence
{
  avionics_interfaces__msg__PotConfigResponse * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__PotConfigResponse__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_RESPONSE__STRUCT_H_
