'''
TODO:
    At BEEGEEK school, class names are unusual.

    They have the following format:
        <class number><class letter>
    where <class number> must be in the range from 0 (like all programmers)
    to 9 inclusive, and the class letter can be any letter in the range
    from "A" to "P" inclusive.

    Write a program that takes a natural number n, and then n class names,
    each on a new line.

    For each class name, your program should output "YES" (without quotes)
    on a separate line if the class name is correct, or "NO" (without quotes)
    otherwise.

NOTE:
    We will assume that the letter Ё is not in the Russian alphabet,
    which means that a class with such a letter will also be considered
    incorrect. 😢
'''


def validate_classname(classname: str) -> str:
    """
    Validates whether a class name is in the correct format.

    A valid class name is in the format <class number><class letter>,
    where:
    - <class number> is a digit from '0' to '9'.
    - <class letter> is a letter from 'A' to 'P'.

    Parameters:
    - classname (str): The class name to validate.

    Returns:
    - str: 'YES' if the class name is valid, otherwise 'NO'.
    """
    # Check if the classname has exactly two characters
    len_exp = len(classname) == 2

    if len_exp:
        # Check if the first character is a digit between '0' and '9'
        digit_exp = (ord('0') <= ord(classname[0]) <= ord('9'))

        # Check if the second character is a letter between 'A' and 'P'
        letter_exp = (ord('A') <= ord(classname[1]) <= ord('P'))

        if digit_exp and letter_exp:
            return "YES"

    return "NO"


# Process each class name
for _ in range(int(input())):
    classname = input().strip()

    # Validate and print result for each class name
    print(validate_classname(classname))
