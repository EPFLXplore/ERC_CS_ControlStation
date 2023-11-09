# generated from rosidl_generator_py/resource/_idl.py.em
# with input from avionics_interfaces:msg/ImuCalib.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ImuCalib(type):
    """Metaclass of message 'ImuCalib'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('avionics_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'avionics_interfaces.msg.ImuCalib')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__imu_calib
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__imu_calib
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__imu_calib
            cls._TYPE_SUPPORT = module.type_support_msg__msg__imu_calib
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__imu_calib

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ImuCalib(metaclass=Metaclass_ImuCalib):
    """Message class 'ImuCalib'."""

    __slots__ = [
        '_destination_id',
        '_calib_offset_accel',
        '_calib_offset_gyro',
    ]

    _fields_and_field_types = {
        'destination_id': 'uint16',
        'calib_offset_accel': 'boolean',
        'calib_offset_gyro': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.destination_id = kwargs.get('destination_id', int())
        self.calib_offset_accel = kwargs.get('calib_offset_accel', bool())
        self.calib_offset_gyro = kwargs.get('calib_offset_gyro', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.destination_id != other.destination_id:
            return False
        if self.calib_offset_accel != other.calib_offset_accel:
            return False
        if self.calib_offset_gyro != other.calib_offset_gyro:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def destination_id(self):
        """Message field 'destination_id'."""
        return self._destination_id

    @destination_id.setter
    def destination_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'destination_id' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'destination_id' field must be an unsigned integer in [0, 65535]"
        self._destination_id = value

    @property
    def calib_offset_accel(self):
        """Message field 'calib_offset_accel'."""
        return self._calib_offset_accel

    @calib_offset_accel.setter
    def calib_offset_accel(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'calib_offset_accel' field must be of type 'bool'"
        self._calib_offset_accel = value

    @property
    def calib_offset_gyro(self):
        """Message field 'calib_offset_gyro'."""
        return self._calib_offset_gyro

    @calib_offset_gyro.setter
    def calib_offset_gyro(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'calib_offset_gyro' field must be of type 'bool'"
        self._calib_offset_gyro = value
