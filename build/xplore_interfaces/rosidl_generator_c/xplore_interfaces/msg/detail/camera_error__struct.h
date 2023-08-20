// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from xplore_interfaces:msg/CameraError.idl
// generated code does not contain a copyright notice

#ifndef XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__STRUCT_H_
#define XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/CameraError in the package xplore_interfaces.
typedef struct xplore_interfaces__msg__CameraError
{
  int8_t index;
  int64_t ip_adresse;
} xplore_interfaces__msg__CameraError;

// Struct for a sequence of xplore_interfaces__msg__CameraError.
typedef struct xplore_interfaces__msg__CameraError__Sequence
{
  xplore_interfaces__msg__CameraError * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} xplore_interfaces__msg__CameraError__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__STRUCT_H_
