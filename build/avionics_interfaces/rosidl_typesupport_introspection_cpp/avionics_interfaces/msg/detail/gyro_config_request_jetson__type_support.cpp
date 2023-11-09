// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from avionics_interfaces:msg/GyroConfigRequestJetson.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "avionics_interfaces/msg/detail/gyro_config_request_jetson__struct.hpp"
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

void GyroConfigRequestJetson_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) avionics_interfaces::msg::GyroConfigRequestJetson(_init);
}

void GyroConfigRequestJetson_fini_function(void * message_memory)
{
  auto typed_message = static_cast<avionics_interfaces::msg::GyroConfigRequestJetson *>(message_memory);
  typed_message->~GyroConfigRequestJetson();
}

size_t size_function__GyroConfigRequestJetson__bias(const void * untyped_member)
{
  (void)untyped_member;
  return 3;
}

const void * get_const_function__GyroConfigRequestJetson__bias(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 3> *>(untyped_member);
  return &member[index];
}

void * get_function__GyroConfigRequestJetson__bias(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 3> *>(untyped_member);
  return &member[index];
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember GyroConfigRequestJetson_message_member_array[4] = {
  {
    "destination_id",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::GyroConfigRequestJetson, destination_id),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "bias",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::GyroConfigRequestJetson, bias),  // bytes offset in struct
    nullptr,  // default value
    size_function__GyroConfigRequestJetson__bias,  // size() function pointer
    get_const_function__GyroConfigRequestJetson__bias,  // get_const(index) function pointer
    get_function__GyroConfigRequestJetson__bias,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "remote_command",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::GyroConfigRequestJetson, remote_command),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "set_bias",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::GyroConfigRequestJetson, set_bias),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers GyroConfigRequestJetson_message_members = {
  "avionics_interfaces::msg",  // message namespace
  "GyroConfigRequestJetson",  // message name
  4,  // number of fields
  sizeof(avionics_interfaces::msg::GyroConfigRequestJetson),
  GyroConfigRequestJetson_message_member_array,  // message members
  GyroConfigRequestJetson_init_function,  // function to initialize message memory (memory has to be allocated)
  GyroConfigRequestJetson_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t GyroConfigRequestJetson_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &GyroConfigRequestJetson_message_members,
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
get_message_type_support_handle<avionics_interfaces::msg::GyroConfigRequestJetson>()
{
  return &::avionics_interfaces::msg::rosidl_typesupport_introspection_cpp::GyroConfigRequestJetson_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, avionics_interfaces, msg, GyroConfigRequestJetson)() {
  return &::avionics_interfaces::msg::rosidl_typesupport_introspection_cpp::GyroConfigRequestJetson_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
