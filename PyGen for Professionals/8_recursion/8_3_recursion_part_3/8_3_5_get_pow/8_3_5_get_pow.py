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

    def recursive_pow(base: int, exponent: int) -> int:
        """
        Recursively calculates the power of a number.

        Args:
            base (int): The base number.
            exponent (int): The current exponent.

        Returns:
            int: The result of base raised to the power of exponent.
        """
        # Base case: when exponent is 0, return 1
        if exponent == 0:
            return 1

        # Recursive case: multiply base with the result of base^(exponent-1)
        return base * recursive_pow(base, exponent - 1)

    return recursive_pow(a, n)


print(get_pow(5, 2))  # Output should be 25
