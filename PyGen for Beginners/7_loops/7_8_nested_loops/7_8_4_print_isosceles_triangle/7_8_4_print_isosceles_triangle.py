'''
TODO:
    Given an odd natural number n.

    Write a program that prints an isosceles star triangle with base n
    according to the example:
        *
        **
        ***
        ****
        ***
        **
        *

NOTE:
    Use a nested for loop.
'''


def print_isosceles_triangle(n: int) -> None:
    """
    Prints an isosceles triangle with stars, given an odd natural number n.

    The triangle will have a base of n stars, and the height will be n.
    The pattern of the stars will form an isosceles triangle, with the
    number of stars in the rows increasing until the middle and then
    decreasing symmetrically.

    Args:
    n (int): The odd natural number representing the size of the triangle.

    Returns:
    None: This function does not return any value, it directly prints
    the pattern.
    """

    # Upper part of the triangle (including the middle row)
    for i in range(n // 2 + 1):
        cur_cnt = i + 1  # Number of stars increases as we go down
        for j in range(cur_cnt):
            print("*", end="")
        print()  # Move to the next line after printing stars

    # Lower part of the triangle (after the middle row)
    for i in range(n // 2):
        cur_cnt = n // 2 - i  # Number of stars decreases after the middle row
        for j in range(cur_cnt):
            print("*", end="")
        print()  # Move to the next line after printing stars


# Get input from the user
n = int(input("Enter an odd natural number: "))
# Call the function to print the triangle
print_isosceles_triangle(n)
