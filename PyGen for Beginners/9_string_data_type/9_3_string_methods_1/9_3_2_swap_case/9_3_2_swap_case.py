'''
TODO:
    The input to the program is a string.

    Write a program that changes the case of characters, in other words,
    change all lowercase characters to uppercase and vice versa.
'''


def swap_case(string: str) -> str:
    """
    Changes the case of characters in the given string: converts all
    lowercase characters to uppercase and all uppercase characters
    to lowercase.

    Args:
        string (str): The input string whose characters' cases will be swapped.

    Returns:
        str: The string with swapped cases.
    """
    # Swap the case of the string
    return string.swapcase()


# User input
input_string = input("Enter a string: ")

# Call the function and print the result
print(swap_case(input_string))
