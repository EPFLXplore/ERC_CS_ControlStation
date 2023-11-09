// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from avionics_interfaces:msg/FourInOne.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "avionics_interfaces/msg/detail/four_in_one__rosidl_typesupport_introspection_c.h"
#include "avionics_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "avionics_interfaces/msg/detail/four_in_one__functions.h"
#include "avionics_interfaces/msg/detail/four_in_one__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void FourInOne__rosidl_typesupport_introspection_c__FourInOne_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  avionics_interfaces__msg__FourInOne__init(message_memory);
}

void FourInOne__rosidl_typesupport_introspection_c__FourInOne_fini_function(void * message_memory)
{
  avionics_interfaces__msg__FourInOne__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember FourInOne__rosidl_typesupport_introspection_c__FourInOne_message_member_array[5] = {
  {
    "id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__FourInOne, id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "temperature",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__FourInOne, temperature),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "moisture",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__FourInOne, moisture),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "conductivity",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__FourInOne, conductivity),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "ph",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__FourInOne, ph),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers FourInOne__rosidl_typesupport_introspection_c__FourInOne_message_members = {
  "avionics_interfaces__msg",  // message namespace
  "FourInOne",  // message name
  5,  // number of fields
  sizeof(avionics_interfaces__msg__FourInOne),
  FourInOne__rosidl_typesupport_introspection_c__FourInOne_message_member_array,  // message members
  FourInOne__rosidl_typesupport_introspection_c__FourInOne_init_function,  // function to initialize message memory (memory has to be allocated)
  FourInOne__rosidl_typesupport_introspection_c__FourInOne_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t FourInOne__rosidl_typesupport_introspection_c__FourInOne_message_type_support_handle = {
  0,
  &FourInOne__rosidl_typesupport_introspection_c__FourInOne_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_avionics_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, avionics_interfaces, msg, FourInOne)() {
  if (!FourInOne__rosidl_typesupport_introspection_c__FourInOne_message_type_support_handle.typesupport_identifier) {
    FourInOne__rosidl_typesupport_introspection_c__FourInOne_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &FourInOne__rosidl_typesupport_introspection_c__FourInOne_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
