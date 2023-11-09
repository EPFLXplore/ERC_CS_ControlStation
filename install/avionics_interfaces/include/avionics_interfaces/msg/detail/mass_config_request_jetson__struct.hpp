// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/MassConfigRequestJetson.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_REQUEST_JETSON__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_REQUEST_JETSON__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__MassConfigRequestJetson __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__MassConfigRequestJetson __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MassConfigRequestJetson_
{
  using Type = MassConfigRequestJetson_<ContainerAllocator>;

  explicit MassConfigRequestJetson_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->destination_id = 0;
      std::fill<typename std::array<float, 4>::iterator, float>(this->offset.begin(), this->offset.end(), 0.0f);
      std::fill<typename std::array<float, 4>::iterator, float>(this->scale.begin(), this->scale.end(), 0.0f);
      this->alpha = 0.0f;
      std::fill<typename std::array<bool, 4>::iterator, bool>(this->enabled_channels.begin(), this->enabled_channels.end(), false);
      this->remote_command = false;
      this->set_offset = false;
      this->set_scale = false;
      this->set_alpha = false;
      this->set_channels_status = false;
    }
  }

  explicit MassConfigRequestJetson_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : offset(_alloc),
    scale(_alloc),
    enabled_channels(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->destination_id = 0;
      std::fill<typename std::array<float, 4>::iterator, float>(this->offset.begin(), this->offset.end(), 0.0f);
      std::fill<typename std::array<float, 4>::iterator, float>(this->scale.begin(), this->scale.end(), 0.0f);
      this->alpha = 0.0f;
      std::fill<typename std::array<bool, 4>::iterator, bool>(this->enabled_channels.begin(), this->enabled_channels.end(), false);
      this->remote_command = false;
      this->set_offset = false;
      this->set_scale = false;
      this->set_alpha = false;
      this->set_channels_status = false;
    }
  }

  // field types and members
  using _destination_id_type =
    uint16_t;
  _destination_id_type destination_id;
  using _offset_type =
    std::array<float, 4>;
  _offset_type offset;
  using _scale_type =
    std::array<float, 4>;
  _scale_type scale;
  using _alpha_type =
    float;
  _alpha_type alpha;
  using _enabled_channels_type =
    std::array<bool, 4>;
  _enabled_channels_type enabled_channels;
  using _remote_command_type =
    bool;
  _remote_command_type remote_command;
  using _set_offset_type =
    bool;
  _set_offset_type set_offset;
  using _set_scale_type =
    bool;
  _set_scale_type set_scale;
  using _set_alpha_type =
    bool;
  _set_alpha_type set_alpha;
  using _set_channels_status_type =
    bool;
  _set_channels_status_type set_channels_status;

  // setters for named parameter idiom
  Type & set__destination_id(
    const uint16_t & _arg)
  {
    this->destination_id = _arg;
    return *this;
  }
  Type & set__offset(
    const std::array<float, 4> & _arg)
  {
    this->offset = _arg;
    return *this;
  }
  Type & set__scale(
    const std::array<float, 4> & _arg)
  {
    this->scale = _arg;
    return *this;
  }
  Type & set__alpha(
    const float & _arg)
  {
    this->alpha = _arg;
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
  Type & set__set_offset(
    const bool & _arg)
  {
    this->set_offset = _arg;
    return *this;
  }
  Type & set__set_scale(
    const bool & _arg)
  {
    this->set_scale = _arg;
    return *this;
  }
  Type & set__set_alpha(
    const bool & _arg)
  {
    this->set_alpha = _arg;
    return *this;
  }
  Type & set__set_channels_status(
    const bool & _arg)
  {
    this->set_channels_status = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avionics_interfaces::msg::MassConfigRequestJetson_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::MassConfigRequestJetson_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::MassConfigRequestJetson_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::MassConfigRequestJetson_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::MassConfigRequestJetson_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::MassConfigRequestJetson_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::MassConfigRequestJetson_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::MassConfigRequestJetson_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::MassConfigRequestJetson_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::MassConfigRequestJetson_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__MassConfigRequestJetson
    std::shared_ptr<avionics_interfaces::msg::MassConfigRequestJetson_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__MassConfigRequestJetson
    std::shared_ptr<avionics_interfaces::msg::MassConfigRequestJetson_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MassConfigRequestJetson_ & other) const
  {
    if (this->destination_id != other.destination_id) {
      return false;
    }
    if (this->offset != other.offset) {
      return false;
    }
    if (this->scale != other.scale) {
      return false;
    }
    if (this->alpha != other.alpha) {
      return false;
    }
    if (this->enabled_channels != other.enabled_channels) {
      return false;
    }
    if (this->remote_command != other.remote_command) {
      return false;
    }
    if (this->set_offset != other.set_offset) {
      return false;
    }
    if (this->set_scale != other.set_scale) {
      return false;
    }
    if (this->set_alpha != other.set_alpha) {
      return false;
    }
    if (this->set_channels_status != other.set_channels_status) {
      return false;
    }
    return true;
  }
  bool operator!=(const MassConfigRequestJetson_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MassConfigRequestJetson_

// alias to use template instance with default allocator
using MassConfigRequestJetson =
  avionics_interfaces::msg::MassConfigRequestJetson_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_REQUEST_JETSON__STRUCT_HPP_
