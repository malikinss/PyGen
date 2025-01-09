'''
TODO:
    The program is given two numbers as input.

    Write a program that determines whether these numbers contain
    the same digits.
'''


def have_same_digits(number1: str, number2: str) -> str:
    """
    Determines if two numbers contain the same digits.

    Args:
        number1 (str): First number as a string.
        number2 (str): Second number as a string.

    Returns:
        str: "YES" if the numbers contain the same digits, otherwise "NO".
    """
    if set(number1) == set(number2):
        return "YES"
    return "NO"


# Main execution
number1 = input()
number2 = input()

print(have_same_digits(number1, number2))
