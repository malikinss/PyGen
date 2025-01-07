'''
TODO:
    The program is given a string consisting of numbers as input.

    It is necessary to determine whether it is true that none of the numbers
    are repeated in its entry?
'''


def has_unique_digits(number_string: str) -> str:
    """
    Determines if all digits in the given string are unique.

    Args:
    number_string (str): String of digits to evaluate.

    Returns:
    str: "YES" if all digits are unique, otherwise "NO".
    """
    return "YES" if len(set(number_string)) == len(number_string) else "NO"


# Read input and call the function
print(has_unique_digits(input()))
