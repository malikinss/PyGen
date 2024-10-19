"""
TODO:
    The input to the program is a natural number n (n≥2)
    - the leg of a right-angled isosceles triangle.

    Write a program that prints a star triangle according to the example.

    Args:
        n (int): The leg of the triangle, a natural number greater than
        or equal to 2.

    Returns:
        None
"""


def print_star_triangle(n: int) -> None:
    """
    Prints a right-angled isosceles triangle made of stars.

    Args:
        n (int): The leg of the triangle.

    Raises:
        ValueError: If n is less than 2.
    """
    if n < 2:
        raise ValueError("Input must be a natural number greater than or equal to 2.")

    star = '*'

    for i in range(n):
        print(star * (n - i))


# Get user input and validate it
try:
    n = int(input("Enter a natural number (n≥2): "))
    print_star_triangle(n)
except ValueError as e:
    print(f"Error: {e}")
