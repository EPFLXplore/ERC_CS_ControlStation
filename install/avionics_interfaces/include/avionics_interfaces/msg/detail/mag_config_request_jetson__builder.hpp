// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/MagConfigRequestJetson.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_REQUEST_JETSON__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_REQUEST_JETSON__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/mag_config_request_jetson__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_MagConfigRequestJetson_set_soft_iron
{
public:
  explicit Init_MagConfigRequestJetson_set_soft_iron(::avionics_interfaces::msg::MagConfigRequestJetson & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::MagConfigRequestJetson set_soft_iron(::avionics_interfaces::msg::MagConfigRequestJetson::_set_soft_iron_type arg)
  {
    msg_.set_soft_iron = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigRequestJetson msg_;
};

class Init_MagConfigRequestJetson_set_hard_iron
{
public:
  explicit Init_MagConfigRequestJetson_set_hard_iron(::avionics_interfaces::msg::MagConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_MagConfigRequestJetson_set_soft_iron set_hard_iron(::avionics_interfaces::msg::MagConfigRequestJetson::_set_hard_iron_type arg)
  {
    msg_.set_hard_iron = std::move(arg);
    return Init_MagConfigRequestJetson_set_soft_iron(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigRequestJetson msg_;
};

class Init_MagConfigRequestJetson_remote_command
{
public:
  explicit Init_MagConfigRequestJetson_remote_command(::avionics_interfaces::msg::MagConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_MagConfigRequestJetson_set_hard_iron remote_command(::avionics_interfaces::msg::MagConfigRequestJetson::_remote_command_type arg)
  {
    msg_.remote_command = std::move(arg);
    return Init_MagConfigRequestJetson_set_hard_iron(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigRequestJetson msg_;
};

class Init_MagConfigRequestJetson_soft_iron
{
public:
  explicit Init_MagConfigRequestJetson_soft_iron(::avionics_interfaces::msg::MagConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_MagConfigRequestJetson_remote_command soft_iron(::avionics_interfaces::msg::MagConfigRequestJetson::_soft_iron_type arg)
  {
    msg_.soft_iron = std::move(arg);
    return Init_MagConfigRequestJetson_remote_command(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigRequestJetson msg_;
};

class Init_MagConfigRequestJetson_hard_iron
{
public:
  explicit Init_MagConfigRequestJetson_hard_iron(::avionics_interfaces::msg::MagConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_MagConfigRequestJetson_soft_iron hard_iron(::avionics_interfaces::msg::MagConfigRequestJetson::_hard_iron_type arg)
  {
    msg_.hard_iron = std::move(arg);
    return Init_MagConfigRequestJetson_soft_iron(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigRequestJetson msg_;
};

class Init_MagConfigRequestJetson_destination_id
{
public:
  Init_MagConfigRequestJetson_destination_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MagConfigRequestJetson_hard_iron destination_id(::avionics_interfaces::msg::MagConfigRequestJetson::_destination_id_type arg)
  {
    msg_.destination_id = std::move(arg);
    return Init_MagConfigRequestJetson_hard_iron(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigRequestJetson msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::MagConfigRequestJetson>()
{
  return avionics_interfaces::msg::builder::Init_MagConfigRequestJetson_destination_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_REQUEST_JETSON__BUILDER_HPP_
