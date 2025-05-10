'''
TODO:
    A predicate is a function that returns True or False depending on
    the arguments passed.

    Implement the @predicate decorator, which allows you to conveniently
    combine predicates using the &, |, and ~ operators:
        @predicate
        def is_even(num):
        return num % 2 == 0
        @predicate
        def is_positive(num):
        return num > 0
        print((is_even & is_positive)(4))
        # True; equivalent to is_even(4) and is_positive(4)
        print((is_even & is_positive)(3))
        # False; equivalent to is_even(3) and is_positive(3)
        print((is_even | is_positive)(3))
        # True; equivalent to is_even(3) or is_positive(3)
        print((~is_even & is_positive)(3))
        # True; equivalent to not is_even(3) and is_positive(3)

    The decorator should be able to work with any predicate, no matter how
    many arguments it takes:
        @predicate
        def to_be():
        return True
        print((to_be | ~to_be)()) # True; equivalent to to_be() or not to_be()
        @predicate
        def is_equal(a, b):
        return a == b
        @predicate
        def is_less_than(a, b):
        return a < b
        print((is_less_than | is_equal)(1, 2))
        # True; equivalent to is_less_than(1, 2) or is_equal(1, 2)

    Both positional and named arguments should also be supported:
        print((is_less_than | is_equal)(2, b=2))
        # True; equivalent to is_less_than(2, b=2) or is_equal(2, b=2)
        print((is_less_than | is_equal)(a=3, b=2))
        # False; equivalent to is_less_than(a=3, b=2) or is_equal(a=3, b=2)

    The decorated function must be accessible outside combinations with other
    functions and behave like the original function:
        @predicate
        def is_less_than(a, b):
        return a < b
        print(is_less_than(1, 2)) # True
        print(is_less_than(2, 2)) # False
        print(is_less_than(3, 2)) # False

NOTE:
    It is guaranteed that the functions being combined have the same
    signatures.
'''
from typing import Callable
from functools import wraps, update_wrapper


class predicate:
    """
    Decorator for predicates with logical operations.
    """
    def __init__(self, func: Callable[..., bool]) -> None:
        """
        Initialize with predicate function.

        Args:
            func: Function returning bool.
        """
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs) -> bool:
        """
        Call wrapped predicate with arguments.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            Result of predicate function.
        """
        # Call the wrapped function
        return self.func(*args, **kwargs)

    def __and__(self, other: 'predicate') -> 'predicate':
        """
        Create predicate for logical AND.

        Args:
            other: Another predicate.

        Returns:
            New predicate combining self and other with AND.
        """
        @predicate
        @wraps(self.func)
        def combined(*args, **kwargs) -> bool:
            return self.func(*args, **kwargs) and other.func(*args, **kwargs)
        return combined

    def __or__(self, other: 'predicate') -> 'predicate':
        """
        Create predicate for logical OR.

        Args:
            other: Another predicate.

        Returns:
            New predicate combining self and other with OR.
        """
        @predicate
        @wraps(self.func)
        def combined(*args, **kwargs) -> bool:
            return self.func(*args, **kwargs) or other.func(*args, **kwargs)
        return combined

    def __invert__(self) -> 'predicate':
        """
        Create predicate for logical NOT.

        Returns:
            New predicate negating self.
        """
        @predicate
        @wraps(self.func)
        def negated(*args, **kwargs) -> bool:
            return not self.func(*args, **kwargs)
        return negated
