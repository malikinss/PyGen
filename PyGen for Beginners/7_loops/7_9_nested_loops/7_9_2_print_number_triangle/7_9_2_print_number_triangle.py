'''
TODO:
    Given a natural number n.

    Write a program that prints a number triangle with a height of n,
    according to the example:
        1
        121
        12321
        1234321
        123454321
        ...

NOTE:
    Use a nested for loop.
'''


def print_number_triangle(n: int) -> None:
    """
    Prints a number triangle with a height of n, where each row contains
    numbers increasing from 1 to the row number and then decreasing back to 1.

    The pattern follows this structure:
        1
        121
        12321
        1234321
        123454321
        ...

    Args:
    n (int): The height of the triangle.

    Returns:
    None: This function directly prints the triangle and does not return
    any value.
    """

    # Outer loop for each row
    for i in range(1, n + 1):
        # Print the increasing numbers
        for j in range(1, i):
            print(j, end="")

        # Print the middle number (i)
        print(i, end="")

        # Print the decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")

        # Move to the next line after each row
        print()


# Get input from the user
n = int(input("Enter a natural number: "))
# Call the function to print the triangle
print_number_triangle(n)
