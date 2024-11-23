'''
TODO:
    The input to the program is a text string containing various
    natural numbers.

    A list of numbers is formed from this string.

    Write a program that swaps the minimum and maximum elements
    of this list.
'''
from typing import List


def swap_min_max_elements(numbers: List[int]) -> List[int]:
    """
    Swaps the minimum and maximum elements in a list of integers.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The list with the minimum and maximum elements swapped.
    """
    # Find the indices of the maximum and minimum elements
    max_idx = numbers.index(max(numbers))
    min_idx = numbers.index(min(numbers))

    # Swap the elements
    numbers[max_idx], numbers[min_idx] = numbers[min_idx], numbers[max_idx]
    return numbers


# Input: Read a string of natural numbers and convert to a list of integers
input_numbers = list(map(int, input().split()))

# Swap the min and max elements
swapped_numbers = swap_min_max_elements(input_numbers)

# Print the updated list
print(*swapped_numbers)
