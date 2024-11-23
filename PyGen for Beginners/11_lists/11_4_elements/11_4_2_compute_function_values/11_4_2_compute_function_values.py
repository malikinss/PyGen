'''
TODO:
    The input to the program is a natural number n, and then n integers.

    Write a program that for each input number x prints the value of the
    function f(x)= x^2 + 2x + 1, each on a separate line.
'''


def compute_function_values(numbers: list[int]) -> list[int]:
    """
    Computes the values of f(x) = x^2 + 2x + 1 for a list of integers.

    Args:
        numbers (list[int]): List of input integers.

    Returns:
        list[int]: List of computed function values.
    """
    return [x * x + 2 * x + 1 for x in numbers]


# Input: number of integers and their values
n = int(input("Enter the number of integers: "))
numbers = [int(input("Enter a number: ")) for _ in range(n)]

# Display input numbers and computed values
print("\nInput numbers:")
print(*numbers, sep='\n')

print("\nComputed function values:")
print(*compute_function_values(numbers), sep='\n')
