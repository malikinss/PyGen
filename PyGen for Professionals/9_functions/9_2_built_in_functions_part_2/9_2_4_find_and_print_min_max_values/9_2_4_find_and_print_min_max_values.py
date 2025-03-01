'''
TODO:
    Write a program that determines the minimum and maximum values of
    a function on a segment in integer points.

    The program receives a valid function f(x) on the first line, and two
    integers a and b, separated by a space, on the next line, representing
    the boundaries of the segment [a; b].

    The program must determine the minimum and maximum values of the
    function f(x) on the segment [a; b] in integer points and output the
    result in the following format:
    - The min value of the function <function f(x)> on the segment <segment> is <min. value>
    - The max value of the function <function f(x)> on the segment <segment> is <max. value>

NOTE:
    A valid function is an expression that fully complies with the
    Python syntax.
'''
import sys
from typing import List


def get_values(function_expression: str,
               start: int,
               end: int) -> List[int]:
    """
    Calculate the values of a function on a segment.

    Args:
        function_expression (str): The string representing the function.
        start (int): The starting integer value of the segment.
        end (int): The ending integer value of the segment.

    Returns:
        List[int]: A list containing values of the function on the segment.
    """
    try:
        # Evaluate the function expression for each value of x in the range
        return [eval(function_expression) for x in range(start, end + 1)]
    except Exception as e:
        print(f"Error evaluating the function: {e}")
        sys.exit(1)


def calculate_min_max_values(function_expression: str,
                             start: int,
                             end: int) -> List[int]:
    """
    Calculate the minimum and maximum values of a function on a segment.

    Args:
        function_expression (str): The string representing the function.
        start (int): The starting integer value of the segment.
        end (int): The ending integer value of the segment.

    Returns:
        List[int]: A list containing the minimum and maximum values.
    """
    values = get_values(function_expression, start, end)
    return [min(values), max(values)]


def find_and_print_min_max_values() -> None:
    """
    Calculates and prints the minimum and maximum values of a function on
    a given segment.

    Reads the function and segment boundaries from input, evaluates the
    function at each integer point in the segment,
    and prints the minimum and maximum values.

    Args:
        None

    Returns:
        None
    """

    function_expression = input()
    start, end = map(int, input().split())
    titles = ['Минимальное', 'Максимальное']

    results = calculate_min_max_values(function_expression, start, end)

    for i in range(len(results)):
        print(f'{titles[i]} значение функции {function_expression} на отрезке [{start}; {end}] равно {results[i]}')


find_and_print_min_max_values()
