// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/PotConfigRequestMCU.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_REQUEST_MCU__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_REQUEST_MCU__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__PotConfigRequestMCU __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__PotConfigRequestMCU __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct PotConfigRequestMCU_
{
  using Type = PotConfigRequestMCU_<ContainerAllocator>;

  explicit PotConfigRequestMCU_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      this->req_min_voltages = false;
      this->req_max_voltages = false;
      this->req_min_angles = false;
      this->req_max_angles = false;
      this->req_channels_status = false;
    }
  }

  explicit PotConfigRequestMCU_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      this->req_min_voltages = false;
      this->req_max_voltages = false;
      this->req_min_angles = false;
      this->req_max_angles = false;
      this->req_channels_status = false;
    }
  }

  // field types and members
  using _id_type =
    uint16_t;
  _id_type id;
  using _req_min_voltages_type =
    bool;
  _req_min_voltages_type req_min_voltages;
  using _req_max_voltages_type =
    bool;
  _req_max_voltages_type req_max_voltages;
  using _req_min_angles_type =
    bool;
  _req_min_angles_type req_min_angles;
  using _req_max_angles_type =
    bool;
  _req_max_angles_type req_max_angles;
  using _req_channels_status_type =
    bool;
  _req_channels_status_type req_channels_status;

  // setters for named parameter idiom
  Type & set__id(
    const uint16_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__req_min_voltages(
    const bool & _arg)
  {
    this->req_min_voltages = _arg;
    return *this;
  }
  Type & set__req_max_voltages(
    const bool & _arg)
  {
    this->req_max_voltages = _arg;
    return *this;
  }
  Type & set__req_min_angles(
    const bool & _arg)
  {
    this->req_min_angles = _arg;
    return *this;
  }
  Type & set__req_max_angles(
    const bool & _arg)
  {
    this->req_max_angles = _arg;
    return *this;
  }
  Type & set__req_channels_status(
    const bool & _arg)
  {
    this->req_channels_status = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avionics_interfaces::msg::PotConfigRequestMCU_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::PotConfigRequestMCU_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::PotConfigRequestMCU_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::PotConfigRequestMCU_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::PotConfigRequestMCU_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::PotConfigRequestMCU_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::PotConfigRequestMCU_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::PotConfigRequestMCU_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::PotConfigRequestMCU_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::PotConfigRequestMCU_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__PotConfigRequestMCU
    std::shared_ptr<avionics_interfaces::msg::PotConfigRequestMCU_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__PotConfigRequestMCU
    std::shared_ptr<avionics_interfaces::msg::PotConfigRequestMCU_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PotConfigRequestMCU_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->req_min_voltages != other.req_min_voltages) {
      return false;
    }
    if (this->req_max_voltages != other.req_max_voltages) {
      return false;
    }
    if (this->req_min_angles != other.req_min_angles) {
      return false;
    }
    if (this->req_max_angles != other.req_max_angles) {
      return false;
    }
    if (this->req_channels_status != other.req_channels_status) {
      return false;
    }
    return true;
  }
  bool operator!=(const PotConfigRequestMCU_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PotConfigRequestMCU_

// alias to use template instance with default allocator
using PotConfigRequestMCU =
  avionics_interfaces::msg::PotConfigRequestMCU_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_REQUEST_MCU__STRUCT_HPP_
