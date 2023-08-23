// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from xplore_interfaces:msg/CameraError.idl
// generated code does not contain a copyright notice

#ifndef XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__BUILDER_HPP_
#define XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__BUILDER_HPP_

#include "xplore_interfaces/msg/detail/camera_error__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace xplore_interfaces
{

namespace msg
{

namespace builder
{

class Init_CameraError_ip_adresse
{
public:
  explicit Init_CameraError_ip_adresse(::xplore_interfaces::msg::CameraError & msg)
  : msg_(msg)
  {}
  ::xplore_interfaces::msg::CameraError ip_adresse(::xplore_interfaces::msg::CameraError::_ip_adresse_type arg)
  {
    msg_.ip_adresse = std::move(arg);
    return std::move(msg_);
  }

private:
  ::xplore_interfaces::msg::CameraError msg_;
};

class Init_CameraError_index
{
public:
  Init_CameraError_index()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CameraError_ip_adresse index(::xplore_interfaces::msg::CameraError::_index_type arg)
  {
    msg_.index = std::move(arg);
    return Init_CameraError_ip_adresse(msg_);
  }

private:
  ::xplore_interfaces::msg::CameraError msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::xplore_interfaces::msg::CameraError>()
{
  return xplore_interfaces::msg::builder::Init_CameraError_index();
}

}  // namespace xplore_interfaces

#endif  // XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__BUILDER_HPP_
