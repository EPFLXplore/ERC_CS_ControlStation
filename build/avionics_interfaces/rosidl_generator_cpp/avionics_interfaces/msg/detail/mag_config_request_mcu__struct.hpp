// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/MagConfigRequestMCU.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_REQUEST_MCU__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_REQUEST_MCU__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__MagConfigRequestMCU __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__MagConfigRequestMCU __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MagConfigRequestMCU_
{
  using Type = MagConfigRequestMCU_<ContainerAllocator>;

  explicit MagConfigRequestMCU_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      this->req_hard_iron = false;
      this->req_soft_iron = false;
    }
  }

  explicit MagConfigRequestMCU_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      this->req_hard_iron = false;
      this->req_soft_iron = false;
    }
  }

  // field types and members
  using _id_type =
    uint16_t;
  _id_type id;
  using _req_hard_iron_type =
    bool;
  _req_hard_iron_type req_hard_iron;
  using _req_soft_iron_type =
    bool;
  _req_soft_iron_type req_soft_iron;

  // setters for named parameter idiom
  Type & set__id(
    const uint16_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__req_hard_iron(
    const bool & _arg)
  {
    this->req_hard_iron = _arg;
    return *this;
  }
  Type & set__req_soft_iron(
    const bool & _arg)
  {
    this->req_soft_iron = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avionics_interfaces::msg::MagConfigRequestMCU_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::MagConfigRequestMCU_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::MagConfigRequestMCU_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::MagConfigRequestMCU_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::MagConfigRequestMCU_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::MagConfigRequestMCU_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::MagConfigRequestMCU_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::MagConfigRequestMCU_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::MagConfigRequestMCU_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::MagConfigRequestMCU_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__MagConfigRequestMCU
    std::shared_ptr<avionics_interfaces::msg::MagConfigRequestMCU_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__MagConfigRequestMCU
    std::shared_ptr<avionics_interfaces::msg::MagConfigRequestMCU_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MagConfigRequestMCU_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->req_hard_iron != other.req_hard_iron) {
      return false;
    }
    if (this->req_soft_iron != other.req_soft_iron) {
      return false;
    }
    return true;
  }
  bool operator!=(const MagConfigRequestMCU_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MagConfigRequestMCU_

// alias to use template instance with default allocator
using MagConfigRequestMCU =
  avionics_interfaces::msg::MagConfigRequestMCU_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_REQUEST_MCU__STRUCT_HPP_
