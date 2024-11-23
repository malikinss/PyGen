'''
TODO:
    The input to the program is a string of text and a delimiter string.

    Write a program that inserts a specified separator between each character
    of an input string of text.
'''


def insert_separator(string_1: str, string_2: str) -> str:
    """
    This function inserts a specified separator between each character
    of an input string.

    Args:
        string_1 (str): The input string where the separator will be inserted.
        string_2 (str): The separator to be inserted between each character.

    Returns:
        str: A new string with the separator inserted between each character.
    """
    return string_2.join(string_1)


# Input: The first string and the separator
input_string = input()
separator = input()

# Call the function and print the result
result = insert_separator(input_string, separator)
print(result)
