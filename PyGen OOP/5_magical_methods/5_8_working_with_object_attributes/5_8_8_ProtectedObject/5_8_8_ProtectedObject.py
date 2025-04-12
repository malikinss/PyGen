'''
TODO:
    We will consider an attribute protected if its name begins with
    an underscore (_).

    For example, _password, __email, and __dict__.

    Implement the ProtectedObject class.

    When creating an instance, the class must accept an arbitrary number of
    named arguments.

    All arguments passed must be set as attributes of the created instance.

    The ProtectedObject class must prohibit getting and changing the values of
    protected attributes of its instances, as well as deleting these
    attributes or creating new ones.

    When attempting to get or change the value of a protected attribute,
    as well as attempting to delete an attribute or create a new one,
    an AttributeError exception must be raised with the text:
        Access to the protected attribute is not possible

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the ProtectedObject class, it can be arbitrary.
'''
from typing import Any


class ProtectedObject:
    """
    A class that protects attributes starting with an underscore.
    """

    ACCESS_ERR = "Access to the protected attribute is not possible"

    def __init__(self, **kwargs: Any) -> None:
        """
        Initialize with arbitrary named attributes.

        Args:
            **kwargs: Named arguments to set as attributes.
        """
        for attr, value in kwargs.items():
            object.__setattr__(self, attr, value)

    def __setattr__(self, attr: str, value: Any) -> None:
        """
        Prevent setting protected attributes.

        Args:
            attr (str): The name of the attribute.
            value (Any): The value to set.

        Raises:
            AttributeError: If the attribute name starts with an underscore.
        """
        if attr.startswith('_'):
            raise AttributeError(self.ACCESS_ERR)
        object.__setattr__(self, attr, value)

    def __getattribute__(self, attr: str) -> Any:
        """
        Prevent accessing protected attributes.

        Args:
            attr (str): The name of the attribute.

        Returns:
            Any: The attribute value if not protected.

        Raises:
            AttributeError: If the attribute name starts with an underscore.
        """
        if attr.startswith('_'):
            raise AttributeError(self.ACCESS_ERR)
        return object.__getattribute__(self, attr)

    def __delattr__(self, attr: str) -> None:
        """
        Prevent deleting protected attributes.

        Args:
            attr (str): The name of the attribute.

        Raises:
            AttributeError: If the attribute name starts with an underscore.
        """
        if attr.startswith('_'):
            raise AttributeError(self.ACCESS_ERR)
        object.__delattr__(self, attr)
