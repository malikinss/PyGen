'''
TODO:
    The input to the program is one line.

    Write a program that displays the elements of a row
    with indices 0, 2, 4, ... in a column.
'''


def display_even_indexed_characters(input_string: str) -> None:
    """
    Displays the characters of the input string located at even
    indices (0, 2, 4, ...).

    Args:
        input_string (str): The input string to process.

    Returns:
        None: Prints each character located at even indices on a new line.
    """
    for i in range(0, len(input_string), 2):
        print(input_string[i])


# Input from the user
user_input = input("Enter a string: ")

# Call the function to display the result
display_even_indexed_characters(user_input)
