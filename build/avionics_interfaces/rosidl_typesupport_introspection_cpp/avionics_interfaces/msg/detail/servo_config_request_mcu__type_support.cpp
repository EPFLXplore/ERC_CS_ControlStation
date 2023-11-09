// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from avionics_interfaces:msg/ServoConfigRequestMCU.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "avionics_interfaces/msg/detail/servo_config_request_mcu__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace avionics_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void ServoConfigRequestMCU_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) avionics_interfaces::msg::ServoConfigRequestMCU(_init);
}

void ServoConfigRequestMCU_fini_function(void * message_memory)
{
  auto typed_message = static_cast<avionics_interfaces::msg::ServoConfigRequestMCU *>(message_memory);
  typed_message->~ServoConfigRequestMCU();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember ServoConfigRequestMCU_message_member_array[5] = {
  {
    "id",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::ServoConfigRequestMCU, id),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "req_min_duty",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::ServoConfigRequestMCU, req_min_duty),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "req_max_duty",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::ServoConfigRequestMCU, req_max_duty),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "req_min_angles",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::ServoConfigRequestMCU, req_min_angles),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "req_max_angles",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::ServoConfigRequestMCU, req_max_angles),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers ServoConfigRequestMCU_message_members = {
  "avionics_interfaces::msg",  // message namespace
  "ServoConfigRequestMCU",  // message name
  5,  // number of fields
  sizeof(avionics_interfaces::msg::ServoConfigRequestMCU),
  ServoConfigRequestMCU_message_member_array,  // message members
  ServoConfigRequestMCU_init_function,  // function to initialize message memory (memory has to be allocated)
  ServoConfigRequestMCU_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t ServoConfigRequestMCU_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &ServoConfigRequestMCU_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace avionics_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<avionics_interfaces::msg::ServoConfigRequestMCU>()
{
  return &::avionics_interfaces::msg::rosidl_typesupport_introspection_cpp::ServoConfigRequestMCU_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, avionics_interfaces, msg, ServoConfigRequestMCU)() {
  return &::avionics_interfaces::msg::rosidl_typesupport_introspection_cpp::ServoConfigRequestMCU_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
