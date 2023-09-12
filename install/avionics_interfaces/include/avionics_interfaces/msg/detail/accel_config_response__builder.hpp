// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/AccelConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_RESPONSE__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_RESPONSE__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/accel_config_response__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_AccelConfigResponse_success
{
public:
  explicit Init_AccelConfigResponse_success(::avionics_interfaces::msg::AccelConfigResponse & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::AccelConfigResponse success(::avionics_interfaces::msg::AccelConfigResponse::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigResponse msg_;
};

class Init_AccelConfigResponse_set_transform
{
public:
  explicit Init_AccelConfigResponse_set_transform(::avionics_interfaces::msg::AccelConfigResponse & msg)
  : msg_(msg)
  {}
  Init_AccelConfigResponse_success set_transform(::avionics_interfaces::msg::AccelConfigResponse::_set_transform_type arg)
  {
    msg_.set_transform = std::move(arg);
    return Init_AccelConfigResponse_success(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigResponse msg_;
};

class Init_AccelConfigResponse_set_bias
{
public:
  explicit Init_AccelConfigResponse_set_bias(::avionics_interfaces::msg::AccelConfigResponse & msg)
  : msg_(msg)
  {}
  Init_AccelConfigResponse_set_transform set_bias(::avionics_interfaces::msg::AccelConfigResponse::_set_bias_type arg)
  {
    msg_.set_bias = std::move(arg);
    return Init_AccelConfigResponse_set_transform(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigResponse msg_;
};

class Init_AccelConfigResponse_remote_command
{
public:
  explicit Init_AccelConfigResponse_remote_command(::avionics_interfaces::msg::AccelConfigResponse & msg)
  : msg_(msg)
  {}
  Init_AccelConfigResponse_set_bias remote_command(::avionics_interfaces::msg::AccelConfigResponse::_remote_command_type arg)
  {
    msg_.remote_command = std::move(arg);
    return Init_AccelConfigResponse_set_bias(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigResponse msg_;
};

class Init_AccelConfigResponse_transform
{
public:
  explicit Init_AccelConfigResponse_transform(::avionics_interfaces::msg::AccelConfigResponse & msg)
  : msg_(msg)
  {}
  Init_AccelConfigResponse_remote_command transform(::avionics_interfaces::msg::AccelConfigResponse::_transform_type arg)
  {
    msg_.transform = std::move(arg);
    return Init_AccelConfigResponse_remote_command(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigResponse msg_;
};

class Init_AccelConfigResponse_bias
{
public:
  explicit Init_AccelConfigResponse_bias(::avionics_interfaces::msg::AccelConfigResponse & msg)
  : msg_(msg)
  {}
  Init_AccelConfigResponse_transform bias(::avionics_interfaces::msg::AccelConfigResponse::_bias_type arg)
  {
    msg_.bias = std::move(arg);
    return Init_AccelConfigResponse_transform(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigResponse msg_;
};

class Init_AccelConfigResponse_id
{
public:
  Init_AccelConfigResponse_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AccelConfigResponse_bias id(::avionics_interfaces::msg::AccelConfigResponse::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_AccelConfigResponse_bias(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigResponse msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::AccelConfigResponse>()
{
  return avionics_interfaces::msg::builder::Init_AccelConfigResponse_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_RESPONSE__BUILDER_HPP_
