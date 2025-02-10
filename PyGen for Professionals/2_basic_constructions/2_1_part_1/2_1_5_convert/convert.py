'''
TODO:
    Implement the convert() function, which takes one argument:
        string — an arbitrary string

    The function should return a string:
        - completely in lowercase if there are more lowercase letters in this
          line
        - fully uppercase if there are more uppercase letters in this line
        - completely in lowercase if the number of uppercase and lowercase
          letters in this line is the same

NOTE:
    String characters that are not letters should be ignored.
'''


def convert(given_string: str) -> str:
    """
    Converts the given string to lowercase or uppercase based on the frequency
    of lowercase and uppercase letters. Non-letter characters are ignored.

    Args:
        given_string (str): The input string to convert.

    Returns:
        str: The converted string based on the conditions.
    """
    lower_count = sum(1 for c in given_string if c.islower())
    upper_count = sum(1 for c in given_string if c.isupper())

    if lower_count >= upper_count:
        return given_string.lower()
    else:
        return given_string.upper()
