'''
TODO:
    The input to the program is a string of text.

    Write a program using a list expression that finds the length
    of the longest word.
'''


def longest_word_length(text: str) -> int:
    """
    Finds the length of the longest word in the given text.

    Args:
        text (str): The input string containing words.

    Returns:
        int: The length of the longest word.
    """
    words = text.split()  # Split the input string into words
    if not words:  # If the list is empty, return 0 (or handle accordingly)
        return 0
    return max(len(word) for word in words)  # Find the longest word length


# Input string
given_string = input()

# Output the length of the longest word
print(longest_word_length(given_string))
