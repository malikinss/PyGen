'''
TODO:
    Implement a function is_iterable() that takes one argument:
        obj — an arbitrary object

    The function should return True if obj is an iterable object
    or False otherwise.
'''


def is_iterable(obj: any) -> bool:
    """
    Check if the given object is iterable.

    Args:
        obj (Any): The object to check.

    Returns:
        bool: True if the object is iterable, otherwise False.
    """
    return hasattr(obj, '__iter__')
