'''
TODO:
    Write a program that sorts a list of points coordinates of points in
    a plane according to their distance from the origin (point (0;0)).

    The program should output the sorted list.

NOTE:
    The distance from the origin O(0;0) to the point A(x;y)
    is OA=sqrt(x^2 + y^2)
'''
from typing import List, Tuple


def get_distance_from_origin(point: Tuple[int, int]) -> float:
    """
    Calculates the distance from the origin (0, 0) to the given point (x, y).

    Args:
        point (Tuple[int, int]): A tuple representing the coordinates (x, y)
                                 of a point.

    Returns:
        float: The distance from the origin to the point.
    """
    x, y = point
    return (x ** 2 + y ** 2) ** 0.5


points: List[Tuple[int, int]] = [
    (-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0),
    (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)
]

# Sort the list of points by distance from the origin
points.sort(key=get_distance_from_origin)

print(points)
