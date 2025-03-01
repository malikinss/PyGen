'''
TODO:
    Write a program that takes as input an arbitrary number of lines
    containing valid mathematical expressions and outputs the value
    of the largest of them.

NOTE:
    A valid mathematical expression is one that fully complies with
    Python syntax.
'''
import sys
from typing import List


def read_input() -> List[str]:
    """
    Reads lines from standard input and strips leading/trailing whitespace.

    Returns:
        List[str]: A list of stripped lines.
    """
    return [line.strip() for line in sys.stdin.readlines() if line.strip()]


def find_max_expression_result() -> float:
    """
    Evaluates a list of mathematical expressions and returns the
    maximum result.

    Returns:
        max_result (float): The largest evaluated result from the
        input expressions.
    """
    operations = read_input()
    results = []

    for operation in operations:
        try:
            # Safely evaluate the mathematical expression
            result = eval(operation)
            if isinstance(result, (int, float)):  # Ensure it's a valid number
                results.append(result)
            else:
                print(
                    f"Warning: Expression '{operation}'"
                    f"did not return a valid number.",
                    file=sys.stderr
                )
        except (SyntaxError, NameError, ZeroDivisionError, ValueError) as e:
            print(
                f"Error evaluating expression '{operation}': {e}",
                file=sys.stderr
            )

    return max(results) if results else float('-inf')


print(find_max_expression_result())
