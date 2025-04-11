'''
TODO:
    Implement a @CachedFunction decorator that caches the computed values of
    the decorated function.

    The cache must be accessible via the cache attribute and be a dictionary
    whose key is a tuple of arguments and whose value is the return value of
    the decorated function when called with these arguments.

NOTE:
    For unambiguous caching, it is guaranteed that the decorated function
    accepts only positional arguments.

    Submit a program to the testing system that contains only the required
    @CachedFunction decorator, but not the code that calls it.
'''
from typing import Callable, Any


class CachedFunction:
    """
    A decorator class that caches the return values of a function.
    """

    def __init__(self, func: Callable) -> None:
        """
        Initialize the decorator with the function to be cached.

        Args:
            func (Callable): The function to decorate and cache results for.
        """
        self.cache = {}
        self.func = func

    def __call__(self, *args: Any) -> Any:
        """
        Call the decorated function, caching and returning its result.

        Args:
            *args: Positional arguments to pass to the decorated function.

        Returns:
            Any: The cached or computed return value of the decorated function.
        """
        key = tuple(args)
        if key not in self.cache:
            self.cache[key] = self.func(*args)
        return self.cache[key]
