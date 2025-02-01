'''
TODO:
    Write a program that takes a number and a function name and outputs
    the result of applying the function to the given number.

    List of possible functions:
    - square: the function takes a number and returns its square;
    - cube: the function takes a number and returns its cube;
    - root: the function takes a number and returns the square root of
            that number;
    - modulus: the function takes a number and returns its modulus;
    - sine: the function takes a number (in radians) and returns the sine of
            that number.

NOTE:
    Solve the problem without using the conditional operator.
'''
from math import sqrt, fabs, sin
from typing import Callable, Dict, Union


def square(number: int) -> int:
    """
    Returns the square of the given number.

    Args:
        number (int): The number to square.

    Returns:
        int: The square of the number.
    """
    return number ** 2


def cube(number: int) -> int:
    """
    Returns the cube of the given number.

    Args:
        number (int): The number to cube.

    Returns:
        int: The cube of the number.
    """
    return number ** 3


def root(number: int) -> float | str:
    """
    Returns the square root of the given number.

    Args:
        number (int): The number to calculate the square root for.

    Returns:
        float: The square root of the number.
    """
    if number < 0:
        return "Error: Cannot take square root of a negative number"
    return sqrt(number)


def modulus(number: int) -> float:
    """
    Returns the modulus of the given number.

    Args:
        number (int): The number to calculate the modulus for.

    Returns:
        float: The modulus of the number.
    """
    return fabs(number)


def sine(number: float) -> float:
    """
    Returns the sine of the given number (in radians).

    Args:
        number (float): The number to calculate the sine for.

    Returns:
        float: The sine of the number.
    """
    return sin(number)


def do_action(
    actions: Dict[str, Callable[[int], Union[int, float, str]]],
    number: int
) -> None:
    """
    Applies the chosen function to the number and prints the result.

    Args:
        actions (dict): Dictionary mapping function names to functions.
        action (str): The name of the action to perform.
        number (int): The number to which the function will be applied.
    """
    if action in actions:
        result = actions[action](number)
        print(result)
    else:
        print("Invalid function name. Please choose a valid function.")


# Dictionary to map function names to their respective functions
my_actions: Dict[str, Callable[[int], int | float | str]] = {
    'квадрат': square,
    'куб': cube,
    'корень': root,
    'модуль': modulus,
    'синус': sine
}

# Taking user input for the number and action
number = int(input("Enter a number: "))
action = input(
    "Enter the function name (square, cube, sqrt, modulus, sin): "
    ).strip().lower()

do_action(my_actions, number)
