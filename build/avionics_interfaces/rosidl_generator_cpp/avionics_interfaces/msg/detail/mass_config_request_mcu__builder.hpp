// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/MassConfigRequestMCU.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_REQUEST_MCU__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_REQUEST_MCU__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/mass_config_request_mcu__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_MassConfigRequestMCU_req_channels_status
{
public:
  explicit Init_MassConfigRequestMCU_req_channels_status(::avionics_interfaces::msg::MassConfigRequestMCU & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::MassConfigRequestMCU req_channels_status(::avionics_interfaces::msg::MassConfigRequestMCU::_req_channels_status_type arg)
  {
    msg_.req_channels_status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestMCU msg_;
};

class Init_MassConfigRequestMCU_req_alpha
{
public:
  explicit Init_MassConfigRequestMCU_req_alpha(::avionics_interfaces::msg::MassConfigRequestMCU & msg)
  : msg_(msg)
  {}
  Init_MassConfigRequestMCU_req_channels_status req_alpha(::avionics_interfaces::msg::MassConfigRequestMCU::_req_alpha_type arg)
  {
    msg_.req_alpha = std::move(arg);
    return Init_MassConfigRequestMCU_req_channels_status(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestMCU msg_;
};

class Init_MassConfigRequestMCU_req_scale
{
public:
  explicit Init_MassConfigRequestMCU_req_scale(::avionics_interfaces::msg::MassConfigRequestMCU & msg)
  : msg_(msg)
  {}
  Init_MassConfigRequestMCU_req_alpha req_scale(::avionics_interfaces::msg::MassConfigRequestMCU::_req_scale_type arg)
  {
    msg_.req_scale = std::move(arg);
    return Init_MassConfigRequestMCU_req_alpha(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestMCU msg_;
};

class Init_MassConfigRequestMCU_req_offset
{
public:
  explicit Init_MassConfigRequestMCU_req_offset(::avionics_interfaces::msg::MassConfigRequestMCU & msg)
  : msg_(msg)
  {}
  Init_MassConfigRequestMCU_req_scale req_offset(::avionics_interfaces::msg::MassConfigRequestMCU::_req_offset_type arg)
  {
    msg_.req_offset = std::move(arg);
    return Init_MassConfigRequestMCU_req_scale(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestMCU msg_;
};

class Init_MassConfigRequestMCU_id
{
public:
  Init_MassConfigRequestMCU_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MassConfigRequestMCU_req_offset id(::avionics_interfaces::msg::MassConfigRequestMCU::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_MassConfigRequestMCU_req_offset(msg_);
  }

private:
  ::avionics_interfaces::msg::MassConfigRequestMCU msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::MassConfigRequestMCU>()
{
  return avionics_interfaces::msg::builder::Init_MassConfigRequestMCU_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_REQUEST_MCU__BUILDER_HPP_
