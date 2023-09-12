// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/Voltage.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__VOLTAGE__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__VOLTAGE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/Voltage in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__Voltage
{
  uint16_t id;
  float voltage;
} avionics_interfaces__msg__Voltage;

// Struct for a sequence of avionics_interfaces__msg__Voltage.
typedef struct avionics_interfaces__msg__Voltage__Sequence
{
  avionics_interfaces__msg__Voltage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__Voltage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__VOLTAGE__STRUCT_H_
