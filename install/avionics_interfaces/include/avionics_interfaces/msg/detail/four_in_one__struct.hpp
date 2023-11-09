// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/FourInOne.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__FOUR_IN_ONE__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__FOUR_IN_ONE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__FourInOne __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__FourInOne __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct FourInOne_
{
  using Type = FourInOne_<ContainerAllocator>;

  explicit FourInOne_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      this->temperature = 0.0f;
      this->moisture = 0.0f;
      this->conductivity = 0.0f;
      this->ph = 0.0f;
    }
  }

  explicit FourInOne_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      this->temperature = 0.0f;
      this->moisture = 0.0f;
      this->conductivity = 0.0f;
      this->ph = 0.0f;
    }
  }

  // field types and members
  using _id_type =
    uint16_t;
  _id_type id;
  using _temperature_type =
    float;
  _temperature_type temperature;
  using _moisture_type =
    float;
  _moisture_type moisture;
  using _conductivity_type =
    float;
  _conductivity_type conductivity;
  using _ph_type =
    float;
  _ph_type ph;

  // setters for named parameter idiom
  Type & set__id(
    const uint16_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__temperature(
    const float & _arg)
  {
    this->temperature = _arg;
    return *this;
  }
  Type & set__moisture(
    const float & _arg)
  {
    this->moisture = _arg;
    return *this;
  }
  Type & set__conductivity(
    const float & _arg)
  {
    this->conductivity = _arg;
    return *this;
  }
  Type & set__ph(
    const float & _arg)
  {
    this->ph = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avionics_interfaces::msg::FourInOne_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::FourInOne_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::FourInOne_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::FourInOne_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::FourInOne_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::FourInOne_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::FourInOne_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::FourInOne_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::FourInOne_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::FourInOne_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__FourInOne
    std::shared_ptr<avionics_interfaces::msg::FourInOne_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__FourInOne
    std::shared_ptr<avionics_interfaces::msg::FourInOne_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FourInOne_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->temperature != other.temperature) {
      return false;
    }
    if (this->moisture != other.moisture) {
      return false;
    }
    if (this->conductivity != other.conductivity) {
      return false;
    }
    if (this->ph != other.ph) {
      return false;
    }
    return true;
  }
  bool operator!=(const FourInOne_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FourInOne_

// alias to use template instance with default allocator
using FourInOne =
  avionics_interfaces::msg::FourInOne_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__FOUR_IN_ONE__STRUCT_HPP_
