'''
TODO:
    The input to the program is a text string containing natural numbers.

    Write a program that inserts a + sign between each number and then
    calculates the sum of the resulting numbers.
'''


def sum_of_numbers(input_string: str) -> None:
    """
    This function takes a string of natural numbers separated by spaces,
    inserts a '+' sign between each number, and then calculates and prints the
    sum of those numbers.

    Args:
    input_string (str): A string containing natural numbers separated
    by spaces.

    Returns:
    None: This function prints the numbers with a '+' sign between them
    and the sum at the end.

    Example:
    If the input string is '1 2 3 4', the output will be:
    1+2+3+4=10
    """
    # Convert the input string to a list of integers
    numbers = [int(i) for i in input_string.split()]

    # Print the numbers with '+' between them and then the sum
    print(*numbers, sep='+', end='=')  # Print the numbers with '+' between
    print(sum(numbers))  # Print the sum of the numbers


# Example usage
input_string = input()  # Read input string
sum_of_numbers(input_string)  # Call the function
