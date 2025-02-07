'''
TODO:
    In the RGB color scheme, colors are specified using three components:
        - R is the intensity of the red component of the color;
        - G is the intensity of the green component of the color;
        - B is the intensity of the blue component of the color.

    Opposite colors are specified as RGB and (255-R)(255-G)(255-B).

    Such colors are considered to be in good harmony with each other.

    Write a program that, given three components of a given color, finds the
    components of the opposite color.
'''
from typing import Callable

# Lambda function to calculate the opposite color
get_opposite_color: Callable = lambda r, g, b: (255 - r, 255 - g, 255 - b)

# Read input values
r, g, b = map(int, input().split())

# Compute and print the opposite color
print(*get_opposite_color(r, g, b))
