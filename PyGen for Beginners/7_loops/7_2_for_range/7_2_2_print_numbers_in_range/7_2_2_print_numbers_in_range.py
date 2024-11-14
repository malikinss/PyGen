'''
TODO:
    Two integers m and n are given.
    Write a program that prints all numbers from m to n inclusive,
    in ascending order if m < n, or in descending order otherwise.
'''


def print_numbers_in_range(m: int, n: int) -> None:
    """
    Prints all numbers from m to n inclusive in ascending or descending order,
    depending on whether m < n or not.

    Args:
        m (int): The starting number.
        n (int): The ending number.

    Returns:
        None

    The function prints each number in the range from m to n inclusive,
    either in ascending or descending order based on the relationship
    between m and n.
    """
    if m < n:
        # Ascending order
        for i in range(m, n + 1):
            print(i)
    else:
        # Descending order
        for i in range(m, n - 1, -1):
            print(i)


# Input data
m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))

# Call the function
print_numbers_in_range(m, n)
