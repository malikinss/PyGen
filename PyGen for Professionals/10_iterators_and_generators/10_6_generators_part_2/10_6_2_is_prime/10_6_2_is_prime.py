'''
TODO:
    Implement the is_prime() function using generator expressions that takes
    one argument:
        - number is a natural number

    The function should return True if number is prime, or False otherwise.

NOTE:
    A prime number is a natural number that has exactly two distinct natural
    divisors — one and itself.

    It is convenient to use the all() or any() functions in the problem.
'''


def is_prime(number: int) -> bool:
    """
    Determines if a given number is prime.

    Args:
        number (int): A natural number.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:
        is_prime(7) -> True
        is_prime(10) -> False
    """
    if number < 2:
        return False
    return all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))
