// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/Mag.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MAG__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MAG__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'mag_raw'
// Member 'mag_cal'
#include "sensor_msgs/msg/detail/magnetic_field__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__Mag __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__Mag __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Mag_
{
  using Type = Mag_<ContainerAllocator>;

  explicit Mag_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : mag_raw(_init),
    mag_cal(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
    }
  }

  explicit Mag_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : mag_raw(_alloc, _init),
    mag_cal(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
    }
  }

  // field types and members
  using _id_type =
    uint16_t;
  _id_type id;
  using _mag_raw_type =
    sensor_msgs::msg::MagneticField_<ContainerAllocator>;
  _mag_raw_type mag_raw;
  using _mag_cal_type =
    sensor_msgs::msg::MagneticField_<ContainerAllocator>;
  _mag_cal_type mag_cal;

  // setters for named parameter idiom
  Type & set__id(
    const uint16_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__mag_raw(
    const sensor_msgs::msg::MagneticField_<ContainerAllocator> & _arg)
  {
    this->mag_raw = _arg;
    return *this;
  }
  Type & set__mag_cal(
    const sensor_msgs::msg::MagneticField_<ContainerAllocator> & _arg)
  {
    this->mag_cal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avionics_interfaces::msg::Mag_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::Mag_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::Mag_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::Mag_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::Mag_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::Mag_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::Mag_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::Mag_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::Mag_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::Mag_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__Mag
    std::shared_ptr<avionics_interfaces::msg::Mag_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__Mag
    std::shared_ptr<avionics_interfaces::msg::Mag_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Mag_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->mag_raw != other.mag_raw) {
      return false;
    }
    if (this->mag_cal != other.mag_cal) {
      return false;
    }
    return true;
  }
  bool operator!=(const Mag_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Mag_

// alias to use template instance with default allocator
using Mag =
  avionics_interfaces::msg::Mag_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MAG__STRUCT_HPP_
