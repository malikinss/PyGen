'''
TODO:
    Using anonymous function syntax, implement a recursive function fib()
    that takes one argument:
        n is a natural number

    The function should return the n-th term of the Fibonacci sequence.

NOTE:
    The Fibonacci sequence is a sequence of natural numbers where each
    subsequent number is the sum of the two preceding ones:
        1,1,2,3,5,8,13,21,34,55,89,144,233,...
'''


def fib(n: int) -> int:
    """
    Calculates the n-th term of the Fibonacci sequence using a recursive
    anonymous function.

    The Fibonacci sequence is defined as follows:
    F(1) = 1, F(2) = 1, and for n > 2, F(n) = F(n-1) + F(n-2).

    Args:
        n (int): The position of the desired term in the Fibonacci sequence.
                 It must be a positive integer.

    Returns:
        int: The n-th Fibonacci number.

    Example:
        >>> fib(5)
        5

    Notes:
        This implementation uses a recursive lambda function to compute
        the Fibonacci value.
    """
    return (
        lambda f: f(f, n)
    )(
        lambda f, n: 1 if n <= 2 else f(f, n - 1) + f(f, n - 2)
    )
