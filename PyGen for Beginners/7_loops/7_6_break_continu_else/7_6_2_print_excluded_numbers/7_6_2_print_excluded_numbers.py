'''
TODO:
    The input to the program is a natural number n.

    Write a program that prints numbers from 1 to n inclusive except for:
    - numbers from 5 to 9 inclusive;
    - numbers from 17 to 37 inclusive;
    - numbers from 78 to 87 inclusive.
'''


def print_excluded_numbers(n: int):
    """
    Prints numbers from 1 to n inclusive, excluding numbers in specific ranges:
    - From 5 to 9 inclusive
    - From 17 to 37 inclusive
    - From 78 to 87 inclusive

    Args:
        n (int): The input natural number.
    """
    i = 1
    while i <= n:
        if (5 <= i <= 9) or (17 <= i <= 37) or (78 <= i <= 87):
            i += 1
            continue
        print(i)
        i += 1


# Example usage:
n = int(input("Enter a natural number: "))
print_excluded_numbers(n)
