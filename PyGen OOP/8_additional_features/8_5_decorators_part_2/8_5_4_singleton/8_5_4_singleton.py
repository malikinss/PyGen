'''
TODO:
    Implement the @singleton decorator to decorate the class.

    The decorator should turn the decorated class into a singleton, that is,
    into a class that creates a single instance of itself on the first call
    and returns the same instance on subsequent calls.
'''
from typing import Any, Type, TypeVar

T = TypeVar("T")


class singleton:
    """
    Decorator to make a class a singleton.
    """
    def __init__(self, cls: Type[T]) -> None:
        """
        Init decorator.

        Args:
            cls: Class to decorate.
        """
        self.cls = cls
        self.cls._instance = None

    def __call__(self, *args: Any, **kwargs: Any) -> T:
        """
        Create or return singleton instance.

        Args:
            *args: Positional arguments for __init__.
            **kwargs: Keyword arguments for __init__.

        Returns:
            T: Singleton instance.
        """
        if self.cls._instance is None:
            self.cls._instance = object.__new__(self.cls)
        self.cls.__init__(self.cls._instance, *args, **kwargs)
        return self.cls._instance
