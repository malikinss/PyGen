'''
TODO:
    A dictionary of class attributes, unlike a dictionary of class instance
    attributes, is a mappingproxy object, not a dict.

    The code below:
        class MyClass:
            pass

        print(type(MyClass.__dict__))
    outputs:
        <class 'mappingproxy'>

    The mappingproxy type is a simplified dictionary.

    It differs from the dict type in having fewer methods, and most
    importantly, in the absence of the magic method __setitem__().

    This means that you cannot directly add a new key-value pair to
    a mappingproxy object, or change the value of an existing key.

    The code below:
        class MyClass:
            pass

        MyClass.__dict__['__doc__'] = 'docstring'

    results in an exception:
        TypeError: 'mappingproxy' object does not support item assignment

    You can use the setattr() function to add the required attribute to
    a class.

    The code below:
        class MyClass:
            pass

        setattr(MyClass, '__doc__', 'docstring')
        print(MyClass.__doc__)

    outputs:
        docstring

    Implement the @add_attr_to_class decorator to decorate the class.

    The decorator should accept an arbitrary number of named arguments and add
    them as attributes to the decorated class.
'''
from typing import Any, Type, TypeVar

T = TypeVar("T")


class add_attr_to_class:
    """
    Decorator to add attributes to a class.
    """
    def __init__(self, **kwargs: Any) -> None:
        """
        Init decorator.

        Args:
            **kwargs: Attributes to add to the class.
        """
        self.attrs = kwargs

    def __call__(self, cls: Type[T]) -> Type[T]:
        """
        Add attributes to the class.

        Args:
            cls: Class to decorate.

        Returns:
            Type[T]: Decorated class.
        """
        for attr, value in self.attrs.items():
            setattr(cls, attr, value)
        return cls
