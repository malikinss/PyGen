'''
TODO:
    The input to the program is a string of text.

    Write a program that displays the words of the input
    string in a column.
'''


def print_words_in_column(text: str) -> None:
    """
    This function takes a string and prints its words in a column.

    Args:
        text (str): The input string that contains words to be printed
        in a column.

    Returns:
        None: The function prints the words in a column and does not return
        any value.
    """
    words = text.split()
    print(*words, sep='\n')


# Input the string
s = input()

# Call the function with the input string
print_words_in_column(s)
