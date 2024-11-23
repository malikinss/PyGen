'''
TODO:
    The input to the program is a line of text containing words.
    Write a program that displays the words of the input string in a column.
'''


def print_words_in_column(text: str) -> None:
    """
    Prints each word from the input text on a new line.

    Args:
        text (str): A string containing words separated by spaces.
    """
    words = text.split()  # Split the input text into a list of words
    print(*words, sep='\n')  # Print each word on a new line


def main() -> None:
    """
    Prompts the user for a line of text and displays the words in the text
    in a column format, one word per line.
    """
    text = input("Enter a line of text: ")  # Get user input
    print_words_in_column(text)  # Call the function to print words in a column


# Calling the main function to execute the program
main()
