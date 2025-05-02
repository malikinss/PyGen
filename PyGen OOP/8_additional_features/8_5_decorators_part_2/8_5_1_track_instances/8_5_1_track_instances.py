'''
TODO:
    Implement the @track_instances decorator to decorate the class.

    The decorator must add an instances attribute to the decorated class,
    containing a list of all created instances of this class.

NOTE:
    The instances of the decorated class in the list by the instances
    attribute must be arranged in the order in which they were created.
'''
from functools import wraps
from typing import Any, Type, TypeVar

T = TypeVar("T")


def track_instances(cls: Type[T]) -> Type[T]:
    """
    Decorator to track class instances.

    Args:
        cls: Class to decorate.

    Returns:
        Type[T]: Decorated class with instances attribute.
    """
    cls.instances = []
    original_init = cls.__init__

    @wraps(original_init)
    def new_init(self: T, *args: Any, **kwargs: Any) -> None:
        original_init(self, *args, **kwargs)
        cls.instances.append(self)

    cls.__init__ = new_init
    return cls
