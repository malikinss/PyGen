'''
TODO:
    The program is given two numbers as input.

    Write a program that determines whether the first number contains
    all the digits contained in the second number (regardless of repetition,
    i.e. the number of digits) or not.
'''


def contains_all_digits(number1: str, number2: str) -> str:
    """
    Determines if the first number contains all digits of the second number.

    Args:
        number1 (str): The first number as a string.
        number2 (str): The second number as a string.

    Returns:
        str: "YES" if all digits in the second number are present in the first,
             otherwise "NO".
    """
    if set(number2).issubset(set(number1)):
        return "YES"
    return "NO"


number1 = input()
number2 = input()

print(contains_all_digits(number1, number2))
