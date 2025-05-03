'''
TODO:
    Implement the AttributesMixin class, which adds functionality to classes
    to obtain information about the attributes of their instances.

    The AttributesMixin class must have two instance methods:
        get_public_attributes() — a method that returns a list of names and
                                  values of public attributes of instances of
                                  the class to which the functionality is added
        get_protected_attributes() — a method that returns a list of names and
                                     values of protected attributes of
                                     instances of the class to which
                                     the functionality is added

    The lists returned by the get_public_attributes() and
    get_protected_attributes() methods must have the following format:
        [
            (<attribute name>, <attribute value>),
            (<attribute name>, <attribute value>),
            ...
        ]

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the AttributesMixin class, it can be arbitrary.
'''
from typing import List, Tuple, Any


class AttributesMixin:
    """
    A mixin class for retrieving public and protected instance attributes.
    """
    def get_public_attributes(self) -> List[Tuple[str, Any]]:
        """
        Return a list of public attribute names and values.

        Returns:
            List of tuples with public attribute names and values.
        """
        # Include attributes without leading underscore
        return [
            (k, v)
            for k, v in self.__dict__.items()
            if not k.startswith('_')
        ]

    def get_protected_attributes(self) -> List[Tuple[str, Any]]:
        """
        Return a list of protected attribute names and values.

        Returns:
            List of tuples with protected attribute names and values.
        """
        # Include attributes with single leading underscore, not double
        return [
            (k, v)
            for k, v in self.__dict__.items()
            if k.startswith('_')
            and not k.startswith('__')
            and self.__class__.__name__ not in k
        ]
