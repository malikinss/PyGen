'''
TODO:
    It was required to implement the swapcase_vowels() function, which takes a
    string as an argument, replaces all Latin vowels in it with capital
    letters, and returns the resulting new string.

    The programmer was in a hurry and implemented the function incorrectly.

    Find and correct all errors made in the implementation of this function
    (there are exactly 3 of them).

NOTE:
    It is known that each error affects only one string and can be corrected
    without changing other strings.
'''


# original code
def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''

    for char in string:
        if char == vowels:
            char.upper()
        swapped_string += char

    return print(swapped_string)


# fixed code
def swapcase_vowels2(string: str) -> str:
    """
    Replaces all Latin vowels in the given string with uppercase letters.

    Args:
        string (str): The input string.

    Returns:
        str: The modified string with vowels in uppercase.
    """
    vowels = 'aeiouy'
    return ''.join(char.upper() if char in vowels else char for char in string)
