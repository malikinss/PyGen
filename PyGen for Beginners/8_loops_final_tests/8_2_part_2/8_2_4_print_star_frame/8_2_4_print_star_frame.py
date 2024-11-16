'''
TODO:
    The input to the program is a natural number n.

    Write a program that prints an n*19 star frame.
'''


def print_star_frame(n: int) -> None:
    """
    Prints a star frame of size n*19.

    Args:
        n (int): The number of rows for the star frame (n >= 1).
    """
    for i in range(n):
        if i == 0 or i == (n - 1):
            # Print the full star row for the first and last row
            print("*" * 19)
        else:
            # Print the star frame for the intermediate rows
            print("*" + " " * 17 + "*")


# Input and function call
n = int(input("Enter the number of rows: "))
print_star_frame(n)
