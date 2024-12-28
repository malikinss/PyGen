'''
TODO:
    Write a function get_middle_point(x1, y1, x2, y2), which takes
    as arguments the coordinates of the ends of the segment (x1, y1, x2, y2)
    and returns the coordinates of the point that is the middle
    of this segment.
'''


def get_middle_point(x1: int, y1: int, x2: int, y2: int) -> tuple:
    """
    Calculates the midpoint of a line segment defined
    by two points (x1, y1) and (x2, y2).

    Args:
        x1 (int): The x-coordinate of the first point.
        y1 (int): The y-coordinate of the first point.
        x2 (int): The x-coordinate of the second point.
        y2 (int): The y-coordinate of the second point.

    Returns:
        tuple: A tuple (x, y) representing the coordinates of the midpoint.
    """
    # Calculate the midpoint coordinates
    x_new = (x1 + x2) / 2
    y_new = (y1 + y2) / 2

    return x_new, y_new


# Example usage
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

x, y = get_middle_point(x_1, y_1, x_2, y_2)

print(x, y)
