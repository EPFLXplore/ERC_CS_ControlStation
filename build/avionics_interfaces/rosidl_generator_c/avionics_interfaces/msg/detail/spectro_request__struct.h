// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/SpectroRequest.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__SPECTRO_REQUEST__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__SPECTRO_REQUEST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/SpectroRequest in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__SpectroRequest
{
  uint16_t destination_id;
  bool measure;
} avionics_interfaces__msg__SpectroRequest;

// Struct for a sequence of avionics_interfaces__msg__SpectroRequest.
typedef struct avionics_interfaces__msg__SpectroRequest__Sequence
{
  avionics_interfaces__msg__SpectroRequest * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__SpectroRequest__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__SPECTRO_REQUEST__STRUCT_H_
