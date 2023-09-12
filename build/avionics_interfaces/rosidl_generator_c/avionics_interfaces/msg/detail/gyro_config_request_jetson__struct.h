// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/GyroConfigRequestJetson.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_REQUEST_JETSON__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_REQUEST_JETSON__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/GyroConfigRequestJetson in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__GyroConfigRequestJetson
{
  uint16_t destination_id;
  float bias[3];
  bool remote_command;
  bool set_bias;
} avionics_interfaces__msg__GyroConfigRequestJetson;

// Struct for a sequence of avionics_interfaces__msg__GyroConfigRequestJetson.
typedef struct avionics_interfaces__msg__GyroConfigRequestJetson__Sequence
{
  avionics_interfaces__msg__GyroConfigRequestJetson * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__GyroConfigRequestJetson__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_REQUEST_JETSON__STRUCT_H_
