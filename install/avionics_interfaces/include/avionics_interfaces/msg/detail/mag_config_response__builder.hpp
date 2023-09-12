// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/MagConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_RESPONSE__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_RESPONSE__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/mag_config_response__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_MagConfigResponse_success
{
public:
  explicit Init_MagConfigResponse_success(::avionics_interfaces::msg::MagConfigResponse & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::MagConfigResponse success(::avionics_interfaces::msg::MagConfigResponse::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigResponse msg_;
};

class Init_MagConfigResponse_set_soft_iron
{
public:
  explicit Init_MagConfigResponse_set_soft_iron(::avionics_interfaces::msg::MagConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MagConfigResponse_success set_soft_iron(::avionics_interfaces::msg::MagConfigResponse::_set_soft_iron_type arg)
  {
    msg_.set_soft_iron = std::move(arg);
    return Init_MagConfigResponse_success(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigResponse msg_;
};

class Init_MagConfigResponse_set_hard_iron
{
public:
  explicit Init_MagConfigResponse_set_hard_iron(::avionics_interfaces::msg::MagConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MagConfigResponse_set_soft_iron set_hard_iron(::avionics_interfaces::msg::MagConfigResponse::_set_hard_iron_type arg)
  {
    msg_.set_hard_iron = std::move(arg);
    return Init_MagConfigResponse_set_soft_iron(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigResponse msg_;
};

class Init_MagConfigResponse_remote_command
{
public:
  explicit Init_MagConfigResponse_remote_command(::avionics_interfaces::msg::MagConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MagConfigResponse_set_hard_iron remote_command(::avionics_interfaces::msg::MagConfigResponse::_remote_command_type arg)
  {
    msg_.remote_command = std::move(arg);
    return Init_MagConfigResponse_set_hard_iron(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigResponse msg_;
};

class Init_MagConfigResponse_soft_iron
{
public:
  explicit Init_MagConfigResponse_soft_iron(::avionics_interfaces::msg::MagConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MagConfigResponse_remote_command soft_iron(::avionics_interfaces::msg::MagConfigResponse::_soft_iron_type arg)
  {
    msg_.soft_iron = std::move(arg);
    return Init_MagConfigResponse_remote_command(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigResponse msg_;
};

class Init_MagConfigResponse_hard_iron
{
public:
  explicit Init_MagConfigResponse_hard_iron(::avionics_interfaces::msg::MagConfigResponse & msg)
  : msg_(msg)
  {}
  Init_MagConfigResponse_soft_iron hard_iron(::avionics_interfaces::msg::MagConfigResponse::_hard_iron_type arg)
  {
    msg_.hard_iron = std::move(arg);
    return Init_MagConfigResponse_soft_iron(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigResponse msg_;
};

class Init_MagConfigResponse_id
{
public:
  Init_MagConfigResponse_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MagConfigResponse_hard_iron id(::avionics_interfaces::msg::MagConfigResponse::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_MagConfigResponse_hard_iron(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigResponse msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::MagConfigResponse>()
{
  return avionics_interfaces::msg::builder::Init_MagConfigResponse_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_RESPONSE__BUILDER_HPP_
