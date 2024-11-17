'''
TODO:
    The input to the program is a string of text.

    Write a program that counts the number of digits in a given string.
'''


def count_digits_in_string(text: str) -> int:
    """
    Counts the number of digits in a given string.

    Args:
        text (str): The input string.

    Returns:
        int: The count of digits in the string.
    """
    counter = 0

    for i in range(10):
        counter += text.count(str(i))

    return counter


# User input
text = input("Enter a string: ")

# Get the result and print
result = count_digits_in_string(text)
print(result)
