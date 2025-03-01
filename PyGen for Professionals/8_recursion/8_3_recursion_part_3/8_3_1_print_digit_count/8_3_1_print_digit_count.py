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
    digit_count = 0

    def count_digits(number: int, digit_count: int) -> int:
        """
        Recursively counts the number of digits in the given number.

        Args:
            number (int): The number to count digits in.
            digit_count (int): The current count of digits.

        Returns:
            digit_count (int): The final count of digits.
        """
        if 0 <= number < 10:
            return digit_count + 1

        return count_digits(number // 10, digit_count + 1)

    print(count_digits(number, digit_count))


print_digit_count(11111)
