'''
TODO:
    Implement a range_sum() function using recursion that takes three
    arguments in the following order:
        numbers is a list of integers
        start is a non-negative integer
        end is a non-negative integer

    The function should sum all the numbers in the numbers list
    from numbers[start] to numbers[end] inclusive and return the result.

NOTE:
    It is guaranteed that start <= end.
'''
from typing import List


def range_sum(numbers: List[int], start: int, end: int) -> int:
    """
    Calculate the sum of numbers in a list from the start index to the end
    index using recursion.

    Args:
        numbers (List[int]): The list of integers to sum.
        start (int): The starting index (inclusive).
        end (int): The ending index (inclusive).

    Returns:
        int: The sum of the specified range of numbers.
    """
    def calculate_sum(
        current_index: int, end_index: int, numbers: List[int], total: int = 0
    ) -> int:
        """
        Recursively calculate the sum of elements in a list from current_index
        to end_index.

        Args:
            current_index (int): The current index in the list.
            end_index (int): The end index in the list.
            numbers (List[int]): The list of integers to sum.
            total (int): The accumulated total sum.

        Returns:
            int: The sum of the specified range of numbers.
        """
        if current_index > end_index:
            return total

        current_element = numbers[current_index]

        return calculate_sum(
            current_index + 1,
            end_index,
            numbers,
            total + current_element
        )

    return calculate_sum(start, end, numbers)


# Test the function
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
