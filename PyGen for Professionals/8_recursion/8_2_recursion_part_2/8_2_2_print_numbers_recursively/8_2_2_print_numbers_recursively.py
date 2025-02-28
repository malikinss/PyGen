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
    def print_single_number(num: int) -> None:
        """
        Recursively prints a single number and calls itself for the next
        number.

        Args:
            num (int): The current number to print.
        """
        if num <= end:
            print(num)
            print_single_number(num + 1)

    print_single_number(start)


print_numbers_recursively(1, 100)
