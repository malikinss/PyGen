'''
TODO:
    Write a program using recursion that prints a sequence of natural
    numbers from 1 to 100 inclusive.
'''


def print_numbers_recursively(start: int, end: int) -> None:
    """
    Recursively prints natural numbers from `start` to `end` inclusive.

    Args:
        start (int): The starting number of the sequence.
        end (int): The ending number of the sequence.
    """
    if start <= end:
        print(start)
        print_numbers_recursively(start + 1, end)


# Call the function to print numbers from 1 to 100
print_numbers_recursively(1, 100)
