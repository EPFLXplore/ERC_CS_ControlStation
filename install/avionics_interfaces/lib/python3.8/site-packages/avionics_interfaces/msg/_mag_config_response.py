# generated from rosidl_generator_py/resource/_idl.py.em
# with input from avionics_interfaces:msg/MagConfigResponse.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'hard_iron'
# Member 'soft_iron'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MagConfigResponse(type):
    """Metaclass of message 'MagConfigResponse'."""

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
                'avionics_interfaces.msg.MagConfigResponse')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__mag_config_response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__mag_config_response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__mag_config_response
            cls._TYPE_SUPPORT = module.type_support_msg__msg__mag_config_response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__mag_config_response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MagConfigResponse(metaclass=Metaclass_MagConfigResponse):
    """Message class 'MagConfigResponse'."""

    __slots__ = [
        '_id',
        '_hard_iron',
        '_soft_iron',
        '_remote_command',
        '_set_hard_iron',
        '_set_soft_iron',
        '_success',
    ]

    _fields_and_field_types = {
        'id': 'uint16',
        'hard_iron': 'float[3]',
        'soft_iron': 'float[9]',
        'remote_command': 'boolean',
        'set_hard_iron': 'boolean',
        'set_soft_iron': 'boolean',
        'success': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 3),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 9),  # noqa: E501
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
        if 'hard_iron' not in kwargs:
            self.hard_iron = numpy.zeros(3, dtype=numpy.float32)
        else:
            self.hard_iron = numpy.array(kwargs.get('hard_iron'), dtype=numpy.float32)
            assert self.hard_iron.shape == (3, )
        if 'soft_iron' not in kwargs:
            self.soft_iron = numpy.zeros(9, dtype=numpy.float32)
        else:
            self.soft_iron = numpy.array(kwargs.get('soft_iron'), dtype=numpy.float32)
            assert self.soft_iron.shape == (9, )
        self.remote_command = kwargs.get('remote_command', bool())
        self.set_hard_iron = kwargs.get('set_hard_iron', bool())
        self.set_soft_iron = kwargs.get('set_soft_iron', bool())
        self.success = kwargs.get('success', bool())

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
        if all(self.hard_iron != other.hard_iron):
            return False
        if all(self.soft_iron != other.soft_iron):
            return False
        if self.remote_command != other.remote_command:
            return False
        if self.set_hard_iron != other.set_hard_iron:
            return False
        if self.set_soft_iron != other.set_soft_iron:
            return False
        if self.success != other.success:
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
    def hard_iron(self):
        """Message field 'hard_iron'."""
        return self._hard_iron

    @hard_iron.setter
    def hard_iron(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'hard_iron' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 3, \
                "The 'hard_iron' numpy.ndarray() must have a size of 3"
            self._hard_iron = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 3 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'hard_iron' field must be a set or sequence with length 3 and each value of type 'float'"
        self._hard_iron = numpy.array(value, dtype=numpy.float32)

    @property
    def soft_iron(self):
        """Message field 'soft_iron'."""
        return self._soft_iron

    @soft_iron.setter
    def soft_iron(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'soft_iron' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 9, \
                "The 'soft_iron' numpy.ndarray() must have a size of 9"
            self._soft_iron = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 9 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'soft_iron' field must be a set or sequence with length 9 and each value of type 'float'"
        self._soft_iron = numpy.array(value, dtype=numpy.float32)

    @property
    def remote_command(self):
        """Message field 'remote_command'."""
        return self._remote_command

    @remote_command.setter
    def remote_command(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'remote_command' field must be of type 'bool'"
        self._remote_command = value

    @property
    def set_hard_iron(self):
        """Message field 'set_hard_iron'."""
        return self._set_hard_iron

    @set_hard_iron.setter
    def set_hard_iron(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_hard_iron' field must be of type 'bool'"
        self._set_hard_iron = value

    @property
    def set_soft_iron(self):
        """Message field 'set_soft_iron'."""
        return self._set_soft_iron

    @set_soft_iron.setter
    def set_soft_iron(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_soft_iron' field must be of type 'bool'"
        self._set_soft_iron = value

    @property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value
