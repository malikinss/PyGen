'''
TODO:
    The input to the program is one line.

    Write a program that prints the elements of a row in reverse order.
'''


def print_reverse_order(input_string: str) -> None:
    """
    Prints the characters of the input string in reverse order, one per line.

    Args:
        input_string (str): The string to process.

    Returns:
        None: Prints each character in reverse order, one per line.
    """
    for i in range(-1, -len(input_string)-1, -1):
        print(input_string[i])


# Input from the user
user_input = input("Enter a string: ")

# Call the function to display the result
print_reverse_order(user_input)
