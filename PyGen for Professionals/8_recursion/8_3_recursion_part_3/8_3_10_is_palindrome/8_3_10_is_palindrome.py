'''
TODO:
    Implement the is_palindrome() function using recursion that takes
    one argument:
        - string — an arbitrary string

    The function should return True if the passed string is a palindrome,
    or False otherwise.

NOTE:
    A palindrome is text that reads the same in both directions.

    The empty string is a palindrome, as is a string consisting of a
    single character.
'''


def is_palindrome(string: str) -> bool:
    """
    Check if the given string is a palindrome using recursion.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    if len(string) in (0, 1):
        return True
    if string[0] != string[-1]:  # Compare first and last characters
        return False
    return is_palindrome(string[1:-1])  # Check the remaining substring


# Example usage
print(is_palindrome('stepik'))  # Output: False
print(is_palindrome('level'))   # Output: True
print(is_palindrome('122333221'))  # Output: True
