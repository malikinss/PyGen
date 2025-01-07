'''
TODO:
    The program is given two strings of numbers as input.

    It is necessary to determine whether it is true that all ten numbers
    are used in recording these two strings?
'''


def contains_all_digits(first: str, second: str) -> str:
    """
    Determines if the combination of two strings contains all digits
    from 0 to 9.

    Args:
    first (str): The first string of digits.
    second (str): The second string of digits.

    Returns:
    str: "YES" if all digits 0-9 are present, otherwise "NO".
    """
    return "YES" if set(first + second) >= set('0123456789') else "NO"


# Read input and call the function
first_input = input()
second_input = input()
print(contains_all_digits(first_input, second_input))
