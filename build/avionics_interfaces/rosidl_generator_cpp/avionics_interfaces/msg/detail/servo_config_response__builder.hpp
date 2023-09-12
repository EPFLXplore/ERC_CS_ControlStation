// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/ServoConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_RESPONSE__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_RESPONSE__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/servo_config_response__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_ServoConfigResponse_success
{
public:
  explicit Init_ServoConfigResponse_success(::avionics_interfaces::msg::ServoConfigResponse & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::ServoConfigResponse success(::avionics_interfaces::msg::ServoConfigResponse::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigResponse msg_;
};

class Init_ServoConfigResponse_set_max_angles
{
public:
  explicit Init_ServoConfigResponse_set_max_angles(::avionics_interfaces::msg::ServoConfigResponse & msg)
  : msg_(msg)
  {}
  Init_ServoConfigResponse_success set_max_angles(::avionics_interfaces::msg::ServoConfigResponse::_set_max_angles_type arg)
  {
    msg_.set_max_angles = std::move(arg);
    return Init_ServoConfigResponse_success(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigResponse msg_;
};

class Init_ServoConfigResponse_set_min_angles
{
public:
  explicit Init_ServoConfigResponse_set_min_angles(::avionics_interfaces::msg::ServoConfigResponse & msg)
  : msg_(msg)
  {}
  Init_ServoConfigResponse_set_max_angles set_min_angles(::avionics_interfaces::msg::ServoConfigResponse::_set_min_angles_type arg)
  {
    msg_.set_min_angles = std::move(arg);
    return Init_ServoConfigResponse_set_max_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigResponse msg_;
};

class Init_ServoConfigResponse_set_max_duty
{
public:
  explicit Init_ServoConfigResponse_set_max_duty(::avionics_interfaces::msg::ServoConfigResponse & msg)
  : msg_(msg)
  {}
  Init_ServoConfigResponse_set_min_angles set_max_duty(::avionics_interfaces::msg::ServoConfigResponse::_set_max_duty_type arg)
  {
    msg_.set_max_duty = std::move(arg);
    return Init_ServoConfigResponse_set_min_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigResponse msg_;
};

class Init_ServoConfigResponse_set_min_duty
{
public:
  explicit Init_ServoConfigResponse_set_min_duty(::avionics_interfaces::msg::ServoConfigResponse & msg)
  : msg_(msg)
  {}
  Init_ServoConfigResponse_set_max_duty set_min_duty(::avionics_interfaces::msg::ServoConfigResponse::_set_min_duty_type arg)
  {
    msg_.set_min_duty = std::move(arg);
    return Init_ServoConfigResponse_set_max_duty(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigResponse msg_;
};

class Init_ServoConfigResponse_remote_command
{
public:
  explicit Init_ServoConfigResponse_remote_command(::avionics_interfaces::msg::ServoConfigResponse & msg)
  : msg_(msg)
  {}
  Init_ServoConfigResponse_set_min_duty remote_command(::avionics_interfaces::msg::ServoConfigResponse::_remote_command_type arg)
  {
    msg_.remote_command = std::move(arg);
    return Init_ServoConfigResponse_set_min_duty(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigResponse msg_;
};

class Init_ServoConfigResponse_max_angles
{
public:
  explicit Init_ServoConfigResponse_max_angles(::avionics_interfaces::msg::ServoConfigResponse & msg)
  : msg_(msg)
  {}
  Init_ServoConfigResponse_remote_command max_angles(::avionics_interfaces::msg::ServoConfigResponse::_max_angles_type arg)
  {
    msg_.max_angles = std::move(arg);
    return Init_ServoConfigResponse_remote_command(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigResponse msg_;
};

class Init_ServoConfigResponse_min_angles
{
public:
  explicit Init_ServoConfigResponse_min_angles(::avionics_interfaces::msg::ServoConfigResponse & msg)
  : msg_(msg)
  {}
  Init_ServoConfigResponse_max_angles min_angles(::avionics_interfaces::msg::ServoConfigResponse::_min_angles_type arg)
  {
    msg_.min_angles = std::move(arg);
    return Init_ServoConfigResponse_max_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigResponse msg_;
};

class Init_ServoConfigResponse_max_duty
{
public:
  explicit Init_ServoConfigResponse_max_duty(::avionics_interfaces::msg::ServoConfigResponse & msg)
  : msg_(msg)
  {}
  Init_ServoConfigResponse_min_angles max_duty(::avionics_interfaces::msg::ServoConfigResponse::_max_duty_type arg)
  {
    msg_.max_duty = std::move(arg);
    return Init_ServoConfigResponse_min_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigResponse msg_;
};

class Init_ServoConfigResponse_min_duty
{
public:
  explicit Init_ServoConfigResponse_min_duty(::avionics_interfaces::msg::ServoConfigResponse & msg)
  : msg_(msg)
  {}
  Init_ServoConfigResponse_max_duty min_duty(::avionics_interfaces::msg::ServoConfigResponse::_min_duty_type arg)
  {
    msg_.min_duty = std::move(arg);
    return Init_ServoConfigResponse_max_duty(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigResponse msg_;
};

class Init_ServoConfigResponse_id
{
public:
  Init_ServoConfigResponse_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ServoConfigResponse_min_duty id(::avionics_interfaces::msg::ServoConfigResponse::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_ServoConfigResponse_min_duty(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigResponse msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::ServoConfigResponse>()
{
  return avionics_interfaces::msg::builder::Init_ServoConfigResponse_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_RESPONSE__BUILDER_HPP_
