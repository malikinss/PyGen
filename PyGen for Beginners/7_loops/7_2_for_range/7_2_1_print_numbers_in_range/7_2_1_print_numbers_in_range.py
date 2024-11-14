'''
TODO:
    Given two integers m and n, (m≤n).
    Write a program that prints all numbers from m to n inclusive.
'''


def print_numbers_in_range(m: int, n: int) -> None:
    """
    Prints all numbers from m to n inclusive.

    Args:
        m (int): The starting number.
        n (int): The ending number.

    Returns:
        None

    The function prints each number in the range from m to n, inclusive.
    """
    if m > n:
        print("Error: m should be less than or equal to n.")
        return

    for i in range(m, n + 1):
        print(i)


# Data Input
m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))

# Call
print_numbers_in_range(m, n)
