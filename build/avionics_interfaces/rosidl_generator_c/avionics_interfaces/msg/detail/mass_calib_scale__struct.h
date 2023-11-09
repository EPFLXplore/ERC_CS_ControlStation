// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/MassCalibScale.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MASS_CALIB_SCALE__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__MASS_CALIB_SCALE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/MassCalibScale in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__MassCalibScale
{
  uint16_t destination_id;
  uint8_t channel;
  float expected_weight;
} avionics_interfaces__msg__MassCalibScale;

// Struct for a sequence of avionics_interfaces__msg__MassCalibScale.
typedef struct avionics_interfaces__msg__MassCalibScale__Sequence
{
  avionics_interfaces__msg__MassCalibScale * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__MassCalibScale__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MASS_CALIB_SCALE__STRUCT_H_
