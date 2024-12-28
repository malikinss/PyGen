'''
TODO:
    Write a function convert_to_python_case(text) that takes a camel case
    string as an argument and converts it to snake case.

NOTE:
    You can read more about naming styles here.
        https://ru.wikipedia.org/wiki/CamelCase
'''


def convert_to_python_case(text: str) -> str:
    """
    Converts a camel case string to snake case.

    Args:
        text (str): The camel case string to be converted.

    Returns:
        str: The snake case version of the input string.
    """
    new_text = ""

    for i, el in enumerate(text):
        # If the character is uppercase, we convert it to lowercase
        # and add an underscore before it, but only if it's not
        # the first character (to avoid leading underscore).
        if el.isupper():
            if i > 0:
                new_text += "_"
            new_text += el.lower()
        else:
            new_text += el

    return new_text


# Example usage
txt = input()
print(convert_to_python_case(txt))
