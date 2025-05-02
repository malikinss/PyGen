'''
TODO:
    Implement a @type_check decorator class that takes one argument:
        types — a list whose elements are data types

    The decorator must check that the types of all positional arguments passed
    to the decorated function are fully matched to the types in the types
    list, i.e. the type of the first argument is the first element of
    the types list, the type of the second argument is the second element of
    the types list, and so on.

    If this condition is not met, a TypeError exception must be raised.

    If the number of positional arguments is greater than the number of
    elements in the types list, then the arguments that are not matched must
    not be considered in the check.

    If the number of positional arguments is less than the number of elements
    in the types list, then the types in the types list that are not matched
    must not be considered in the check.

NOTE:
    Remember that the decorator must not consume the return value of
    the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Any, Callable, List, Type


class type_check:
    """
    Decorator to check argument types.
    """
    def __init__(self, types: List[Type[Any]]) -> None:
        """
        Init decorator.

        Args:
            types: List of expected argument types.
        """
        self.types = tuple(types)

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Wrap function to check argument types.

        Args:
            func: Function to decorate.

        Returns:
            Callable: Wrapped function.
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for arg, expected_type in zip(args, self.types):
                if not isinstance(arg, expected_type):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
