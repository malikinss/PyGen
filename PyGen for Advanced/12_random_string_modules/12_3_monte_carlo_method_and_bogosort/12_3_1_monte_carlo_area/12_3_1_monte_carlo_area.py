'''
TODO:
    Write a program that uses the Monte Carlo method to calculate the area of
    a figure defined by a system of inequalities:

        ⎧-2 ≤ x ≤ 2
         -2 ≤ y ≤ 2
        ⎨x^3 + y^4 + 2 ≥ 0
        ⎩3x + y^2 ≤ 2
'''
import random


def is_inside_figure(x: float, y: float) -> bool:
    """
    Check if the point (x, y) is inside the figure defined by the inequalities.

    Args:
        x (float): x-coordinate of the point.
        y (float): y-coordinate of the point.

    Returns:
        bool: True if the point is inside the figure, False otherwise.
    """
    return x**3 + y**4 + 2 >= 0 and 3 * x + y**2 <= 2


def monte_carlo_area(trials: int, bounding_area: float) -> float:
    """
    Calculate the area of a figure using the Monte Carlo method.

    Args:
        trials (int): Number of random points to generate.
        bounding_area (float): Area of the bounding rectangle.

    Returns:
        float: Estimated area of the figure.
    """
    points_inside = 0

    for _ in range(trials):
        x = random.uniform(-2, 2)
        y = random.uniform(-2, 2)

        if is_inside_figure(x, y):
            points_inside += 1

    return (points_inside / trials) * bounding_area


trials = 10**6          # Number of Monte Carlo trials
bounding_area = 16      # Area of the bounding rectangle (-2 ≤ x, y ≤ 2)

estimated_area = monte_carlo_area(trials, bounding_area)
print(f"Estimated area of the figure: {estimated_area:.6f}")
