// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from avionics_interfaces:msg/MagConfigRequestJetson.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "avionics_interfaces/msg/detail/mag_config_request_jetson__rosidl_typesupport_introspection_c.h"
#include "avionics_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "avionics_interfaces/msg/detail/mag_config_request_jetson__functions.h"
#include "avionics_interfaces/msg/detail/mag_config_request_jetson__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void MagConfigRequestJetson__rosidl_typesupport_introspection_c__MagConfigRequestJetson_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  avionics_interfaces__msg__MagConfigRequestJetson__init(message_memory);
}

void MagConfigRequestJetson__rosidl_typesupport_introspection_c__MagConfigRequestJetson_fini_function(void * message_memory)
{
  avionics_interfaces__msg__MagConfigRequestJetson__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember MagConfigRequestJetson__rosidl_typesupport_introspection_c__MagConfigRequestJetson_message_member_array[6] = {
  {
    "destination_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__MagConfigRequestJetson, destination_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "hard_iron",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__MagConfigRequestJetson, hard_iron),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "soft_iron",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    9,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__MagConfigRequestJetson, soft_iron),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "remote_command",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__MagConfigRequestJetson, remote_command),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "set_hard_iron",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__MagConfigRequestJetson, set_hard_iron),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "set_soft_iron",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces__msg__MagConfigRequestJetson, set_soft_iron),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers MagConfigRequestJetson__rosidl_typesupport_introspection_c__MagConfigRequestJetson_message_members = {
  "avionics_interfaces__msg",  // message namespace
  "MagConfigRequestJetson",  // message name
  6,  // number of fields
  sizeof(avionics_interfaces__msg__MagConfigRequestJetson),
  MagConfigRequestJetson__rosidl_typesupport_introspection_c__MagConfigRequestJetson_message_member_array,  // message members
  MagConfigRequestJetson__rosidl_typesupport_introspection_c__MagConfigRequestJetson_init_function,  // function to initialize message memory (memory has to be allocated)
  MagConfigRequestJetson__rosidl_typesupport_introspection_c__MagConfigRequestJetson_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t MagConfigRequestJetson__rosidl_typesupport_introspection_c__MagConfigRequestJetson_message_type_support_handle = {
  0,
  &MagConfigRequestJetson__rosidl_typesupport_introspection_c__MagConfigRequestJetson_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_avionics_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, avionics_interfaces, msg, MagConfigRequestJetson)() {
  if (!MagConfigRequestJetson__rosidl_typesupport_introspection_c__MagConfigRequestJetson_message_type_support_handle.typesupport_identifier) {
    MagConfigRequestJetson__rosidl_typesupport_introspection_c__MagConfigRequestJetson_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &MagConfigRequestJetson__rosidl_typesupport_introspection_c__MagConfigRequestJetson_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
