// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from avionics_interfaces:msg/PotConfigRequestJetson.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "avionics_interfaces/msg/detail/pot_config_request_jetson__struct.hpp"
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

void PotConfigRequestJetson_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) avionics_interfaces::msg::PotConfigRequestJetson(_init);
}

void PotConfigRequestJetson_fini_function(void * message_memory)
{
  auto typed_message = static_cast<avionics_interfaces::msg::PotConfigRequestJetson *>(message_memory);
  typed_message->~PotConfigRequestJetson();
}

size_t size_function__PotConfigRequestJetson__min_voltages(const void * untyped_member)
{
  (void)untyped_member;
  return 4;
}

const void * get_const_function__PotConfigRequestJetson__min_voltages(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 4> *>(untyped_member);
  return &member[index];
}

void * get_function__PotConfigRequestJetson__min_voltages(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 4> *>(untyped_member);
  return &member[index];
}

size_t size_function__PotConfigRequestJetson__max_voltages(const void * untyped_member)
{
  (void)untyped_member;
  return 4;
}

const void * get_const_function__PotConfigRequestJetson__max_voltages(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 4> *>(untyped_member);
  return &member[index];
}

void * get_function__PotConfigRequestJetson__max_voltages(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 4> *>(untyped_member);
  return &member[index];
}

size_t size_function__PotConfigRequestJetson__min_angles(const void * untyped_member)
{
  (void)untyped_member;
  return 4;
}

const void * get_const_function__PotConfigRequestJetson__min_angles(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 4> *>(untyped_member);
  return &member[index];
}

void * get_function__PotConfigRequestJetson__min_angles(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 4> *>(untyped_member);
  return &member[index];
}

size_t size_function__PotConfigRequestJetson__max_angles(const void * untyped_member)
{
  (void)untyped_member;
  return 4;
}

const void * get_const_function__PotConfigRequestJetson__max_angles(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 4> *>(untyped_member);
  return &member[index];
}

void * get_function__PotConfigRequestJetson__max_angles(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 4> *>(untyped_member);
  return &member[index];
}

size_t size_function__PotConfigRequestJetson__enabled_channels(const void * untyped_member)
{
  (void)untyped_member;
  return 4;
}

const void * get_const_function__PotConfigRequestJetson__enabled_channels(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<bool, 4> *>(untyped_member);
  return &member[index];
}

void * get_function__PotConfigRequestJetson__enabled_channels(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<bool, 4> *>(untyped_member);
  return &member[index];
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember PotConfigRequestJetson_message_member_array[12] = {
  {
    "destination_id",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::PotConfigRequestJetson, destination_id),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "min_voltages",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    4,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::PotConfigRequestJetson, min_voltages),  // bytes offset in struct
    nullptr,  // default value
    size_function__PotConfigRequestJetson__min_voltages,  // size() function pointer
    get_const_function__PotConfigRequestJetson__min_voltages,  // get_const(index) function pointer
    get_function__PotConfigRequestJetson__min_voltages,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "max_voltages",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    4,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::PotConfigRequestJetson, max_voltages),  // bytes offset in struct
    nullptr,  // default value
    size_function__PotConfigRequestJetson__max_voltages,  // size() function pointer
    get_const_function__PotConfigRequestJetson__max_voltages,  // get_const(index) function pointer
    get_function__PotConfigRequestJetson__max_voltages,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "min_angles",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    4,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::PotConfigRequestJetson, min_angles),  // bytes offset in struct
    nullptr,  // default value
    size_function__PotConfigRequestJetson__min_angles,  // size() function pointer
    get_const_function__PotConfigRequestJetson__min_angles,  // get_const(index) function pointer
    get_function__PotConfigRequestJetson__min_angles,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "max_angles",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    4,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::PotConfigRequestJetson, max_angles),  // bytes offset in struct
    nullptr,  // default value
    size_function__PotConfigRequestJetson__max_angles,  // size() function pointer
    get_const_function__PotConfigRequestJetson__max_angles,  // get_const(index) function pointer
    get_function__PotConfigRequestJetson__max_angles,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "enabled_channels",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    4,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::PotConfigRequestJetson, enabled_channels),  // bytes offset in struct
    nullptr,  // default value
    size_function__PotConfigRequestJetson__enabled_channels,  // size() function pointer
    get_const_function__PotConfigRequestJetson__enabled_channels,  // get_const(index) function pointer
    get_function__PotConfigRequestJetson__enabled_channels,  // get(index) function pointer
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
    offsetof(avionics_interfaces::msg::PotConfigRequestJetson, remote_command),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "set_min_voltages",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::PotConfigRequestJetson, set_min_voltages),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "set_max_voltages",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::PotConfigRequestJetson, set_max_voltages),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "set_min_angles",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::PotConfigRequestJetson, set_min_angles),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "set_max_angles",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::PotConfigRequestJetson, set_max_angles),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "set_channels_status",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avionics_interfaces::msg::PotConfigRequestJetson, set_channels_status),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers PotConfigRequestJetson_message_members = {
  "avionics_interfaces::msg",  // message namespace
  "PotConfigRequestJetson",  // message name
  12,  // number of fields
  sizeof(avionics_interfaces::msg::PotConfigRequestJetson),
  PotConfigRequestJetson_message_member_array,  // message members
  PotConfigRequestJetson_init_function,  // function to initialize message memory (memory has to be allocated)
  PotConfigRequestJetson_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t PotConfigRequestJetson_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &PotConfigRequestJetson_message_members,
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
get_message_type_support_handle<avionics_interfaces::msg::PotConfigRequestJetson>()
{
  return &::avionics_interfaces::msg::rosidl_typesupport_introspection_cpp::PotConfigRequestJetson_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, avionics_interfaces, msg, PotConfigRequestJetson)() {
  return &::avionics_interfaces::msg::rosidl_typesupport_introspection_cpp::PotConfigRequestJetson_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
