'''
TODO:
    The input to the program is a string of text.
    Write a list expression program that prints all the numeric characters
    of a given string.
'''


def extract_numeric_characters(text: str) -> str:
    """
    Extracts all numeric characters from the input string.

    Args:
        text (str): The input string containing text and numeric characters.

    Returns:
        str: A string consisting of all numeric characters from
        the input string.
    """
    return ''.join(i for i in text if i.isdigit())


def main() -> None:
    """
    Prompts the user for a string and prints all numeric characters
    from the string without spaces.
    """
    s = input("Enter a string of text: ")
    numeric_characters = extract_numeric_characters(s)
    print(numeric_characters)


# Calling the main function to execute the program
main()
