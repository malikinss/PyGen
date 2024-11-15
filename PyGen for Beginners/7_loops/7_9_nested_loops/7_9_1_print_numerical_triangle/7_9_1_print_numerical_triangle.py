'''
TODO:
    Given a natural number n.

    Write a program that prints a numerical triangle according to the example:
        1
        2 3
        4 5 6
        7 8 9 10
        11 12 13 14 15
        16 17 18 19 20 21
        ...

NOTE:
    Use a nested for loop.
'''


def print_numerical_triangle(n: int) -> None:
    """
    Prints a numerical triangle where the i-th row contains 'i'
    consecutive numbers.

    The pattern follows this structure:
        1
        2 3
        4 5 6
        7 8 9 10
        11 12 13 14 15
        16 17 18 19 20 21
        ...

    Args:
    n (int): The number of rows in the triangle.

    Returns:
    None: This function does not return any value, it directly prints
    the pattern.
    """

    a = 1  # Starting number

    # Outer loop for each row
    for i in range(1, n + 1):
        # Inner loop to print the numbers in each row
        for j in range(i):
            print(a, end=' ')
            a += 1  # Increment the number to be printed

        print()  # Move to the next line after each row


# Get input from the user
n = int(input("Enter a natural number: "))
# Call the function to print the triangle
print_numerical_triangle(n)
