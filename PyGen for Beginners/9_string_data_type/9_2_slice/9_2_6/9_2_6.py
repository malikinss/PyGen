'''
TODO:
    The input to the program is one line.

    Write a program that outputs:
        - the total number of characters in the line;
        - original string repeated 3 times;
        - the first character of the string;
        - the first three characters of the string;
        - the last three characters of the string;
        - line in reverse order;
        - a string with the first and last character removed.
'''


def process_string(input_string: str) -> None:
    """
    Processes the input string to perform various tasks:
        - Calculate the total number of characters.
        - Repeat the string 3 times.
        - Extract specific parts of the string.
        - Reverse the string.
        - Remove the first and last characters.

    Args:
        input_string (str): The string to be processed.

    Returns:
        None: Outputs the results directly.
    """
    # Total number of characters
    print(len(input_string))

    # Original string repeated 3 times
    print(input_string * 3)

    # First character of the string
    print(input_string[0])

    # First three characters of the string
    print(input_string[:3])

    # Last three characters of the string
    print(input_string[-3:])

    # Line in reverse order
    print(input_string[::-1])

    # String with the first and last character removed
    print(input_string[1:-1])


# User input
user_string = input("Enter a string: ")

# Call the function
process_string(user_string)
