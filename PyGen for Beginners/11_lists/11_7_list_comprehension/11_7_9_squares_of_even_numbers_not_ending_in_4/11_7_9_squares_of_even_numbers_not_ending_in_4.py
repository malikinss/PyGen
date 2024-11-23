'''
TODO:
    The input to the program is a text string containing integers.

    Write a list expression program that prints the squares of even numbers
    that do not end in 4.
'''
from typing import List


def squares_of_even_numbers_not_ending_in_4(text: str) -> List[int]:
    """
    Returns a list of squares of even numbers that do not end in 4
    from the input string.

    Args:
        text (str): A string containing space-separated integers.

    Returns:
        List[int]: A list of squares of even numbers that do not end in 4.
    """
    return [int(i) ** 2 for i in text.split() if int(i) % 2 == 0 and i[-1] != '4']


def main() -> None:
    """
    Prompts the user for a string of space-separated integers, then prints
    the squares of even numbers that do not end in 4, each on the same line.
    """
    s = input("Enter space-separated integers: ")
    result = squares_of_even_numbers_not_ending_in_4(s)
    print(*result)


# Calling the main function to execute the program
main()
