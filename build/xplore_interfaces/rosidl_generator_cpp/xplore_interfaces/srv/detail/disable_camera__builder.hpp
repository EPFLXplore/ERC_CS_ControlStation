// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from xplore_interfaces:srv/DisableCamera.idl
// generated code does not contain a copyright notice

#ifndef XPLORE_INTERFACES__SRV__DETAIL__DISABLE_CAMERA__BUILDER_HPP_
#define XPLORE_INTERFACES__SRV__DETAIL__DISABLE_CAMERA__BUILDER_HPP_

#include "xplore_interfaces/srv/detail/disable_camera__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace xplore_interfaces
{

namespace srv
{

namespace builder
{

class Init_DisableCamera_Request_index
{
public:
  Init_DisableCamera_Request_index()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::xplore_interfaces::srv::DisableCamera_Request index(::xplore_interfaces::srv::DisableCamera_Request::_index_type arg)
  {
    msg_.index = std::move(arg);
    return std::move(msg_);
  }

private:
  ::xplore_interfaces::srv::DisableCamera_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::xplore_interfaces::srv::DisableCamera_Request>()
{
  return xplore_interfaces::srv::builder::Init_DisableCamera_Request_index();
}

}  // namespace xplore_interfaces


namespace xplore_interfaces
{

namespace srv
{

namespace builder
{

class Init_DisableCamera_Response_success
{
public:
  Init_DisableCamera_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::xplore_interfaces::srv::DisableCamera_Response success(::xplore_interfaces::srv::DisableCamera_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::xplore_interfaces::srv::DisableCamera_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::xplore_interfaces::srv::DisableCamera_Response>()
{
  return xplore_interfaces::srv::builder::Init_DisableCamera_Response_success();
}

}  // namespace xplore_interfaces

#endif  // XPLORE_INTERFACES__SRV__DETAIL__DISABLE_CAMERA__BUILDER_HPP_
