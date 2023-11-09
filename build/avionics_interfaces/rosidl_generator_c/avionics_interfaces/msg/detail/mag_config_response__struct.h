// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/MagConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_RESPONSE__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_RESPONSE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/MagConfigResponse in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__MagConfigResponse
{
  uint16_t id;
  float hard_iron[3];
  float soft_iron[9];
  bool remote_command;
  bool set_hard_iron;
  bool set_soft_iron;
  bool success;
} avionics_interfaces__msg__MagConfigResponse;

// Struct for a sequence of avionics_interfaces__msg__MagConfigResponse.
typedef struct avionics_interfaces__msg__MagConfigResponse__Sequence
{
  avionics_interfaces__msg__MagConfigResponse * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__MagConfigResponse__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_RESPONSE__STRUCT_H_
