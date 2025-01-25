'''
TODO:
    Write a program that uses the Monte Carlo method to determine the
    approximate value of π.

NOTE:
    The area of a unit circle, i.e. a circle with a radius of R = 1, is:
        S = πR^2 = π.

    The equation of the unit circle is:
        x^2 + y^2 = 1
'''
import random


def is_inside_unit_circle(x: float, y: float) -> bool:
    """
    Check if the point (x, y) lies inside the unit circle.

    Args:
        x (float): x-coordinate of the point.
        y (float): y-coordinate of the point.

    Returns:
        bool: True if the point lies inside the unit circle, False otherwise.
    """
    return x**2 + y**2 <= 1


def estimate_pi(trials: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Args:
        trials (int): Number of random points to generate.

    Returns:
        float: Estimated value of π.
    """
    points_inside_circle = 0

    for _ in range(trials):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if is_inside_unit_circle(x, y):
            points_inside_circle += 1

    # π is approximately 4 times the ratio of points inside the circle
    return 4 * (points_inside_circle / trials)


trials = 10**6  # Number of Monte Carlo trials
estimated_pi = estimate_pi(trials)
print(f"Estimated value of π: {estimated_pi:.6f}")
