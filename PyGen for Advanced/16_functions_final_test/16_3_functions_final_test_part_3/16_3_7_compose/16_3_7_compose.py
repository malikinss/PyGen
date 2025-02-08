'''
TODO:
    Write a function compose() that takes two other one-argument functions f
    and g as input and returns a new function.

    This new function should also take a single argument x and apply
    the original functions to it in the correct order: for functions f and g,
    the order of application should be f(g(x)).

NOTE:
    From a mathematical point of view, the composition of functions f and g is
    a new function h(x) = f(g(x)), and the order of applying the functions f
    and g is important!
'''
from typing import Callable, Any


def compose(
    func1: Callable[[Any], Any], func2: Callable[[Any], Any]
) -> Callable[[Any], Any]:
    """
    Returns a new function that applies func1 to the result of applying func2.

    Given two functions f and g, the new function h will behave as
    h(x) = f(g(x)).

    Parameters:
    - func1 (Callable[[Any], Any]): The first function to apply.
    - func2 (Callable[[Any], Any]): The second function to apply.

    Returns:
    - Callable[[Any], Any]: A new function that applies func2 to its input,
      then applies func1 to the result.
    """
    return lambda x: func1(func2(x))
