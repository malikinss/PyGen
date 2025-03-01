'''
TODO:
    Given a sequence of integers, write a program using recursion that prints
    the sequence in reverse order.

    The program is fed a sequence of integers, each on a separate line.

    The sequence ends with the number 0.
'''


def reverse_sequence() -> None:
    """
    Recursively prints a sequence of integers in reverse order. The sequence
    ends with the number 0, which is also printed but not considered part of
    the sequence.

    Args:
        None

    Returns:
        None
    """
    def _print_element_recursive() -> None:
        """
        Reads an integer input from the user and prints the entire sequence in
        reverse order once the number 0 is encountered.

        Args:
            None

        Returns:
            None
        """
        number = int(input())  # Read input

        if number != 0:
            _print_element_recursive()  # Recursively call until 0 is reached

        # Print the number after recursion ends (reversing the sequence)
        print(number)

    _print_element_recursive()


reverse_sequence()
