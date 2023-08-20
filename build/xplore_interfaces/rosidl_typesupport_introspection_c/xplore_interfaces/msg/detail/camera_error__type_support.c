// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from xplore_interfaces:msg/CameraError.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "xplore_interfaces/msg/detail/camera_error__rosidl_typesupport_introspection_c.h"
#include "xplore_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "xplore_interfaces/msg/detail/camera_error__functions.h"
#include "xplore_interfaces/msg/detail/camera_error__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void CameraError__rosidl_typesupport_introspection_c__CameraError_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  xplore_interfaces__msg__CameraError__init(message_memory);
}

void CameraError__rosidl_typesupport_introspection_c__CameraError_fini_function(void * message_memory)
{
  xplore_interfaces__msg__CameraError__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember CameraError__rosidl_typesupport_introspection_c__CameraError_message_member_array[2] = {
  {
    "index",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(xplore_interfaces__msg__CameraError, index),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "ip_adresse",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(xplore_interfaces__msg__CameraError, ip_adresse),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers CameraError__rosidl_typesupport_introspection_c__CameraError_message_members = {
  "xplore_interfaces__msg",  // message namespace
  "CameraError",  // message name
  2,  // number of fields
  sizeof(xplore_interfaces__msg__CameraError),
  CameraError__rosidl_typesupport_introspection_c__CameraError_message_member_array,  // message members
  CameraError__rosidl_typesupport_introspection_c__CameraError_init_function,  // function to initialize message memory (memory has to be allocated)
  CameraError__rosidl_typesupport_introspection_c__CameraError_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t CameraError__rosidl_typesupport_introspection_c__CameraError_message_type_support_handle = {
  0,
  &CameraError__rosidl_typesupport_introspection_c__CameraError_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_xplore_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, xplore_interfaces, msg, CameraError)() {
  if (!CameraError__rosidl_typesupport_introspection_c__CameraError_message_type_support_handle.typesupport_identifier) {
    CameraError__rosidl_typesupport_introspection_c__CameraError_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &CameraError__rosidl_typesupport_introspection_c__CameraError_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
