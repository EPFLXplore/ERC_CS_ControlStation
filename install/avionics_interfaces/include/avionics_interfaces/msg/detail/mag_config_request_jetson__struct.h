// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/MagConfigRequestJetson.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_REQUEST_JETSON__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_REQUEST_JETSON__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/MagConfigRequestJetson in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__MagConfigRequestJetson
{
  uint16_t destination_id;
  float hard_iron[3];
  float soft_iron[9];
  bool remote_command;
  bool set_hard_iron;
  bool set_soft_iron;
} avionics_interfaces__msg__MagConfigRequestJetson;

// Struct for a sequence of avionics_interfaces__msg__MagConfigRequestJetson.
typedef struct avionics_interfaces__msg__MagConfigRequestJetson__Sequence
{
  avionics_interfaces__msg__MagConfigRequestJetson * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__MagConfigRequestJetson__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_REQUEST_JETSON__STRUCT_H_
