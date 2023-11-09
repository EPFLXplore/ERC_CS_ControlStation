// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/MagConfigRequestMCU.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_REQUEST_MCU__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_REQUEST_MCU__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/mag_config_request_mcu__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_MagConfigRequestMCU_req_soft_iron
{
public:
  explicit Init_MagConfigRequestMCU_req_soft_iron(::avionics_interfaces::msg::MagConfigRequestMCU & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::MagConfigRequestMCU req_soft_iron(::avionics_interfaces::msg::MagConfigRequestMCU::_req_soft_iron_type arg)
  {
    msg_.req_soft_iron = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigRequestMCU msg_;
};

class Init_MagConfigRequestMCU_req_hard_iron
{
public:
  explicit Init_MagConfigRequestMCU_req_hard_iron(::avionics_interfaces::msg::MagConfigRequestMCU & msg)
  : msg_(msg)
  {}
  Init_MagConfigRequestMCU_req_soft_iron req_hard_iron(::avionics_interfaces::msg::MagConfigRequestMCU::_req_hard_iron_type arg)
  {
    msg_.req_hard_iron = std::move(arg);
    return Init_MagConfigRequestMCU_req_soft_iron(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigRequestMCU msg_;
};

class Init_MagConfigRequestMCU_id
{
public:
  Init_MagConfigRequestMCU_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MagConfigRequestMCU_req_hard_iron id(::avionics_interfaces::msg::MagConfigRequestMCU::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_MagConfigRequestMCU_req_hard_iron(msg_);
  }

private:
  ::avionics_interfaces::msg::MagConfigRequestMCU msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::MagConfigRequestMCU>()
{
  return avionics_interfaces::msg::builder::Init_MagConfigRequestMCU_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_REQUEST_MCU__BUILDER_HPP_
