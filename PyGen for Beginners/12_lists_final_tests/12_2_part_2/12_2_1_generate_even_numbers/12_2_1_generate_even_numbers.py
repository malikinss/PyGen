'''
TODO:
    The input to the program is an even number n, n≥2. Write a program that
    prints a list of even numbers
'''
from typing import List


def generate_even_numbers(n: int) -> List[int]:
    """
    Generates a list of even numbers from 2 up to a given number n.

    Args:
        n (int): The upper limit of the range, must be an even number.

    Returns:
        List[int]: A list containing even numbers from 2 to n (inclusive).
    """
    return list(range(2, n + 1, 2))


# Input the even number n
n = int(input("Enter an even number: "))

# Ensure the input is valid (n should be an even number and n ≥ 2)
if n >= 2 and n % 2 == 0:
    print(generate_even_numbers(n))
else:
    print("Please enter a valid even number greater than or equal to 2.")
