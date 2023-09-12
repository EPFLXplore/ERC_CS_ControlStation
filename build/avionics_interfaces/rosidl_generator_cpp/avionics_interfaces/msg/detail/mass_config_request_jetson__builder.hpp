// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/MassConfigRequestJetson.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_REQUEST_JETSON__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_REQUEST_JETSON__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/mass_config_request_jetson__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_MassConfigRequestJetson_set_channels_status
{
public:
  explicit Init_MassConfigRequestJetson_set_channels_status(::avionics_interfaces::msg::MassConfigRequestJetson & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::MassConfigRequestJetson set_channels_status(::avionics_interfaces::msg::MassConfigRequestJetson::_set_channels_status_type arg)
  {
    msg_.set_channels_status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestJetson msg_;
};

class Init_MassConfigRequestJetson_set_alpha
{
public:
  explicit Init_MassConfigRequestJetson_set_alpha(::avionics_interfaces::msg::MassConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_MassConfigRequestJetson_set_channels_status set_alpha(::avionics_interfaces::msg::MassConfigRequestJetson::_set_alpha_type arg)
  {
    msg_.set_alpha = std::move(arg);
    return Init_MassConfigRequestJetson_set_channels_status(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestJetson msg_;
};

class Init_MassConfigRequestJetson_set_scale
{
public:
  explicit Init_MassConfigRequestJetson_set_scale(::avionics_interfaces::msg::MassConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_MassConfigRequestJetson_set_alpha set_scale(::avionics_interfaces::msg::MassConfigRequestJetson::_set_scale_type arg)
  {
    msg_.set_scale = std::move(arg);
    return Init_MassConfigRequestJetson_set_alpha(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestJetson msg_;
};

class Init_MassConfigRequestJetson_set_offset
{
public:
  explicit Init_MassConfigRequestJetson_set_offset(::avionics_interfaces::msg::MassConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_MassConfigRequestJetson_set_scale set_offset(::avionics_interfaces::msg::MassConfigRequestJetson::_set_offset_type arg)
  {
    msg_.set_offset = std::move(arg);
    return Init_MassConfigRequestJetson_set_scale(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestJetson msg_;
};

class Init_MassConfigRequestJetson_remote_command
{
public:
  explicit Init_MassConfigRequestJetson_remote_command(::avionics_interfaces::msg::MassConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_MassConfigRequestJetson_set_offset remote_command(::avionics_interfaces::msg::MassConfigRequestJetson::_remote_command_type arg)
  {
    msg_.remote_command = std::move(arg);
    return Init_MassConfigRequestJetson_set_offset(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestJetson msg_;
};

class Init_MassConfigRequestJetson_enabled_channels
{
public:
  explicit Init_MassConfigRequestJetson_enabled_channels(::avionics_interfaces::msg::MassConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_MassConfigRequestJetson_remote_command enabled_channels(::avionics_interfaces::msg::MassConfigRequestJetson::_enabled_channels_type arg)
  {
    msg_.enabled_channels = std::move(arg);
    return Init_MassConfigRequestJetson_remote_command(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestJetson msg_;
};

class Init_MassConfigRequestJetson_alpha
{
public:
  explicit Init_MassConfigRequestJetson_alpha(::avionics_interfaces::msg::MassConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_MassConfigRequestJetson_enabled_channels alpha(::avionics_interfaces::msg::MassConfigRequestJetson::_alpha_type arg)
  {
    msg_.alpha = std::move(arg);
    return Init_MassConfigRequestJetson_enabled_channels(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestJetson msg_;
};

class Init_MassConfigRequestJetson_scale
{
public:
  explicit Init_MassConfigRequestJetson_scale(::avionics_interfaces::msg::MassConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_MassConfigRequestJetson_alpha scale(::avionics_interfaces::msg::MassConfigRequestJetson::_scale_type arg)
  {
    msg_.scale = std::move(arg);
    return Init_MassConfigRequestJetson_alpha(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestJetson msg_;
};

class Init_MassConfigRequestJetson_offset
{
public:
  explicit Init_MassConfigRequestJetson_offset(::avionics_interfaces::msg::MassConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_MassConfigRequestJetson_scale offset(::avionics_interfaces::msg::MassConfigRequestJetson::_offset_type arg)
  {
    msg_.offset = std::move(arg);
    return Init_MassConfigRequestJetson_scale(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestJetson msg_;
};

class Init_MassConfigRequestJetson_destination_id
{
public:
  Init_MassConfigRequestJetson_destination_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MassConfigRequestJetson_offset destination_id(::avionics_interfaces::msg::MassConfigRequestJetson::_destination_id_type arg)
  {
    msg_.destination_id = std::move(arg);
    return Init_MassConfigRequestJetson_offset(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestJetson msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::MassConfigRequestJetson>()
{
  return avionics_interfaces::msg::builder::Init_MassConfigRequestJetson_destination_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_REQUEST_JETSON__BUILDER_HPP_
