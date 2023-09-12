// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/PotConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_RESPONSE__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_RESPONSE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__PotConfigResponse __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__PotConfigResponse __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct PotConfigResponse_
{
  using Type = PotConfigResponse_<ContainerAllocator>;

  explicit PotConfigResponse_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      std::fill<typename std::array<float, 4>::iterator, float>(this->min_voltages.begin(), this->min_voltages.end(), 0.0f);
      std::fill<typename std::array<float, 4>::iterator, float>(this->max_voltages.begin(), this->max_voltages.end(), 0.0f);
      std::fill<typename std::array<float, 4>::iterator, float>(this->min_angles.begin(), this->min_angles.end(), 0.0f);
      std::fill<typename std::array<float, 4>::iterator, float>(this->max_angles.begin(), this->max_angles.end(), 0.0f);
      std::fill<typename std::array<bool, 4>::iterator, bool>(this->enabled_channels.begin(), this->enabled_channels.end(), false);
      this->remote_command = false;
      this->set_min_voltages = false;
      this->set_max_voltages = false;
      this->set_min_angles = false;
      this->set_max_angles = false;
      this->set_channels_status = false;
      this->success = false;
    }
  }

  explicit PotConfigResponse_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : min_voltages(_alloc),
    max_voltages(_alloc),
    min_angles(_alloc),
    max_angles(_alloc),
    enabled_channels(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      std::fill<typename std::array<float, 4>::iterator, float>(this->min_voltages.begin(), this->min_voltages.end(), 0.0f);
      std::fill<typename std::array<float, 4>::iterator, float>(this->max_voltages.begin(), this->max_voltages.end(), 0.0f);
      std::fill<typename std::array<float, 4>::iterator, float>(this->min_angles.begin(), this->min_angles.end(), 0.0f);
      std::fill<typename std::array<float, 4>::iterator, float>(this->max_angles.begin(), this->max_angles.end(), 0.0f);
      std::fill<typename std::array<bool, 4>::iterator, bool>(this->enabled_channels.begin(), this->enabled_channels.end(), false);
      this->remote_command = false;
      this->set_min_voltages = false;
      this->set_max_voltages = false;
      this->set_min_angles = false;
      this->set_max_angles = false;
      this->set_channels_status = false;
      this->success = false;
    }
  }

  // field types and members
  using _id_type =
    uint16_t;
  _id_type id;
  using _min_voltages_type =
    std::array<float, 4>;
  _min_voltages_type min_voltages;
  using _max_voltages_type =
    std::array<float, 4>;
  _max_voltages_type max_voltages;
  using _min_angles_type =
    std::array<float, 4>;
  _min_angles_type min_angles;
  using _max_angles_type =
    std::array<float, 4>;
  _max_angles_type max_angles;
  using _enabled_channels_type =
    std::array<bool, 4>;
  _enabled_channels_type enabled_channels;
  using _remote_command_type =
    bool;
  _remote_command_type remote_command;
  using _set_min_voltages_type =
    bool;
  _set_min_voltages_type set_min_voltages;
  using _set_max_voltages_type =
    bool;
  _set_max_voltages_type set_max_voltages;
  using _set_min_angles_type =
    bool;
  _set_min_angles_type set_min_angles;
  using _set_max_angles_type =
    bool;
  _set_max_angles_type set_max_angles;
  using _set_channels_status_type =
    bool;
  _set_channels_status_type set_channels_status;
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__id(
    const uint16_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__min_voltages(
    const std::array<float, 4> & _arg)
  {
    this->min_voltages = _arg;
    return *this;
  }
  Type & set__max_voltages(
    const std::array<float, 4> & _arg)
  {
    this->max_voltages = _arg;
    return *this;
  }
  Type & set__min_angles(
    const std::array<float, 4> & _arg)
  {
    this->min_angles = _arg;
    return *this;
  }
  Type & set__max_angles(
    const std::array<float, 4> & _arg)
  {
    this->max_angles = _arg;
    return *this;
  }
  Type & set__enabled_channels(
    const std::array<bool, 4> & _arg)
  {
    this->enabled_channels = _arg;
    return *this;
  }
  Type & set__remote_command(
    const bool & _arg)
  {
    this->remote_command = _arg;
    return *this;
  }
  Type & set__set_min_voltages(
    const bool & _arg)
  {
    this->set_min_voltages = _arg;
    return *this;
  }
  Type & set__set_max_voltages(
    const bool & _arg)
  {
    this->set_max_voltages = _arg;
    return *this;
  }
  Type & set__set_min_angles(
    const bool & _arg)
  {
    this->set_min_angles = _arg;
    return *this;
  }
  Type & set__set_max_angles(
    const bool & _arg)
  {
    this->set_max_angles = _arg;
    return *this;
  }
  Type & set__set_channels_status(
    const bool & _arg)
  {
    this->set_channels_status = _arg;
    return *this;
  }
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avionics_interfaces::msg::PotConfigResponse_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::PotConfigResponse_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::PotConfigResponse_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::PotConfigResponse_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::PotConfigResponse_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::PotConfigResponse_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::PotConfigResponse_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::PotConfigResponse_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::PotConfigResponse_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::PotConfigResponse_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__PotConfigResponse
    std::shared_ptr<avionics_interfaces::msg::PotConfigResponse_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__PotConfigResponse
    std::shared_ptr<avionics_interfaces::msg::PotConfigResponse_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PotConfigResponse_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->min_voltages != other.min_voltages) {
      return false;
    }
    if (this->max_voltages != other.max_voltages) {
      return false;
    }
    if (this->min_angles != other.min_angles) {
      return false;
    }
    if (this->max_angles != other.max_angles) {
      return false;
    }
    if (this->enabled_channels != other.enabled_channels) {
      return false;
    }
    if (this->remote_command != other.remote_command) {
      return false;
    }
    if (this->set_min_voltages != other.set_min_voltages) {
      return false;
    }
    if (this->set_max_voltages != other.set_max_voltages) {
      return false;
    }
    if (this->set_min_angles != other.set_min_angles) {
      return false;
    }
    if (this->set_max_angles != other.set_max_angles) {
      return false;
    }
    if (this->set_channels_status != other.set_channels_status) {
      return false;
    }
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const PotConfigResponse_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PotConfigResponse_

// alias to use template instance with default allocator
using PotConfigResponse =
  avionics_interfaces::msg::PotConfigResponse_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_RESPONSE__STRUCT_HPP_
