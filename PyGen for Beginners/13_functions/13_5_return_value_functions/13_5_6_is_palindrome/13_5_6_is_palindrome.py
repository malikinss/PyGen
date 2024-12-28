'''
TODO:
    Write a function is_palindrome(text) that takes the string text
    as an argument and returns True if the specified text is a palindrome
    and False otherwise.
'''


def is_palindrome(text: str) -> bool:
    """
    Checks if the given text is a palindrome.

    A palindrome is a word, phrase, or sequence of characters that reads
    the same backward as forward, ignoring spaces and punctuation.

    Args:
        text (str): The text to check.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    symbols = [' ', ',', '.', '!', '?', '-']

    # Remove unwanted symbols from the text
    for c in symbols:
        text = text.replace(c, '')

    # Convert the text to lowercase to make the comparison case-insensitive
    text = text.lower()

    # Check if the text is equal to its reverse
    return text == text[::-1]


# Example usage
txt = input("Enter text: ")
print(is_palindrome(txt))
