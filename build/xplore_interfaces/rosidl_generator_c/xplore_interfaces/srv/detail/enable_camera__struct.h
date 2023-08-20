// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from xplore_interfaces:srv/EnableCamera.idl
// generated code does not contain a copyright notice

#ifndef XPLORE_INTERFACES__SRV__DETAIL__ENABLE_CAMERA__STRUCT_H_
#define XPLORE_INTERFACES__SRV__DETAIL__ENABLE_CAMERA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in srv/EnableCamera in the package xplore_interfaces.
typedef struct xplore_interfaces__srv__EnableCamera_Request
{
  int8_t index;
} xplore_interfaces__srv__EnableCamera_Request;

// Struct for a sequence of xplore_interfaces__srv__EnableCamera_Request.
typedef struct xplore_interfaces__srv__EnableCamera_Request__Sequence
{
  xplore_interfaces__srv__EnableCamera_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} xplore_interfaces__srv__EnableCamera_Request__Sequence;


// Constants defined in the message

// Struct defined in srv/EnableCamera in the package xplore_interfaces.
typedef struct xplore_interfaces__srv__EnableCamera_Response
{
  bool success;
  int64_t ip_adresse;
} xplore_interfaces__srv__EnableCamera_Response;

// Struct for a sequence of xplore_interfaces__srv__EnableCamera_Response.
typedef struct xplore_interfaces__srv__EnableCamera_Response__Sequence
{
  xplore_interfaces__srv__EnableCamera_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} xplore_interfaces__srv__EnableCamera_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // XPLORE_INTERFACES__SRV__DETAIL__ENABLE_CAMERA__STRUCT_H_
