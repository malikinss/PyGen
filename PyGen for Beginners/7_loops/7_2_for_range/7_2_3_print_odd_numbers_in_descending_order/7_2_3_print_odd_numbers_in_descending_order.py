'''
TODO:
    Two integers m and n (m > n) are given.
    Write a program that prints all odd numbers from m to n inclusive
    in descending order.
'''


def print_odd_numbers_in_descending_order(m: int, n: int) -> None:
    """
    Prints all odd numbers between m and n (inclusive) in descending order.

    Args:
        m (int): The starting number.
        n (int): The ending number.

    Returns:
        None

    This function iterates through the range from m to n and prints
    all odd numbers.
    The order of printing is descending if m > n.
    """
    if m <= n:
        print("Error: m should be greater than n.")
        return

    # Iterate through the range from m to n (inclusive) in descending order
    for i in range(m, n - 1, -1):
        # Check if the number is odd
        if i % 2 != 0:
            print(i)


# Input data
m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))

# Call the function
print_odd_numbers_in_descending_order(m, n)
