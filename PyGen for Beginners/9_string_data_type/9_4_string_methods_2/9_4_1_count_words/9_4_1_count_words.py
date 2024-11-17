'''
TODO:
    The input to the program is a string of text consisting of words separated
    by exactly one space.

    Write a program that counts the number of words in it.
'''


def count_words(input_string: str) -> int:
    """
    Counts the number of words in the given string, assuming
    words are separated by exactly one space.

    Args:
        input_string (str): The string to be analyzed.

    Returns:
        int: The number of words in the input string.
    """
    # Count the number of spaces and add 1 to get the number of words
    total_words = input_string.count(' ') + 1

    return total_words


# User input
given_string = input("Enter the string: ")

# Count and display the result
print(count_words(given_string))
