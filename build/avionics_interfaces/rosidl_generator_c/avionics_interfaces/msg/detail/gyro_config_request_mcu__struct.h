// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/GyroConfigRequestMCU.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_REQUEST_MCU__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_REQUEST_MCU__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/GyroConfigRequestMCU in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__GyroConfigRequestMCU
{
  uint16_t id;
  bool req_bias;
} avionics_interfaces__msg__GyroConfigRequestMCU;

// Struct for a sequence of avionics_interfaces__msg__GyroConfigRequestMCU.
typedef struct avionics_interfaces__msg__GyroConfigRequestMCU__Sequence
{
  avionics_interfaces__msg__GyroConfigRequestMCU * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__GyroConfigRequestMCU__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_REQUEST_MCU__STRUCT_H_
