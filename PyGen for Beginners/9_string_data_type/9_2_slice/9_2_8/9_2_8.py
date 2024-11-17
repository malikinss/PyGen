'''
TODO:
    The input to the program is a string of text.

    Write a program that cuts it into two equal parts, rearranges them,
    and displays them on the screen.
'''


def rearrange_string(input_string: str) -> str:
    """
    Splits the input string into two equal parts, rearranges them,
    and returns the rearranged string.

    If the string has an odd length, the extra character is included
    in the first part.

    Args:
        input_string (str): The string to be rearranged.

    Returns:
        str: The rearranged string.
    """
    string_len = len(input_string)
    mid_len = string_len // 2

    # Adjust for odd-length strings
    if string_len % 2 != 0:
        mid_len += 1

    # Rearrange the string
    rearranged = input_string[mid_len:] + input_string[:mid_len]
    return rearranged


# User input
user_string = input("Enter a string: ")

# Call the function and display the result
print(rearrange_string(user_string))
