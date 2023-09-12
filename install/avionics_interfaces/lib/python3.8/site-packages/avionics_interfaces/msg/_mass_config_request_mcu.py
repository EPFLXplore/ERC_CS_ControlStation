# generated from rosidl_generator_py/resource/_idl.py.em
# with input from avionics_interfaces:msg/MassConfigRequestMCU.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MassConfigRequestMCU(type):
    """Metaclass of message 'MassConfigRequestMCU'."""

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
                'avionics_interfaces.msg.MassConfigRequestMCU')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__mass_config_request_mcu
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__mass_config_request_mcu
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__mass_config_request_mcu
            cls._TYPE_SUPPORT = module.type_support_msg__msg__mass_config_request_mcu
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__mass_config_request_mcu

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MassConfigRequestMCU(metaclass=Metaclass_MassConfigRequestMCU):
    """Message class 'MassConfigRequestMCU'."""

    __slots__ = [
        '_id',
        '_req_offset',
        '_req_scale',
        '_req_alpha',
        '_req_channels_status',
    ]

    _fields_and_field_types = {
        'id': 'uint16',
        'req_offset': 'boolean',
        'req_scale': 'boolean',
        'req_alpha': 'boolean',
        'req_channels_status': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.id = kwargs.get('id', int())
        self.req_offset = kwargs.get('req_offset', bool())
        self.req_scale = kwargs.get('req_scale', bool())
        self.req_alpha = kwargs.get('req_alpha', bool())
        self.req_channels_status = kwargs.get('req_channels_status', bool())

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
        if self.id != other.id:
            return False
        if self.req_offset != other.req_offset:
            return False
        if self.req_scale != other.req_scale:
            return False
        if self.req_alpha != other.req_alpha:
            return False
        if self.req_channels_status != other.req_channels_status:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property  # noqa: A003
    def id(self):  # noqa: A003
        """Message field 'id'."""
        return self._id

    @id.setter  # noqa: A003
    def id(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'id' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'id' field must be an unsigned integer in [0, 65535]"
        self._id = value

    @property
    def req_offset(self):
        """Message field 'req_offset'."""
        return self._req_offset

    @req_offset.setter
    def req_offset(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'req_offset' field must be of type 'bool'"
        self._req_offset = value

    @property
    def req_scale(self):
        """Message field 'req_scale'."""
        return self._req_scale

    @req_scale.setter
    def req_scale(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'req_scale' field must be of type 'bool'"
        self._req_scale = value

    @property
    def req_alpha(self):
        """Message field 'req_alpha'."""
        return self._req_alpha

    @req_alpha.setter
    def req_alpha(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'req_alpha' field must be of type 'bool'"
        self._req_alpha = value

    @property
    def req_channels_status(self):
        """Message field 'req_channels_status'."""
        return self._req_channels_status

    @req_channels_status.setter
    def req_channels_status(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'req_channels_status' field must be of type 'bool'"
        self._req_channels_status = value
