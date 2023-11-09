// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/NodeStateArray.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__NODE_STATE_ARRAY__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__NODE_STATE_ARRAY__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__NodeStateArray __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__NodeStateArray __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct NodeStateArray_
{
  using Type = NodeStateArray_<ContainerAllocator>;

  explicit NodeStateArray_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit NodeStateArray_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _node_state_type =
    std::vector<bool, typename ContainerAllocator::template rebind<bool>::other>;
  _node_state_type node_state;

  // setters for named parameter idiom
  Type & set__node_state(
    const std::vector<bool, typename ContainerAllocator::template rebind<bool>::other> & _arg)
  {
    this->node_state = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avionics_interfaces::msg::NodeStateArray_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::NodeStateArray_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::NodeStateArray_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::NodeStateArray_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::NodeStateArray_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::NodeStateArray_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::NodeStateArray_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::NodeStateArray_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::NodeStateArray_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::NodeStateArray_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__NodeStateArray
    std::shared_ptr<avionics_interfaces::msg::NodeStateArray_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__NodeStateArray
    std::shared_ptr<avionics_interfaces::msg::NodeStateArray_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const NodeStateArray_ & other) const
  {
    if (this->node_state != other.node_state) {
      return false;
    }
    return true;
  }
  bool operator!=(const NodeStateArray_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct NodeStateArray_

// alias to use template instance with default allocator
using NodeStateArray =
  avionics_interfaces::msg::NodeStateArray_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__NODE_STATE_ARRAY__STRUCT_HPP_
