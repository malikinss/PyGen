'''
TODO:
    Write a function is_prime(num) that takes a natural number
    as an argument and returns True if the number is prime and False otherwise.
'''


def is_prime(num):
    """
    Checks if a given number is prime.

    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.

    Args:
        num (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:
        is_prime(5)  # Returns: True
        is_prime(10)  # Returns: False
    """
    lst = [i for i in range(1, num + 1) if num % i == 0]

    if len(lst) == 2:
        return True
    else:
        return False


n = int(input())
print(is_prime(n))
