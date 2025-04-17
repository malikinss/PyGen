'''
TODO:
    Implement a function is_context_manager() that takes one argument:
        obj — an arbitrary object

    The function should return True if obj is a context manager,
    or False otherwise.
'''
from typing import Any


def is_context_manager(obj: Any) -> bool:
    """
    Check if an object is a context manager.

    Args:
        obj: Any object to check.

    Returns:
        bool: True if the object has __enter__ and __exit__ methods,
              False otherwise.
    """
    return hasattr(obj, '__enter__') and hasattr(obj, '__exit__')
