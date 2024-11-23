'''
TODO:
    The input to the program is a text string containing integers.

    Write a program using a list expression that will print the cubes
    of the specified numbers also on the same line.
'''
from typing import List


def generate_cubes(numbers: str) -> List[int]:
    """
    Generates a list of cubes of integers from the input string.

    Args:
        numbers (str): A string of space-separated integers.

    Returns:
        List[int]: A list of cubes of the input integers.
    """
    return [int(i) ** 3 for i in numbers.split()]


def print_cubes() -> None:
    """
    Prompts the user for a string of space-separated integers,
    computes the cubes of these integers, and prints them on the same line.
    """
    s = input("Enter space-separated integers: ")
    cubes = generate_cubes(s)
    print(*cubes)


# Calling the function to print cubes
print_cubes()
