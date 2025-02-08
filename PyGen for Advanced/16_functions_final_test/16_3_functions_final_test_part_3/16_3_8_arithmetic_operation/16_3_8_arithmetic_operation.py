'''
TODO:
    Write a function arithmetic_operation() that takes a symbol for one of
    the four arithmetic operations (+, -, *, /) and returns a function of
    two arguments for the corresponding operation.

NOTE:
    The operator module can be useful in solving this problem.
'''
from operator import add, sub, mul, truediv
from typing import Callable


def arithmetic_operation(operation: str) -> Callable[[float, float], float]:
    """
    Returns a function that performs the specified arithmetic operation.

    Based on the input operation symbol ('+', '-', '*', '/'), this function
    returns a function that takes two arguments and performs the corresponding
    arithmetic operation.

    Parameters:
    - operation (str): The symbol representing the arithmetic operation.
                        One of '+', '-', '*', '/'.

    Returns:
    - Callable[[float, float], float]: A function that takes two arguments
      and performs the specified operation on them.

    Raises:
    - ValueError: If the operation symbol is not one of '+', '-', '*', or '/'.
    """
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }

    return lambda x, y: operations[operation](x, y)
