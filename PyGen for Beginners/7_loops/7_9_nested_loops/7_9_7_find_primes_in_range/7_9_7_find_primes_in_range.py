'''
TODO:
    The input to the program is two natural numbers a and b, (a< b).

    Write a program that finds all prime numbers from a to b inclusive.
'''


def find_primes_in_range(a: int, b: int) -> None:
    """
    Finds and prints all prime numbers in the inclusive range [a, b].

    A prime number is a natural number greater than 1 that is not divisible
    by any number other than 1 and itself.

    Args:
    a (int): The start of the range (inclusive).
    b (int): The end of the range (inclusive).
    """
    for cur_num in range(a, b + 1):
        if cur_num == 1:
            continue  # 1 is not a prime number

        # Check if the current number is divisible by any number between 2
        # and cur_num - 1
        for i in range(2, cur_num):
            if cur_num % i == 0:
                break
        else:
            print(cur_num)  # If no divisor is found, it's a prime number


# Input: two natural numbers a and b
a, b = int(input()), int(input())

# Output: all prime numbers in the range [a, b]
find_primes_in_range(a, b)
