'''
TODO:
    The input to the program is one line.

    Write a program that prints the message "Digit" (without quotes)
    if a string contains a digit. Otherwise, display the message
    "No digits" (without quotes).
'''


def check_for_digits(input_string: str) -> str:
    """
    Checks if the input string contains any digits.

    Args:
        input_string (str): The string to be checked.

    Returns:
        str: "Digit" if the string contains a digit, otherwise "No digits".
    """
    for char in input_string:
        if char.isdigit():
            return "Digit"
    return "No digits"


# User input
given_string = input("Enter a string: ")

# Output result
result = check_for_digits(given_string)
print(result)
