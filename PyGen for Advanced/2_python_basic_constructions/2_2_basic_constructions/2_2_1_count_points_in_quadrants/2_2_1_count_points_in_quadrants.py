'''
TODO:
    Given a set of points on a coordinate plane.

    Count and print the number of points lying in each coordinate quadrant.

    The first line contains the number of points.

    Each next line consists of two integers - the coordinates of the point
    (first the abscissa - x, then the ordinate - y), separated by
    a space character.

NOTE:
    Please note that points lying on the coordinate axes are not usually
    assigned to any coordinate quadrant.
'''
from typing import List, Tuple


def count_points_in_quadrants(points: List[Tuple[int, int]]) -> List[int]:
    """
    Count the number of points that lie in each of the four
    coordinate quadrants.

    Parameters:
    - points (List[Tuple[int, int]]): A list of tuples, each containing the
    (x, y) coordinates of a point.

    Returns:
    - List[int]: A list of four integers representing the count of points
    in each quadrant [First, Second, Third, Fourth].
    """
    count = [0, 0, 0, 0]  # Quadrant counters in order: 1st, 2nd, 3rd, 4th

    for x, y in points:
        if x > 0 and y > 0:
            count[0] += 1  # First quadrant
        elif x < 0 and y > 0:
            count[1] += 1  # Second quadrant
        elif x < 0 and y < 0:
            count[2] += 1  # Third quadrant
        elif x > 0 and y < 0:
            count[3] += 1  # Fourth quadrant

    return count


def main() -> None:
    """
    Main function to handle user input and print the results.
    """
    n = int(input("Enter number of points: "))
    points = [tuple(map(int, input().split())) for _ in range(n)]

    count = count_points_in_quadrants(points)  # type: ignore
    names = ['First quarter:', 'Second quarter:',
             'Third quarter:', 'Fourth quarter:']

    for i in range(4):
        print(names[i], count[i])


if __name__ == "__main__":
    main()
