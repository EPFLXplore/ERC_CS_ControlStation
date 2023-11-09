// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/NodeStateArray.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__NODE_STATE_ARRAY__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__NODE_STATE_ARRAY__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/node_state_array__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_NodeStateArray_node_state
{
public:
  Init_NodeStateArray_node_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::avionics_interfaces::msg::NodeStateArray node_state(::avionics_interfaces::msg::NodeStateArray::_node_state_type arg)
  {
    msg_.node_state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::NodeStateArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::NodeStateArray>()
{
  return avionics_interfaces::msg::builder::Init_NodeStateArray_node_state();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__NODE_STATE_ARRAY__BUILDER_HPP_
