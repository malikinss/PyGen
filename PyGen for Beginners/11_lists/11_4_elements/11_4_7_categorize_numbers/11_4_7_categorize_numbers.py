'''
TODO:
    The input to the program is a natural number n, and then n integers.

    Write a program that first prints all negative numbers, then zeros,
    and then all positive numbers, each on a separate line.

    The numbers must be output in the same order in which they were entered.
'''


def categorize_numbers(n: int, numbers: list[int]) -> list[int]:
    """
    Categorizes the given list of numbers into negative, zero,
    and positive numbers, and returns them in the order:
        negatives, zeros, positives.

    Args:
        n (int): The number of input integers.
        numbers (list[int]): The list of integers to be categorized.

    Returns:
        list[int]: The categorized list of integers.
    """
    negatives = [num for num in numbers if num < 0]
    zeros = [num for num in numbers if num == 0]
    positives = [num for num in numbers if num > 0]

    return negatives + zeros + positives


# Input
n = int(input())  # Read number of integers
numbers = [int(input()) for _ in range(n)]  # Read n integers

# Categorize numbers
result = categorize_numbers(n, numbers)

# Output the result
print("\n".join(map(str, result)))
