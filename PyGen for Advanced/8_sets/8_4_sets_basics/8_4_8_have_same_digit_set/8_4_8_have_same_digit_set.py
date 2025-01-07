'''
TODO:
    The program is given two strings of numbers as input.

    It is necessary to determine whether it is true that the same sets
    of numbers were used to write these strings?
'''


def have_same_digit_set(first: str, second: str) -> str:
    """
    Determines if two strings consist of the same set of digits.

    Args:
    first (str): The first string of digits.
    second (str): The second string of digits.

    Returns:
    str: "YES" if both strings contain the same set of digits, otherwise "NO".
    """
    return "YES" if set(first) == set(second) else "NO"


# Read input and call the function
first_input = input()
second_input = input()
print(have_same_digit_set(first_input, second_input))
