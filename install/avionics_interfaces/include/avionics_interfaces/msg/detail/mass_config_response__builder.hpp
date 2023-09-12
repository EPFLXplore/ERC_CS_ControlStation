// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/MassConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_RESPONSE__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_RESPONSE__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/mass_config_response__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_MassConfigResponse_success
{
public:
  explicit Init_MassConfigResponse_success(::avionics_interfaces::msg::MassConfigResponse & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::MassConfigResponse success(::avionics_interfaces::msg::MassConfigResponse::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigResponse msg_;
};

class Init_MassConfigResponse_set_channels_status
{
public:
  explicit Init_MassConfigResponse_set_channels_status(::avionics_interfaces::msg::MassConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MassConfigResponse_success set_channels_status(::avionics_interfaces::msg::MassConfigResponse::_set_channels_status_type arg)
  {
    msg_.set_channels_status = std::move(arg);
    return Init_MassConfigResponse_success(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigResponse msg_;
};

class Init_MassConfigResponse_set_alpha
{
public:
  explicit Init_MassConfigResponse_set_alpha(::avionics_interfaces::msg::MassConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MassConfigResponse_set_channels_status set_alpha(::avionics_interfaces::msg::MassConfigResponse::_set_alpha_type arg)
  {
    msg_.set_alpha = std::move(arg);
    return Init_MassConfigResponse_set_channels_status(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigResponse msg_;
};

class Init_MassConfigResponse_set_scale
{
public:
  explicit Init_MassConfigResponse_set_scale(::avionics_interfaces::msg::MassConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MassConfigResponse_set_alpha set_scale(::avionics_interfaces::msg::MassConfigResponse::_set_scale_type arg)
  {
    msg_.set_scale = std::move(arg);
    return Init_MassConfigResponse_set_alpha(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigResponse msg_;
};

class Init_MassConfigResponse_set_offset
{
public:
  explicit Init_MassConfigResponse_set_offset(::avionics_interfaces::msg::MassConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MassConfigResponse_set_scale set_offset(::avionics_interfaces::msg::MassConfigResponse::_set_offset_type arg)
  {
    msg_.set_offset = std::move(arg);
    return Init_MassConfigResponse_set_scale(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigResponse msg_;
};

class Init_MassConfigResponse_remote_command
{
public:
  explicit Init_MassConfigResponse_remote_command(::avionics_interfaces::msg::MassConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MassConfigResponse_set_offset remote_command(::avionics_interfaces::msg::MassConfigResponse::_remote_command_type arg)
  {
    msg_.remote_command = std::move(arg);
    return Init_MassConfigResponse_set_offset(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigResponse msg_;
};

class Init_MassConfigResponse_enabled_channels
{
public:
  explicit Init_MassConfigResponse_enabled_channels(::avionics_interfaces::msg::MassConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MassConfigResponse_remote_command enabled_channels(::avionics_interfaces::msg::MassConfigResponse::_enabled_channels_type arg)
  {
    msg_.enabled_channels = std::move(arg);
    return Init_MassConfigResponse_remote_command(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigResponse msg_;
};

class Init_MassConfigResponse_alpha
{
public:
  explicit Init_MassConfigResponse_alpha(::avionics_interfaces::msg::MassConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MassConfigResponse_enabled_channels alpha(::avionics_interfaces::msg::MassConfigResponse::_alpha_type arg)
  {
    msg_.alpha = std::move(arg);
    return Init_MassConfigResponse_enabled_channels(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigResponse msg_;
};

class Init_MassConfigResponse_scale
{
public:
  explicit Init_MassConfigResponse_scale(::avionics_interfaces::msg::MassConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MassConfigResponse_alpha scale(::avionics_interfaces::msg::MassConfigResponse::_scale_type arg)
  {
    msg_.scale = std::move(arg);
    return Init_MassConfigResponse_alpha(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigResponse msg_;
};

class Init_MassConfigResponse_offset
{
public:
  explicit Init_MassConfigResponse_offset(::avionics_interfaces::msg::MassConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MassConfigResponse_scale offset(::avionics_interfaces::msg::MassConfigResponse::_offset_type arg)
  {
    msg_.offset = std::move(arg);
    return Init_MassConfigResponse_scale(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigResponse msg_;
};

class Init_MassConfigResponse_id
{
public:
  Init_MassConfigResponse_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MassConfigResponse_offset id(::avionics_interfaces::msg::MassConfigResponse::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_MassConfigResponse_offset(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigResponse msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::MassConfigResponse>()
{
  return avionics_interfaces::msg::builder::Init_MassConfigResponse_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_RESPONSE__BUILDER_HPP_
