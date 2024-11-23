'''
TODO:
    Complete the above code using a list expression so that you get a new list
    containing the strings of the original list with the first character
    removed.
'''
from typing import List


def remove_first_character(keywords: List[str]) -> List[str]:
    """
    Removes the first character from each string in the given list.

    Args:
        keywords (List[str]): A list of strings.

    Returns:
        List[str]: A new list with the first character removed from
        each string.
    """
    return [s[1:] for s in keywords]


# List of keywords
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break',
            'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
            'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in',
            'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
            'while', 'yield']

# Call the function to remove the first character and store the result
new_keywords = remove_first_character(keywords)

# Print the resulting list
print(new_keywords)
