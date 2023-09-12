// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/Mag.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MAG__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__MAG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'mag_raw'
// Member 'mag_cal'
#include "sensor_msgs/msg/detail/magnetic_field__struct.h"

// Struct defined in msg/Mag in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__Mag
{
  uint16_t id;
  sensor_msgs__msg__MagneticField mag_raw;
  sensor_msgs__msg__MagneticField mag_cal;
} avionics_interfaces__msg__Mag;

// Struct for a sequence of avionics_interfaces__msg__Mag.
typedef struct avionics_interfaces__msg__Mag__Sequence
{
  avionics_interfaces__msg__Mag * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__Mag__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MAG__STRUCT_H_
