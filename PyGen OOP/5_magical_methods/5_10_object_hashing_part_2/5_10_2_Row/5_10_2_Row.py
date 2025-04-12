'''
TODO:
    Implement a Row class that describes an object containing an arbitrary set
    of attributes.

    When creating an instance, the class must accept an arbitrary number of
    named arguments and set them as attributes of the instance being created.

    The Row class must prohibit setting new attributes to its instances.

    In addition, the class must prohibit changing the values of existing
    attributes, as well as deleting them.

    When attempting to set a new attribute, an AttributeError exception must
    be raised with the text:
        It is not possible to set a new attribute

    When attempting to change the value of an existing attribute,
    an AttributeError exception must be raised with the text:
        It is not possible to change the attribute value

    When attempting to delete an attribute, an AttributeError exception must
    be raised with the text:
        It is not possible to delete an attribute

    An instance of the Row class must have the following formal string
    representation:
        Row(
            <name of the 1st attribute>=<value of the 1st attribute>,
            <name of the 2nd attribute>=<value of the 2nd attribute>,
            ...
        )

    Also, instances of the Row class must support comparison operations
    between themselves using the == and != operators.

    Two instances of the Row class are considered equal if their sets of
    attributes are completely identical, that is, their number, positions,
    names, and corresponding values are the same.

    Finally, when passing an instance of the Row class to the hash() function,
    its hash value must be returned.

    The algorithm for calculating the hash value can be arbitrary, but it must
    take into account all instance attributes, their positions, names,
    and corresponding values

NOTE:
    It is guaranteed that the attribute values of Row instances are hashable
    objects.

    Note that in the formal string representation, the attribute values that
    belong to the str type must be enclosed in apostrophes.

    If the object with which the comparison is performed is invalid,
    the method implementing the comparison operation must return
    the NotImplemented constant.

    There are no restrictions regarding the implementation of the Row class,
    it can be arbitrary.
'''
from typing import Any


class Row:
    """
    A class representing an immutable set of named attributes.

    Attributes are set during initialization and cannot be added, modified,
    or deleted.
    Instances support equality comparison and hashing based on attribute names
    and values.
    """

    def __init__(self, **kwargs: Any) -> None:
        """
        Initialize a Row with arbitrary named attributes.

        Args:
            **kwargs: Named arguments to set as attributes.
        """
        for attr, value in kwargs.items():
            object.__setattr__(self, attr, value)

    def __setattr__(self, attr: str, value: Any) -> None:
        """
        Prevent setting or modifying attributes.

        Args:
            attr: Name of the attribute.
            value: Value to set (ignored).

        Raises:
            AttributeError: If attempting to set a new attribute or modify
                            an existing one.
        """
        if not hasattr(self, attr):
            raise AttributeError("It isn't possible to set a new attribute")
        raise AttributeError("It isn't possible to change the attribute value")

    def __delattr__(self, attr: str) -> None:
        """
        Prevent deleting attributes.

        Args:
            attr: Name of the attribute.

        Raises:
            AttributeError: If attempting to delete an attribute.
        """
        raise AttributeError("It isn't possible to delete an attribute")

    def __repr__(self) -> str:
        """
        Formal string representation of the Row.

        Returns:
            str: String in the format Row(attr1=value1, attr2=value2, ...),
                with string values quoted.
        """
        if not self.__dict__:
            return "Row()"
        attrs = [
            f"{attr}='{v}'" if isinstance(v, str) else f"{attr}={v}"
            for attr, v in self.__dict__.items()
        ]
        return f"Row({', '.join(attrs)})"

    def __eq__(self, other: Any) -> bool:
        """
        Check equality with another object.

        Args:
            other: Object to compare with.

        Returns:
            bool: True if other is a Row with identical attributes
                  (names, values, order); False otherwise.
                  Returns NotImplemented if other is not a Row.
        """
        if not isinstance(other, Row):
            return NotImplemented
        return tuple(self.__dict__.items()) == tuple(other.__dict__.items())

    def __hash__(self) -> int:
        """
        Compute hash value based on attributes.

        Returns:
            int: Hash of a tuple containing attribute names and values.
        """
        return hash(tuple(self.__dict__.items()))
