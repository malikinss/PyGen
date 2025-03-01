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
    # If n is even, use (a * a)^(n // 2)
    elif n % 2 == 0:
        half_pow = get_fast_pow(a, n // 2)
        return half_pow * half_pow
    # If n is odd, use a * a^(n - 1)
    else:
        return a * get_fast_pow(a, n - 1)


# Test the function
print(get_fast_pow(5, 3))  # Output should be 125
