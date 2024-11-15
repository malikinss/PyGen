'''
TODO:
    Given a natural number n.

    Write a program that prints a numerical triangle according to the example:
        1
        22
        333
        4444
        55555
        ...

NOTE:
    Use a nested for loop.
'''


def print_numerical_triangle(n: int) -> None:
    """
    Prints a numerical triangle where the i-th row contains
    the number 'i' repeated 'i' times.

    The pattern follows this structure:
        1
        22
        333
        4444
        ...

    Args:
    n (int): The number of rows in the triangle.

    Returns:
    None: This function does not return any value, it directly prints
    the pattern.
    """

    for i in range(1, n + 1):
        for j in range(i):
            print(i, end="")  # Print the number 'i', 'i' times

        print()  # Move to the next line after printing the row


# Get input from the user
n = int(input("Enter a natural number: "))
# Call the function to print the triangle
print_numerical_triangle(n)
