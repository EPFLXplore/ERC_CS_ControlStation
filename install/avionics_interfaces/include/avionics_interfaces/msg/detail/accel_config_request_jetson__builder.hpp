// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/AccelConfigRequestJetson.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_REQUEST_JETSON__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_REQUEST_JETSON__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/accel_config_request_jetson__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_AccelConfigRequestJetson_set_transform
{
public:
  explicit Init_AccelConfigRequestJetson_set_transform(::avionics_interfaces::msg::AccelConfigRequestJetson & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::AccelConfigRequestJetson set_transform(::avionics_interfaces::msg::AccelConfigRequestJetson::_set_transform_type arg)
  {
    msg_.set_transform = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigRequestJetson msg_;
};

class Init_AccelConfigRequestJetson_set_bias
{
public:
  explicit Init_AccelConfigRequestJetson_set_bias(::avionics_interfaces::msg::AccelConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_AccelConfigRequestJetson_set_transform set_bias(::avionics_interfaces::msg::AccelConfigRequestJetson::_set_bias_type arg)
  {
    msg_.set_bias = std::move(arg);
    return Init_AccelConfigRequestJetson_set_transform(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigRequestJetson msg_;
};

class Init_AccelConfigRequestJetson_remote_command
{
public:
  explicit Init_AccelConfigRequestJetson_remote_command(::avionics_interfaces::msg::AccelConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_AccelConfigRequestJetson_set_bias remote_command(::avionics_interfaces::msg::AccelConfigRequestJetson::_remote_command_type arg)
  {
    msg_.remote_command = std::move(arg);
    return Init_AccelConfigRequestJetson_set_bias(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigRequestJetson msg_;
};

class Init_AccelConfigRequestJetson_transform
{
public:
  explicit Init_AccelConfigRequestJetson_transform(::avionics_interfaces::msg::AccelConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_AccelConfigRequestJetson_remote_command transform(::avionics_interfaces::msg::AccelConfigRequestJetson::_transform_type arg)
  {
    msg_.transform = std::move(arg);
    return Init_AccelConfigRequestJetson_remote_command(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigRequestJetson msg_;
};

class Init_AccelConfigRequestJetson_bias
{
public:
  explicit Init_AccelConfigRequestJetson_bias(::avionics_interfaces::msg::AccelConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_AccelConfigRequestJetson_transform bias(::avionics_interfaces::msg::AccelConfigRequestJetson::_bias_type arg)
  {
    msg_.bias = std::move(arg);
    return Init_AccelConfigRequestJetson_transform(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigRequestJetson msg_;
};

class Init_AccelConfigRequestJetson_destination_id
{
public:
  Init_AccelConfigRequestJetson_destination_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AccelConfigRequestJetson_bias destination_id(::avionics_interfaces::msg::AccelConfigRequestJetson::_destination_id_type arg)
  {
    msg_.destination_id = std::move(arg);
    return Init_AccelConfigRequestJetson_bias(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigRequestJetson msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::AccelConfigRequestJetson>()
{
  return avionics_interfaces::msg::builder::Init_AccelConfigRequestJetson_destination_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_REQUEST_JETSON__BUILDER_HPP_
