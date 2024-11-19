'''
TODO:
    The input to the program is a string of text.

    Write a program that translates each of its characters into its
    corresponding code from the Unicode character table.
'''


def string_to_unicode(string: str):
    """
    Converts each character in the given string to its Unicode code point.

    Args:
        string (str): The input string to be converted.

    Returns:
        None: Prints the Unicode code points of the characters in the string.
    """
    for char in string:
        print(ord(char), end=' ')


# Input the string from the user
given_string = input()

# Call the function
string_to_unicode(given_string)
