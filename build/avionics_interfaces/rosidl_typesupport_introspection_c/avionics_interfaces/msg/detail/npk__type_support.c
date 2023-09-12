// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from avionics_interfaces:msg/NPK.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "avionics_interfaces/msg/detail/npk__rosidl_typesupport_introspection_c.h"
#include "avionics_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "avionics_interfaces/msg/detail/npk__functions.h"
#include "avionics_interfaces/msg/detail/npk__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void NPK__rosidl_typesupport_introspection_c__NPK_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  avionics_interfaces__msg__NPK__init(message_memory);
}

void NPK__rosidl_typesupport_introspection_c__NPK_fini_function(void * message_memory)
{
  avionics_interfaces__msg__NPK__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember NPK__rosidl_typesupport_introspection_c__NPK_message_member_array[4] = {
  {
    "id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__NPK, id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "nitrogen",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__NPK, nitrogen),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "phosphorus",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__NPK, phosphorus),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "potassium",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__NPK, potassium),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers NPK__rosidl_typesupport_introspection_c__NPK_message_members = {
  "avionics_interfaces__msg",  // message namespace
  "NPK",  // message name
  4,  // number of fields
  sizeof(avionics_interfaces__msg__NPK),
  NPK__rosidl_typesupport_introspection_c__NPK_message_member_array,  // message members
  NPK__rosidl_typesupport_introspection_c__NPK_init_function,  // function to initialize message memory (memory has to be allocated)
  NPK__rosidl_typesupport_introspection_c__NPK_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t NPK__rosidl_typesupport_introspection_c__NPK_message_type_support_handle = {
  0,
  &NPK__rosidl_typesupport_introspection_c__NPK_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_avionics_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, avionics_interfaces, msg, NPK)() {
  if (!NPK__rosidl_typesupport_introspection_c__NPK_message_type_support_handle.typesupport_identifier) {
    NPK__rosidl_typesupport_introspection_c__NPK_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &NPK__rosidl_typesupport_introspection_c__NPK_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
