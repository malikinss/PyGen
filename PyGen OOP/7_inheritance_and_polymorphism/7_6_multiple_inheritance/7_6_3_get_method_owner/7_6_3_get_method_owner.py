'''
TODO:
    Implement a get_method_owner() function that takes two arguments in
    the following order:
        cls — an arbitrary class
        method — a string name of the method

    The function should return the class from which the class cls inherits
    the method method.

    If the method method does not exist in the class itself or in any other
    class in its hierarchy, the get_method_owner() function should return None.
'''


from typing import Union


def get_method_owner(cls: type, method: str) -> Union[type, None]:
    """
    Find the class in cls's hierarchy that defines the method.

    Args:
        cls: The class to start the search from.
        method: The name of the method to find.

    Returns:
        type | None: The class defining the method, or None if not found.
    """
    for klass in cls.__mro__:
        if method in klass.__dict__:
            return klass
    return None
