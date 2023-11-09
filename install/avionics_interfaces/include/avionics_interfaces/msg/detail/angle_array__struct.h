// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/AngleArray.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__ANGLE_ARRAY__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__ANGLE_ARRAY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/AngleArray in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__AngleArray
{
  uint16_t id;
  float angles[4];
} avionics_interfaces__msg__AngleArray;

// Struct for a sequence of avionics_interfaces__msg__AngleArray.
typedef struct avionics_interfaces__msg__AngleArray__Sequence
{
  avionics_interfaces__msg__AngleArray * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__AngleArray__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__ANGLE_ARRAY__STRUCT_H_
