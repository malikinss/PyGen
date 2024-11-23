'''
TODO:
    Complete the above code so that it outputs the arithmetic
    mean of the elements of the evens list.
'''
from typing import List

# original code
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# fixed code
def calculate_mean(numbers: List[int]) -> float:
    """
    Calculates and returns the arithmetic mean of the given list of numbers.
    """
    return sum(numbers) / len(numbers)


# List of even numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Call the function and print the result
print(calculate_mean(evens))
