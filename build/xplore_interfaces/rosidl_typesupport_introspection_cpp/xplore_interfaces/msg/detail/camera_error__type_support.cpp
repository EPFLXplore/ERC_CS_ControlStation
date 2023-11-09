// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from xplore_interfaces:msg/CameraError.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "xplore_interfaces/msg/detail/camera_error__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace xplore_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void CameraError_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) xplore_interfaces::msg::CameraError(_init);
}

void CameraError_fini_function(void * message_memory)
{
  auto typed_message = static_cast<xplore_interfaces::msg::CameraError *>(message_memory);
  typed_message->~CameraError();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember CameraError_message_member_array[2] = {
  {
    "index",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(xplore_interfaces::msg::CameraError, index),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "ip_adresse",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(xplore_interfaces::msg::CameraError, ip_adresse),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers CameraError_message_members = {
  "xplore_interfaces::msg",  // message namespace
  "CameraError",  // message name
  2,  // number of fields
  sizeof(xplore_interfaces::msg::CameraError),
  CameraError_message_member_array,  // message members
  CameraError_init_function,  // function to initialize message memory (memory has to be allocated)
  CameraError_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t CameraError_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &CameraError_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace xplore_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<xplore_interfaces::msg::CameraError>()
{
  return &::xplore_interfaces::msg::rosidl_typesupport_introspection_cpp::CameraError_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, xplore_interfaces, msg, CameraError)() {
  return &::xplore_interfaces::msg::rosidl_typesupport_introspection_cpp::CameraError_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
