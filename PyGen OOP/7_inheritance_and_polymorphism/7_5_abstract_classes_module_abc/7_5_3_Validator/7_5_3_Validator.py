'''
TODO:
    Implement an abstract Validator class that describes a descriptor that
    checks that the value being set or changed is valid.

    The class must not take any arguments when instantiated.

    The descriptor must be attached to an attribute that has the same name as
    the variable to which the descriptor is assigned.

    When accessing an attribute, the descriptor must return the value of that
    attribute, if it is set.

    If the attribute's value is not set, an AttributeError exception must be
    raised with the text:
        Attribute not found

    When setting or changing the value of an attribute, the descriptor must
    first check for validity using the validate() method.

    The Validator class must have one abstract instance method:
        validate() - an empty method

    Also implement a Number class that inherits from the Validator class and
    describes a descriptor that checks that the value being set or changed
    is a number from a certain range.

    The descriptor must be attached to an attribute that has the same name as
    the variable to which the descriptor is assigned.

    When instantiated, the class must accept two arguments in the following
    order:
        minvalue — the left end of the range, which defaults to None and
                   does not limit the number on the left
        maxvalue — the right end of the range, which defaults to None and
                   does not limit the number on the right

    The Number class must have one instance method:
        validate() — a method that accepts an arbitrary object as an argument
                     and throws an exception if it does not satisfy any
                     conditions.

    If the specified object is not of type int or float, a TypeError exception
    should be raised with the text:
        The value being set must be a number

    If the specified object is a number less than minvalue, a ValueError
    exception should be raised with the text:
        The number being set must be greater than or equal to <minvalue>

    If the specified object is a number greater than maxvalue, a ValueError
    exception should be raised with the text:
        The number being set must be less than or equal to <maxvalue>

    Finally, implement a String class that inherits from Validator, describing
    a descriptor that checks that the value being set or modified is a string
    of a certain length.

    The descriptor should be attached to an attribute that has the same name
    as the variable to which the descriptor is assigned.

    When instantiated, the class must accept three arguments in the following
    order:
        minsize — the minimum word length, defaults to None and does not limit
                  the minimum length
        maxsize — the maximum word length, defaults to None and does not limit
                  the maximum length
        predicate — a predicate function for additional validation, defaults
                    to None and is not used

    The String class must have one instance method:
        validate() — a method that takes an arbitrary object as an argument
                     and throws an exception if it does not satisfy any
                     conditions.

    If the specified object is not of type str, the method must throw
    a TypeError exception with the message:
        The value to be set must be a string

    If the specified object is a string with a length less than minsize,
    a ValueError exception must be raised with the text:
        The len of the string to be set must be greater than or equal to <min>

    If the specified object is a string with a length greater than maxsize,
    a ValueError exception must be raised with the text:
        The length of the string to be set must be less than or equal to <max>

    If the specified object returns False when passed to the predicate()
    function, a ValueError exception must be raised with the text:
        The string to be set does not satisfy additional conditions

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented classes are used only with correct
    data.

    There are no restrictions regarding the implementation of classes,
    it can be arbitrary.
'''
from abc import ABC, abstractmethod
from typing import Any, Optional, Callable


class Validator(ABC):
    """
    Abstract base class for validating descriptor attributes.
    """
    _ATTR_ERR_MSG = 'Attribute not found'

    def __init__(self) -> None:
        """
        Initialize the descriptor.
        """
        self._attr: str = ""

    def __set_name__(self, owner: type, name: str) -> None:
        """
        Set the attribute name for the descriptor.

        Args:
            owner: The owner class.
            name: The attribute name.
        """
        self._attr = name

    def __get__(self, obj: Optional[object], owner: Optional[type]) -> Any:
        """
        Get the attribute value.

        Args:
            obj: Instance of the owner class, or None if accessed via class.
            owner: The owner class.

        Returns:
            The attribute value if set.

        Raises:
            AttributeError: If the attribute is not set, with message:
                                'Attribute not found'.
        """
        if obj is None:
            return self
        if self._attr not in obj.__dict__:
            raise AttributeError(self._ATTR_ERR_MSG)
        return obj.__dict__[self._attr]

    def __set__(self, obj: object, value: Any) -> None:
        """
        Set the attribute value after validation.

        Args:
            obj: Instance of the owner class.
            value: Value to set.

        Raises:
            TypeError: If the value fails type validation.
            ValueError: If the value fails range or other validation.
        """
        self.validate(value)
        obj.__dict__[self._attr] = value

    @abstractmethod
    def validate(self, value: Any) -> None:
        """Validate the value.

        Args:
            value: Value to validate.

        Raises:
            TypeError: If the value type is invalid.
            ValueError: If the value fails other validation.
        """
        pass


class Number(Validator):
    """
    Descriptor for validating numbers within a range.
    """
    _ERR_MSGS = {
        'TYPE': 'The value being set must be a number',
        'VAL': 'The number being set must be {} than or equal to {}'
    }

    def __init__(
        self,
        minvalue: Optional[float] = None,
        maxvalue: Optional[float] = None
    ) -> None:
        """
        Initialize with optional range bounds.

        Args:
            minvalue: Minimum allowed value, or None for no lower bound.
                      Defaults to None.
            maxvalue: Maximum allowed value, or None for no upper bound.
                      Defaults to None.
        """
        super().__init__()
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value: Any) -> None:
        """
        Validate that the value is a number within the specified range.

        Args:
            value: Value to validate.

        Raises:
            TypeError: If value is not an int or float, with message:
                            'The value being set must be a number'.
            ValueError: If value is outside the allowed range,
                        with appropriate message.
        """
        if not isinstance(value, (int, float)):
            raise TypeError(self._ERR_MSGS['TYPE'])
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(
                self._ERR_MSGS['VAL'].format('greater', self.minvalue)
            )
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(
                self._ERR_MSGS['VAL'].format('less', self.maxvalue)
            )


class String(Validator):
    """
    Descriptor for validating strings by length and optional predicate.
    """
    _ERR_MSGS = {
        'TYPE': "The value to be set must be a string",
        'VAL': 'The len of the string to be set must be {} than or equal to {}',
        'PRED': "The string to be set does not satisfy additional conditions"
    }

    def __init__(
        self,
        minsize: Optional[int] = None,
        maxsize: Optional[int] = None,
        predicate: Optional[Callable[[str], bool]] = None
    ) -> None:
        """
        Initialize with optional length bounds and predicate.

        Args:
            minsize: Minimum string length, or None for no lower bound.
                     Defaults to None.
            maxsize: Maximum string length, or None for no upper bound.
                     Defaults to None.
            predicate: Optional function to validate the string, or None.
                       Defaults to None.
        """
        super().__init__()
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value: Any) -> None:
        """
        Validate that the value is a string with valid length and predicate.

        Args:
            value: Value to validate.

        Raises:
            TypeError: If value is not a string, with message:
                        'The value to be set must be a string'.
            ValueError: If string length or predicate validation fails,
            with appropriate message.
        """
        if not isinstance(value, str):
            raise TypeError(self._ERR_MSGS['TYPE'])
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(
                self._ERR_MSGS['VAL'].format('greater', self.minsize)
            )
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                self._ERR_MSGS['VAL'].format('less', self.maxsize)
            )
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(self._ERR_MSGS['PRED'])
