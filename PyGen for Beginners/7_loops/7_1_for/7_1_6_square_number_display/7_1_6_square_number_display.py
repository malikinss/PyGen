"""
TODO:
    The input to the program is a natural number n.
    Write a program that for each of the numbers from 0 to n (inclusive)
    displays the phrase:
    "The square of the number [number] is equal to [number]" (without quotes).

    Args:
        n (int): A natural number.

    Returns:
        None
"""


def display_square_of_numbers(n: int) -> None:
    """
    Prints the square of each number from 0 to n (inclusive) in the format:
    "The square of the number [number] is equal to [square]".

    Args:
        n (int): The upper limit number.

    Raises:
        ValueError: If n is not a natural number.
    """
    if n < 0:
        raise ValueError("Input must be a natural number.")

    for i in range(n + 1):
        square = i ** 2
        print(f'The square of the number {i} is equal to {square}')


# Get user input and validate it
try:
    n = int(input("Enter a natural number: "))
    display_square_of_numbers(n)
except ValueError as e:
    print(f"Error: {e}")
