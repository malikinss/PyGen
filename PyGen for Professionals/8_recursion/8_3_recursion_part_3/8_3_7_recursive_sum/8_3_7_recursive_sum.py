'''
TODO:
    Implement a recursive_sum() function using recursion that takes two
    arguments in the following order:
        - a is a non-negative integer
        - b is a non-negative integer

    The function should return the sum of a and b. When calculating the sum,
    the function:
        - should not use loops
        - should use only +1 and -1 of all arithmetic operations
'''


def recursive_sum(a: int, b: int) -> int:
    """
    Calculate the sum of two non-negative integers using recursion.

    Args:
        a (int): The first non-negative integer.
        b (int): The second non-negative integer.

    Returns:
        int: The sum of the two integers.
    """
    if a == 0:
        return b  # If 'a' is 0, return 'b' as the sum.
    elif b == 0:
        return a  # If 'b' is 0, return 'a' as the sum.

    # Recurse by decreasing 'a' and increasing 'b'.
    return recursive_sum(a - 1, b + 1)
