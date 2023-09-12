# generated from rosidl_generator_py/resource/_idl.py.em
# with input from avionics_interfaces:msg/MassCalibScale.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MassCalibScale(type):
    """Metaclass of message 'MassCalibScale'."""

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
                'avionics_interfaces.msg.MassCalibScale')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__mass_calib_scale
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__mass_calib_scale
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__mass_calib_scale
            cls._TYPE_SUPPORT = module.type_support_msg__msg__mass_calib_scale
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__mass_calib_scale

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MassCalibScale(metaclass=Metaclass_MassCalibScale):
    """Message class 'MassCalibScale'."""

    __slots__ = [
        '_destination_id',
        '_channel',
        '_expected_weight',
    ]

    _fields_and_field_types = {
        'destination_id': 'uint16',
        'channel': 'uint8',
        'expected_weight': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.destination_id = kwargs.get('destination_id', int())
        self.channel = kwargs.get('channel', int())
        self.expected_weight = kwargs.get('expected_weight', float())

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
        if self.channel != other.channel:
            return False
        if self.expected_weight != other.expected_weight:
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
    def channel(self):
        """Message field 'channel'."""
        return self._channel

    @channel.setter
    def channel(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'channel' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'channel' field must be an unsigned integer in [0, 255]"
        self._channel = value

    @property
    def expected_weight(self):
        """Message field 'expected_weight'."""
        return self._expected_weight

    @expected_weight.setter
    def expected_weight(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'expected_weight' field must be of type 'float'"
        self._expected_weight = value
