// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/GyroConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_RESPONSE__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_RESPONSE__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/gyro_config_response__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_GyroConfigResponse_success
{
public:
  explicit Init_GyroConfigResponse_success(::avionics_interfaces::msg::GyroConfigResponse & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::GyroConfigResponse success(::avionics_interfaces::msg::GyroConfigResponse::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::GyroConfigResponse msg_;
};

class Init_GyroConfigResponse_set_bias
{
public:
  explicit Init_GyroConfigResponse_set_bias(::avionics_interfaces::msg::GyroConfigResponse & msg)
  : msg_(msg)
  {}
  Init_GyroConfigResponse_success set_bias(::avionics_interfaces::msg::GyroConfigResponse::_set_bias_type arg)
  {
    msg_.set_bias = std::move(arg);
    return Init_GyroConfigResponse_success(msg_);
  }

private:
  ::avionics_interfaces::msg::GyroConfigResponse msg_;
};

class Init_GyroConfigResponse_remote_command
{
public:
  explicit Init_GyroConfigResponse_remote_command(::avionics_interfaces::msg::GyroConfigResponse & msg)
  : msg_(msg)
  {}
  Init_GyroConfigResponse_set_bias remote_command(::avionics_interfaces::msg::GyroConfigResponse::_remote_command_type arg)
  {
    msg_.remote_command = std::move(arg);
    return Init_GyroConfigResponse_set_bias(msg_);
  }

private:
  ::avionics_interfaces::msg::GyroConfigResponse msg_;
};

class Init_GyroConfigResponse_bias
{
public:
  explicit Init_GyroConfigResponse_bias(::avionics_interfaces::msg::GyroConfigResponse & msg)
  : msg_(msg)
  {}
  Init_GyroConfigResponse_remote_command bias(::avionics_interfaces::msg::GyroConfigResponse::_bias_type arg)
  {
    msg_.bias = std::move(arg);
    return Init_GyroConfigResponse_remote_command(msg_);
  }

private:
  ::avionics_interfaces::msg::GyroConfigResponse msg_;
};

class Init_GyroConfigResponse_id
{
public:
  Init_GyroConfigResponse_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GyroConfigResponse_bias id(::avionics_interfaces::msg::GyroConfigResponse::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_GyroConfigResponse_bias(msg_);
  }

private:
  ::avionics_interfaces::msg::GyroConfigResponse msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::GyroConfigResponse>()
{
  return avionics_interfaces::msg::builder::Init_GyroConfigResponse_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_RESPONSE__BUILDER_HPP_
