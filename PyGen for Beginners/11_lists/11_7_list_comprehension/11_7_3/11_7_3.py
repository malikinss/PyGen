'''
TODO:
    Complete the above code with a list expression to get a new list
    containing only words that are at least five characters long (inclusive).
'''


def filter_keywords(keywords: list[str]) -> list[str]:
    """
    Filters the given list of keywords and returns a list of words
    that are at least five characters long.

    Args:
        keywords (list of str): The list of keywords to be filtered.

    Returns:
        list of str: A list of keywords with at least five characters.
    """
    # Using list comprehension to filter keywords with length >= 5
    return [i for i in keywords if len(i) >= 5]


# Test the function
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break',
            'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
            'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in',
            'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
            'return', 'while', 'yield']

# Calling the function and storing the result
new_keywords = filter_keywords(keywords)

# Output the result
print(new_keywords)
