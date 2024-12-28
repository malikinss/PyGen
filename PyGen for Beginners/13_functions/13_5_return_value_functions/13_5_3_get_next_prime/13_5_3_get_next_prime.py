'''
TODO:
    Write a function get_next_prime(num) that takes a natural number num
    as an argument and returns the first prime number greater than num

NOTE:
    Use the is_prime() function from the previous task.
'''


def is_prime(num: int) -> bool:
    """
    Checks if a given number is prime.

    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.

    Args:
        num (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_next_prime(num: int) -> int:
    """
    Returns the next prime number greater than the given number.

    Args:
        num (int): The number to find the next prime greater than.

    Returns:
        int: The first prime number greater than the input number.
    """
    num += 1  # Start looking for the next number greater than the given one
    while not is_prime(num):
        num += 1  # Keep incrementing until a prime is found
    return num


n = int(input())
print(get_next_prime(n))
