'''
TODO:
    The input to the program is a natural number n.

    Write a program that calculates n!.
'''


def factorial(n: int) -> int:
    """
    Calculate the factorial of a given number n.

    Args:
        n (int): The natural number to calculate the factorial of.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1  # 0! is 1 by definition

    factorial_n = 1
    for i in range(1, n + 1):
        factorial_n *= i

    return factorial_n


# Input data
n = int(input("Enter a natural number n: "))

# Validate the input
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Call the function and print the result
    result = factorial(n)
    print(result)
