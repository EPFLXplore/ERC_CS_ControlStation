// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/ImuCalib.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__IMU_CALIB__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__IMU_CALIB__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__ImuCalib __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__ImuCalib __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ImuCalib_
{
  using Type = ImuCalib_<ContainerAllocator>;

  explicit ImuCalib_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->destination_id = 0;
      this->calib_offset_accel = false;
      this->calib_offset_gyro = false;
    }
  }

  explicit ImuCalib_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->destination_id = 0;
      this->calib_offset_accel = false;
      this->calib_offset_gyro = false;
    }
  }

  // field types and members
  using _destination_id_type =
    uint16_t;
  _destination_id_type destination_id;
  using _calib_offset_accel_type =
    bool;
  _calib_offset_accel_type calib_offset_accel;
  using _calib_offset_gyro_type =
    bool;
  _calib_offset_gyro_type calib_offset_gyro;

  // setters for named parameter idiom
  Type & set__destination_id(
    const uint16_t & _arg)
  {
    this->destination_id = _arg;
    return *this;
  }
  Type & set__calib_offset_accel(
    const bool & _arg)
  {
    this->calib_offset_accel = _arg;
    return *this;
  }
  Type & set__calib_offset_gyro(
    const bool & _arg)
  {
    this->calib_offset_gyro = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avionics_interfaces::msg::ImuCalib_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::ImuCalib_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::ImuCalib_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::ImuCalib_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::ImuCalib_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::ImuCalib_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::ImuCalib_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::ImuCalib_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::ImuCalib_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::ImuCalib_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__ImuCalib
    std::shared_ptr<avionics_interfaces::msg::ImuCalib_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__ImuCalib
    std::shared_ptr<avionics_interfaces::msg::ImuCalib_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ImuCalib_ & other) const
  {
    if (this->destination_id != other.destination_id) {
      return false;
    }
    if (this->calib_offset_accel != other.calib_offset_accel) {
      return false;
    }
    if (this->calib_offset_gyro != other.calib_offset_gyro) {
      return false;
    }
    return true;
  }
  bool operator!=(const ImuCalib_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ImuCalib_

// alias to use template instance with default allocator
using ImuCalib =
  avionics_interfaces::msg::ImuCalib_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__IMU_CALIB__STRUCT_HPP_
