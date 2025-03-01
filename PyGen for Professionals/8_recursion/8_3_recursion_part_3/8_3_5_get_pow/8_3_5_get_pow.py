'''
TODO:
    Implement the get_pow() function using recursion that takes two arguments
    in the following order:
        - a is a positive integer
        - n is a non-negative integer

    The function should evaluate a to the power n and return the result.

NOTE:
    When solving, do not use the exponentiation operator **.

    To build a recursive algorithm, use the following recurrence relation:
        a^n = a⋅a^n-1
'''


def get_pow(a: int, n: int) -> int:
    """
    Calculates a to the power of n using recursion.

    Args:
        a (int): The base, a positive integer.
        n (int): The exponent, a non-negative integer.

    Returns:
        int: The result of a raised to the power of n.
    """
    if n == 0:
        return 1

    return a * get_pow(a, n - 1)


# Test the function with an example
print(get_pow(5, 2))  # Output should be 25
