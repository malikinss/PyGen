'''
TODO:
    The input to the program is a string.
    Write a program that counts the number of lowercase alphabetic characters.
'''


def count_lowercase_characters(input_string: str) -> int:
    """
    Counts the number of lowercase alphabetic characters in the input string.

    Args:
        input_string (str): The string to be analyzed.

    Returns:
        int: The number of lowercase alphabetic characters in the input string.
    """
    lower_cnt = 0

    # Iterate through the string and count lowercase characters
    for char in input_string:
        if char.islower():
            lower_cnt += 1

    return lower_cnt


# User input
given_string = input("Enter the string: ")

# Count and display the result
print(count_lowercase_characters(given_string))
