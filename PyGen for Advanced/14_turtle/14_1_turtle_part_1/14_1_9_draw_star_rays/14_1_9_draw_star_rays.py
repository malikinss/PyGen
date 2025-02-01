'''
TODO:
    Write a program that draws the rays of a star.
'''
import turtle as t


def draw_star_rays(length: int) -> None:
    """
    Draws the rays of a star with the given length.

    Args:
        length (int): The length of each ray of the star.
    """
    for _ in range(6):
        t.forward(length)  # Draw one ray of the star
        t.backward(2 * length)  # Move to the opposite side
        t.forward(length)  # Return to the starting point
        t.left(30)  # Rotate to draw the next ray


# Call the function to draw the rays of the star
draw_star_rays(100)
