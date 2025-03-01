'''
TODO:
    It is possible to raise to a power much faster than n multiplications.

    To do this, use the following recurrence relations:
        a^n = (a * a)^(2/n), for even n
        a^n = a * a^(n - 1), for odd n

    Implement the get_fast_pow() function using recursion that takes two
    arguments in the following order:
        - a is a positive integer
        - n is a non-negative integer

    The function should calculate the value of a raised to the power of n
    using the fast exponentiation algorithm and return the result.

NOTE:
    Do not use the exponentiation operator ** when solving.
'''


def get_fast_pow(a: int, n: int) -> int:
    """
    Calculate a raised to the power of n using fast exponentiation.

    Args:
        a (int): The base, a positive integer.
        n (int): The exponent, a non-negative integer.

    Returns:
        int: The result of a raised to the power of n.
    """
    if n == 0:
        return 1

    def recursive_fast_pow(base: int, exponent: int) -> int:
        """
        Recursively calculate base raised to the power of exponent using
        fast exponentiation.

        Args:
            base (int): The base value.
            exponent (int): The exponent value.

        Returns:
            int: The result of base raised to the power of exponent.
        """
        # Base case: when exponent is 0, return 1
        if exponent == 0:
            return 1
        # If exponent is even, apply the first recurrence relation
        elif exponent % 2 == 0:
            return recursive_fast_pow(base * base, exponent // 2)
        # If exponent is odd, apply the second recurrence relation
        else:
            return base * recursive_fast_pow(base, exponent - 1)

    return recursive_fast_pow(a, n)


print(get_fast_pow(5, 3))
