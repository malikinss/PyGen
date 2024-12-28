'''
TODO:
    Write a function is_valid_triangle(side1, side2, side3) that takes three
    natural numbers as arguments, and returns True if there is
    a non-degenerate triangle with sides side1, side2, side3,
    and False otherwise.
'''


def is_valid_triangle(side1, side2, side3):
    """
    Checks if three sides can form a valid (non-degenerate) triangle.

    A triangle is valid if the sum of any two sides is greater than
    the third side.
    This is known as the triangle inequality theorem.

    Args:
        side1 (int): The length of the first side of the triangle.
        side2 (int): The length of the second side of the triangle.
        side3 (int): The length of the third side of the triangle.

    Returns:
        bool: True if the sides form a valid triangle, False otherwise.

    Example:
        is_valid_triangle(3, 4, 5)
        # Returns: True

        is_valid_triangle(1, 2, 3)
        # Returns: False
    """
    expression_1 = side1 < side2 + side3
    expression_2 = side2 < side1 + side3
    expression_3 = side3 < side1 + side2

    result = expression_1 and expression_2 and expression_3
    return result


a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))
