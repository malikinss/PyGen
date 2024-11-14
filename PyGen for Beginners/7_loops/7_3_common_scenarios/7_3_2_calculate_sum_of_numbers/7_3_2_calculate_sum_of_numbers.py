'''
TODO:
    The input to the program is a natural number n,
    and then n integers, each on a separate line.

    Write a program that calculates the sum of the given numbers.
'''


def calculate_sum_of_numbers(n: int) -> int:
    """
    Calculates the sum of n integers.

    Args:
        n (int): The number of integers to sum.

    Returns:
        int: The sum of the n integers.
    """
    total = 0
    for _ in range(n):
        total += int(input())
    return total


# Input data
n = int(input("Enter the number of integers (n): "))

# Call the function and print the result
result = calculate_sum_of_numbers(n)
print(result)
