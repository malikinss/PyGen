'''
TODO:
    Write a function info_kwargs() that takes an arbitrary number of named
    arguments and prints the named arguments according to the pattern:
        <argument name>: <argument value>
    with the argument names in alphabetical order (ascending).

NOTE:
    Note that the function should take an arbitrary number of named arguments,
    not a list.
'''
from typing import Any


def info_kwargs(**kwargs: Any) -> None:
    """
    Prints the named arguments in alphabetical order.

    Args:
        **kwargs (Any): An arbitrary number of named arguments.

    The output format is:
        <argument name>: <argument value>
    """
    for key, value in sorted(kwargs.items()):
        print(f"{key}: {value}")
