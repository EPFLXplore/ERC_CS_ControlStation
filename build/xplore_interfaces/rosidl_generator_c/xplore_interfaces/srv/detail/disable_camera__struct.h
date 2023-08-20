// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from xplore_interfaces:srv/DisableCamera.idl
// generated code does not contain a copyright notice

#ifndef XPLORE_INTERFACES__SRV__DETAIL__DISABLE_CAMERA__STRUCT_H_
#define XPLORE_INTERFACES__SRV__DETAIL__DISABLE_CAMERA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in srv/DisableCamera in the package xplore_interfaces.
typedef struct xplore_interfaces__srv__DisableCamera_Request
{
  int8_t index;
} xplore_interfaces__srv__DisableCamera_Request;

// Struct for a sequence of xplore_interfaces__srv__DisableCamera_Request.
typedef struct xplore_interfaces__srv__DisableCamera_Request__Sequence
{
  xplore_interfaces__srv__DisableCamera_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} xplore_interfaces__srv__DisableCamera_Request__Sequence;


// Constants defined in the message

// Struct defined in srv/DisableCamera in the package xplore_interfaces.
typedef struct xplore_interfaces__srv__DisableCamera_Response
{
  bool success;
} xplore_interfaces__srv__DisableCamera_Response;

// Struct for a sequence of xplore_interfaces__srv__DisableCamera_Response.
typedef struct xplore_interfaces__srv__DisableCamera_Response__Sequence
{
  xplore_interfaces__srv__DisableCamera_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} xplore_interfaces__srv__DisableCamera_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // XPLORE_INTERFACES__SRV__DETAIL__DISABLE_CAMERA__STRUCT_H_
