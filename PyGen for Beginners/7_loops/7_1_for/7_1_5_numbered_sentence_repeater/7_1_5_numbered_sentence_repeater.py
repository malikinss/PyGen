"""
TODO:
    Write a program that reads one line of text and outputs 10 lines,
    numbered 0 to 9, each with a specified line of text.

    Args:
        None (reads input from the user)

    Returns:
        None
"""


def print_numbered_lines(sentence: str) -> None:
    """
    Prints the sentence 10 times, each line numbered from 0 to 9.

    Args:
        sentence (str): The sentence to be printed.

    Raises:
        ValueError: If the input sentence is empty.
    """
    if not sentence.strip():
        raise ValueError("The input sentence cannot be empty.")

    for i in range(10):
        print(i, sentence)


# Get user input and validate it
try:
    sentence = input("Enter a sentence: ")
    print_numbered_lines(sentence)
except ValueError as e:
    print(f"Error: {e}")
