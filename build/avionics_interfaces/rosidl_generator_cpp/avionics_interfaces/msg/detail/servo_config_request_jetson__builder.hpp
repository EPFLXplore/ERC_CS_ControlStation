// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/ServoConfigRequestJetson.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_REQUEST_JETSON__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_REQUEST_JETSON__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/servo_config_request_jetson__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_ServoConfigRequestJetson_set_max_angles
{
public:
  explicit Init_ServoConfigRequestJetson_set_max_angles(::avionics_interfaces::msg::ServoConfigRequestJetson & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::ServoConfigRequestJetson set_max_angles(::avionics_interfaces::msg::ServoConfigRequestJetson::_set_max_angles_type arg)
  {
    msg_.set_max_angles = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestJetson msg_;
};

class Init_ServoConfigRequestJetson_set_min_angles
{
public:
  explicit Init_ServoConfigRequestJetson_set_min_angles(::avionics_interfaces::msg::ServoConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_ServoConfigRequestJetson_set_max_angles set_min_angles(::avionics_interfaces::msg::ServoConfigRequestJetson::_set_min_angles_type arg)
  {
    msg_.set_min_angles = std::move(arg);
    return Init_ServoConfigRequestJetson_set_max_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestJetson msg_;
};

class Init_ServoConfigRequestJetson_set_max_duty
{
public:
  explicit Init_ServoConfigRequestJetson_set_max_duty(::avionics_interfaces::msg::ServoConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_ServoConfigRequestJetson_set_min_angles set_max_duty(::avionics_interfaces::msg::ServoConfigRequestJetson::_set_max_duty_type arg)
  {
    msg_.set_max_duty = std::move(arg);
    return Init_ServoConfigRequestJetson_set_min_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestJetson msg_;
};

class Init_ServoConfigRequestJetson_set_min_duty
{
public:
  explicit Init_ServoConfigRequestJetson_set_min_duty(::avionics_interfaces::msg::ServoConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_ServoConfigRequestJetson_set_max_duty set_min_duty(::avionics_interfaces::msg::ServoConfigRequestJetson::_set_min_duty_type arg)
  {
    msg_.set_min_duty = std::move(arg);
    return Init_ServoConfigRequestJetson_set_max_duty(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestJetson msg_;
};

class Init_ServoConfigRequestJetson_remote_command
{
public:
  explicit Init_ServoConfigRequestJetson_remote_command(::avionics_interfaces::msg::ServoConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_ServoConfigRequestJetson_set_min_duty remote_command(::avionics_interfaces::msg::ServoConfigRequestJetson::_remote_command_type arg)
  {
    msg_.remote_command = std::move(arg);
    return Init_ServoConfigRequestJetson_set_min_duty(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestJetson msg_;
};

class Init_ServoConfigRequestJetson_max_angles
{
public:
  explicit Init_ServoConfigRequestJetson_max_angles(::avionics_interfaces::msg::ServoConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_ServoConfigRequestJetson_remote_command max_angles(::avionics_interfaces::msg::ServoConfigRequestJetson::_max_angles_type arg)
  {
    msg_.max_angles = std::move(arg);
    return Init_ServoConfigRequestJetson_remote_command(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestJetson msg_;
};

class Init_ServoConfigRequestJetson_min_angles
{
public:
  explicit Init_ServoConfigRequestJetson_min_angles(::avionics_interfaces::msg::ServoConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_ServoConfigRequestJetson_max_angles min_angles(::avionics_interfaces::msg::ServoConfigRequestJetson::_min_angles_type arg)
  {
    msg_.min_angles = std::move(arg);
    return Init_ServoConfigRequestJetson_max_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestJetson msg_;
};

class Init_ServoConfigRequestJetson_max_duty
{
public:
  explicit Init_ServoConfigRequestJetson_max_duty(::avionics_interfaces::msg::ServoConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_ServoConfigRequestJetson_min_angles max_duty(::avionics_interfaces::msg::ServoConfigRequestJetson::_max_duty_type arg)
  {
    msg_.max_duty = std::move(arg);
    return Init_ServoConfigRequestJetson_min_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestJetson msg_;
};

class Init_ServoConfigRequestJetson_min_duty
{
public:
  explicit Init_ServoConfigRequestJetson_min_duty(::avionics_interfaces::msg::ServoConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_ServoConfigRequestJetson_max_duty min_duty(::avionics_interfaces::msg::ServoConfigRequestJetson::_min_duty_type arg)
  {
    msg_.min_duty = std::move(arg);
    return Init_ServoConfigRequestJetson_max_duty(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestJetson msg_;
};

class Init_ServoConfigRequestJetson_destination_id
{
public:
  Init_ServoConfigRequestJetson_destination_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ServoConfigRequestJetson_min_duty destination_id(::avionics_interfaces::msg::ServoConfigRequestJetson::_destination_id_type arg)
  {
    msg_.destination_id = std::move(arg);
    return Init_ServoConfigRequestJetson_min_duty(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestJetson msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::ServoConfigRequestJetson>()
{
  return avionics_interfaces::msg::builder::Init_ServoConfigRequestJetson_destination_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_REQUEST_JETSON__BUILDER_HPP_
