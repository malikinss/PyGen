'''
TODO:
    Write a program using recursion that takes a number as input and outputs
    the number of digits in that number.
'''


def print_digit_count(number: int) -> None:
    """
    Prints the number of digits in the given number.

    Args:
        number (int): The number to count digits in.
    """
    def count_digits(number: int) -> int:
        """
        Recursively counts the number of digits in the given number.

        Args:
            number (int): The number to count digits in.

        Returns:
            int: The count of digits.
        """
        if 0 <= number < 10:
            return 1  # Base case: if the number is a single digit

        # Recursive case: divide the number by 10
        return 1 + count_digits(number // 10)

    print(count_digits(number))


# Test the function
print_digit_count(11111)
