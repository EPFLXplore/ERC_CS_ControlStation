// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/GyroConfigRequestJetson.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_REQUEST_JETSON__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_REQUEST_JETSON__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/gyro_config_request_jetson__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_GyroConfigRequestJetson_set_bias
{
public:
  explicit Init_GyroConfigRequestJetson_set_bias(::avionics_interfaces::msg::GyroConfigRequestJetson & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::GyroConfigRequestJetson set_bias(::avionics_interfaces::msg::GyroConfigRequestJetson::_set_bias_type arg)
  {
    msg_.set_bias = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::GyroConfigRequestJetson msg_;
};

class Init_GyroConfigRequestJetson_remote_command
{
public:
  explicit Init_GyroConfigRequestJetson_remote_command(::avionics_interfaces::msg::GyroConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_GyroConfigRequestJetson_set_bias remote_command(::avionics_interfaces::msg::GyroConfigRequestJetson::_remote_command_type arg)
  {
    msg_.remote_command = std::move(arg);
    return Init_GyroConfigRequestJetson_set_bias(msg_);
  }

private:
  ::avionics_interfaces::msg::GyroConfigRequestJetson msg_;
};

class Init_GyroConfigRequestJetson_bias
{
public:
  explicit Init_GyroConfigRequestJetson_bias(::avionics_interfaces::msg::GyroConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_GyroConfigRequestJetson_remote_command bias(::avionics_interfaces::msg::GyroConfigRequestJetson::_bias_type arg)
  {
    msg_.bias = std::move(arg);
    return Init_GyroConfigRequestJetson_remote_command(msg_);
  }

private:
  ::avionics_interfaces::msg::GyroConfigRequestJetson msg_;
};

class Init_GyroConfigRequestJetson_destination_id
{
public:
  Init_GyroConfigRequestJetson_destination_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GyroConfigRequestJetson_bias destination_id(::avionics_interfaces::msg::GyroConfigRequestJetson::_destination_id_type arg)
  {
    msg_.destination_id = std::move(arg);
    return Init_GyroConfigRequestJetson_bias(msg_);
  }

private:
  ::avionics_interfaces::msg::GyroConfigRequestJetson msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::GyroConfigRequestJetson>()
{
  return avionics_interfaces::msg::builder::Init_GyroConfigRequestJetson_destination_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_REQUEST_JETSON__BUILDER_HPP_
