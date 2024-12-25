'''
TODO:
    The input to the program is a natural number n.

    Write a program that evaluates the value of an expression
    (1 + 1/2 + 1/3 + ... + 1/n) - ln(n)
'''
from math import log


def evaluate_expression(n: int) -> float:
    """
    Evaluates the expression (1 + 1/2 + 1/3 + ... + 1/n) - ln(n).

    Args:
        n (int): The natural number n.

    Returns:
        float: The result of the expression.
    """
    total = 0
    for i in range(1, n + 1):
        total += 1 / i  # type: ignore

    return total - log(n)  # Subtract the natural logarithm of n


# Input data
n = int(input("Enter a natural number n: "))

# Call the function and print the result
result = evaluate_expression(n)
print(result)
