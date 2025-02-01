'''
TODO:
    Write a program that draws a picture of regular polygons using the sample.

    The polygons should have different colors.

NOTE:
    Modify the program so that the area of all polygons is the same.

    The area of a regular polygon is calculated using the formula

    S = (n * a^2)/(4tg * (180∘/n)), where n is the number of sides and
    a is the side length.

    Please note that the trigonometric functions of the math module work with
    radians, not degrees.

    To convert degrees to radians, use the radians function.
'''
import turtle as t
import random as r
from math import tan, radians


def set_up_turtle():
    """Set up the turtle with the correct speed and hide it."""
    t.speed(0)
    t.hideturtle()
    t.up()


def generate_random_color():
    """Generate a random RGB color."""
    return r.randrange(256), r.randrange(256), r.randrange(256)


def create_polygon_turtle():
    """Create and return a turtle for drawing a polygon with random color."""
    poly = t.Turtle()
    poly.hideturtle()
    poly.up()
    poly.fillcolor(generate_random_color())
    poly.speed(0)
    return poly


def calculate_side_length_for_area(n, target_area):
    """
    Calculate the side length of a polygon with n sides to match the
    given area.

    The area formula is:
    S = (n * a^2) / (4 * tan(180 / n))
    Solving for a:
    a = sqrt((4 * S * tan(180 / n)) / n)
    """
    # Convert degrees to radians for tan
    angle_in_radians = radians(180 / n)

    # Calculate the side length for the given target area
    side_length = ((4 * target_area * tan(angle_in_radians)) / n) ** 0.5
    return side_length


def calculate_grid_size(num_polygons):
    """Calculate grid size based on the number of polygons."""
    return int(num_polygons ** 0.5)


def calculate_position(j, i, side_length, grid_size):
    """
    Calculate the position for the polygon in the grid based on row (i),
    column (j), and side length of the polygon.
    """
    x_pos = -160 + 80 * j - side_length / 2
    y_pos = 160 - 80 * i + side_length / 2
    return x_pos, y_pos


def draw_single_polygon(poly, num_of_sides, side_length, x_pos, y_pos):
    """Draw a regular polygon at the specified position."""
    poly.goto(x_pos, y_pos)
    poly.pendown()
    poly.begin_fill()
    for _ in range(num_of_sides):
        poly.forward(side_length)
        poly.right(360 / num_of_sides)
    poly.end_fill()


def draw_all_polygons(sides_of_polygons, target_area, num_polygons=5):
    """Draw a grid of polygons with random colors and fixed area."""
    grid_size = calculate_grid_size(num_polygons)  # Calculate grid size

    # Create and store the polygons
    polygons = []
    for i in range(grid_size):
        for j in range(grid_size):
            num_of_sides = r.randrange(3, 8)
            side_length = sides_of_polygons[num_of_sides]
            poly = create_polygon_turtle()

            # Calculate position for the polygon
            x_pos, y_pos = calculate_position(j, i, side_length, grid_size)
            polygons.append((poly, num_of_sides, x_pos, y_pos))

    # Draw all polygons
    for poly, num_of_sides, x_pos, y_pos in polygons:
        draw_single_polygon(
            poly, num_of_sides, sides_of_polygons[num_of_sides], x_pos, y_pos
        )


def draw_regular_polygons():
    target_area = 200  # Desired area for all polygons (can be adjusted)

    # Set up the screen and turtle
    set_up_turtle()

    # Create a dictionary to hold the side lengths of polygons with
    # the given area
    sides_of_polygons = {4: 0}  # Placeholder for 4 sides, to calculate later

    # Calculate the side length for each polygon (3 to 7 sides) to maintain
    # the same area
    for n in (3, 5, 6, 7):
        sides_of_polygons[n] = calculate_side_length_for_area(n, target_area)

    # Draw the polygons
    draw_all_polygons(sides_of_polygons, target_area, num_polygons=5)
    t.done()


# Run the program
draw_regular_polygons()
