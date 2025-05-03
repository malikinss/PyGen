'''
TODO:
    Implement the @auto_repr decorator to decorate a class.

    The decorator must accept two arguments in the following order:
        args — a list of attribute names
        kwargs — a list of attribute names

    The decorator must implement a formal string representation for instances
    of the class being decorated.

    The string representation must contain the class name and the values of
    the class instance attributes, and must be of the form:
        <class name>(<attribute>, <attribute>, ...)

    If an attribute is specified in the args list, the string representation
    must contain only its value.

    If an attribute is specified in the kwargs list, the string representation
    must contain both its value and its name.

NOTE:
    When decorating a class, it is guaranteed that all required attribute
    names are specified.

    It is also guaranteed that each attribute name appears in exactly one of
    the attribute name lists: either args or kwargs.

    The order of the attributes of an instance of the decorated class in its
    string representation must match their order in the args and kwargs lists.

    In this case, all attributes from the args list must come first, and then
    all attributes from the kwargs list.
'''
from typing import List, Type, TypeVar, Any

T = TypeVar("T")


class auto_repr:
    """
    Decorator to implement __repr__ for class instances.
    """
    def __init__(self, args: List[str], kwargs: List[str]) -> None:
        """
        Init decorator.

        Args:
            args: List of attribute names to display as values.
            kwargs: List of attribute names to display as name=value.
        """
        self.args = args
        self.kwargs = kwargs

    def __call__(self, cls: Type[T]) -> Type[T]:
        """
        Add __repr__ method to the class.

        Args:
            cls: Class to decorate.

        Returns:
            Type[T]: Decorated class.
        """
        def __repr__(instance: Any) -> str:
            arg_values = [
                repr(getattr(instance, arg))
                for arg in self.args
            ]
            kwarg_values = [
                f"{kwarg}={repr(getattr(instance, kwarg))}"
                for kwarg in self.kwargs
            ]
            all_values = arg_values + kwarg_values
            return f"{cls.__name__}({', '.join(all_values)})"

        setattr(cls, "__repr__", __repr__)
        return cls
