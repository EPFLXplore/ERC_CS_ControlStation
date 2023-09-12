// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/PotConfigRequestJetson.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_REQUEST_JETSON__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_REQUEST_JETSON__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/pot_config_request_jetson__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_PotConfigRequestJetson_set_channels_status
{
public:
  explicit Init_PotConfigRequestJetson_set_channels_status(::avionics_interfaces::msg::PotConfigRequestJetson & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::PotConfigRequestJetson set_channels_status(::avionics_interfaces::msg::PotConfigRequestJetson::_set_channels_status_type arg)
  {
    msg_.set_channels_status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestJetson msg_;
};

class Init_PotConfigRequestJetson_set_max_angles
{
public:
  explicit Init_PotConfigRequestJetson_set_max_angles(::avionics_interfaces::msg::PotConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestJetson_set_channels_status set_max_angles(::avionics_interfaces::msg::PotConfigRequestJetson::_set_max_angles_type arg)
  {
    msg_.set_max_angles = std::move(arg);
    return Init_PotConfigRequestJetson_set_channels_status(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestJetson msg_;
};

class Init_PotConfigRequestJetson_set_min_angles
{
public:
  explicit Init_PotConfigRequestJetson_set_min_angles(::avionics_interfaces::msg::PotConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestJetson_set_max_angles set_min_angles(::avionics_interfaces::msg::PotConfigRequestJetson::_set_min_angles_type arg)
  {
    msg_.set_min_angles = std::move(arg);
    return Init_PotConfigRequestJetson_set_max_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestJetson msg_;
};

class Init_PotConfigRequestJetson_set_max_voltages
{
public:
  explicit Init_PotConfigRequestJetson_set_max_voltages(::avionics_interfaces::msg::PotConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestJetson_set_min_angles set_max_voltages(::avionics_interfaces::msg::PotConfigRequestJetson::_set_max_voltages_type arg)
  {
    msg_.set_max_voltages = std::move(arg);
    return Init_PotConfigRequestJetson_set_min_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestJetson msg_;
};

class Init_PotConfigRequestJetson_set_min_voltages
{
public:
  explicit Init_PotConfigRequestJetson_set_min_voltages(::avionics_interfaces::msg::PotConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestJetson_set_max_voltages set_min_voltages(::avionics_interfaces::msg::PotConfigRequestJetson::_set_min_voltages_type arg)
  {
    msg_.set_min_voltages = std::move(arg);
    return Init_PotConfigRequestJetson_set_max_voltages(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestJetson msg_;
};

class Init_PotConfigRequestJetson_remote_command
{
public:
  explicit Init_PotConfigRequestJetson_remote_command(::avionics_interfaces::msg::PotConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestJetson_set_min_voltages remote_command(::avionics_interfaces::msg::PotConfigRequestJetson::_remote_command_type arg)
  {
    msg_.remote_command = std::move(arg);
    return Init_PotConfigRequestJetson_set_min_voltages(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestJetson msg_;
};

class Init_PotConfigRequestJetson_enabled_channels
{
public:
  explicit Init_PotConfigRequestJetson_enabled_channels(::avionics_interfaces::msg::PotConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestJetson_remote_command enabled_channels(::avionics_interfaces::msg::PotConfigRequestJetson::_enabled_channels_type arg)
  {
    msg_.enabled_channels = std::move(arg);
    return Init_PotConfigRequestJetson_remote_command(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestJetson msg_;
};

class Init_PotConfigRequestJetson_max_angles
{
public:
  explicit Init_PotConfigRequestJetson_max_angles(::avionics_interfaces::msg::PotConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestJetson_enabled_channels max_angles(::avionics_interfaces::msg::PotConfigRequestJetson::_max_angles_type arg)
  {
    msg_.max_angles = std::move(arg);
    return Init_PotConfigRequestJetson_enabled_channels(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestJetson msg_;
};

class Init_PotConfigRequestJetson_min_angles
{
public:
  explicit Init_PotConfigRequestJetson_min_angles(::avionics_interfaces::msg::PotConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestJetson_max_angles min_angles(::avionics_interfaces::msg::PotConfigRequestJetson::_min_angles_type arg)
  {
    msg_.min_angles = std::move(arg);
    return Init_PotConfigRequestJetson_max_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestJetson msg_;
};

class Init_PotConfigRequestJetson_max_voltages
{
public:
  explicit Init_PotConfigRequestJetson_max_voltages(::avionics_interfaces::msg::PotConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestJetson_min_angles max_voltages(::avionics_interfaces::msg::PotConfigRequestJetson::_max_voltages_type arg)
  {
    msg_.max_voltages = std::move(arg);
    return Init_PotConfigRequestJetson_min_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestJetson msg_;
};

class Init_PotConfigRequestJetson_min_voltages
{
public:
  explicit Init_PotConfigRequestJetson_min_voltages(::avionics_interfaces::msg::PotConfigRequestJetson & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestJetson_max_voltages min_voltages(::avionics_interfaces::msg::PotConfigRequestJetson::_min_voltages_type arg)
  {
    msg_.min_voltages = std::move(arg);
    return Init_PotConfigRequestJetson_max_voltages(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestJetson msg_;
};

class Init_PotConfigRequestJetson_destination_id
{
public:
  Init_PotConfigRequestJetson_destination_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PotConfigRequestJetson_min_voltages destination_id(::avionics_interfaces::msg::PotConfigRequestJetson::_destination_id_type arg)
  {
    msg_.destination_id = std::move(arg);
    return Init_PotConfigRequestJetson_min_voltages(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestJetson msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::PotConfigRequestJetson>()
{
  return avionics_interfaces::msg::builder::Init_PotConfigRequestJetson_destination_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_REQUEST_JETSON__BUILDER_HPP_
