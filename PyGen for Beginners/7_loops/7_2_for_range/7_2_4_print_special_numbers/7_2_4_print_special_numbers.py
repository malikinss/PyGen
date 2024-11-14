'''
TODO:
    Given two natural numbers m and n (m ≤ n).

    Write a program that prints all numbers from m to n inclusive that
    satisfy at least one of the following conditions:
        - the number is divisible by 17 without a remainder;
        - the number ends in 9;
        - the number is divisible by 3 and 5 without a remainder
          at the same time.
'''


def print_special_numbers(m: int, n: int) -> None:
    """
    Prints all numbers from m to n (inclusive) that satisfy at least one
    of the following conditions:
        - The number is divisible by 17 without a remainder.
        - The number ends in 9.
        - The number is divisible by both 3 and 5 without a remainder.

    Args:
        m (int): The starting number.
        n (int): The ending number.

    Returns:
        None
    """
    if m > n:
        print("Error: m should be less than or equal to n.")
        return

    for i in range(m, n + 1):
        # Check if the number satisfies any of the given conditions
        if (i % 10 == 9) or (i % 17 == 0) or (i % 15 == 0):
            print(i)


# Input data
m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))

# Call the function
print_special_numbers(m, n)
