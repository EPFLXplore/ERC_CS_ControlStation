// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/PotConfigRequestMCU.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_REQUEST_MCU__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_REQUEST_MCU__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/PotConfigRequestMCU in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__PotConfigRequestMCU
{
  uint16_t id;
  bool req_min_voltages;
  bool req_max_voltages;
  bool req_min_angles;
  bool req_max_angles;
  bool req_channels_status;
} avionics_interfaces__msg__PotConfigRequestMCU;

// Struct for a sequence of avionics_interfaces__msg__PotConfigRequestMCU.
typedef struct avionics_interfaces__msg__PotConfigRequestMCU__Sequence
{
  avionics_interfaces__msg__PotConfigRequestMCU * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__PotConfigRequestMCU__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_REQUEST_MCU__STRUCT_H_
