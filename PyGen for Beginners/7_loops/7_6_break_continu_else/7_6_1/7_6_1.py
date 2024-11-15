'''
TODO:
    The number n>1 is given as input to the program.

    Write a program that prints its smallest divisor other than 1.
'''


def smallest_divisor(n: int) -> int:
    """
    Finds the smallest divisor of a number greater than 1, other than 1.

    Args:
        n (int): The input natural number (n > 1).

    Returns:
        int: The smallest divisor of n other than 1.
    """
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            break
        divisor += 1
    return divisor


# Example usage:
n = int(input("Enter a number greater than 1: "))
print(smallest_divisor(n))
