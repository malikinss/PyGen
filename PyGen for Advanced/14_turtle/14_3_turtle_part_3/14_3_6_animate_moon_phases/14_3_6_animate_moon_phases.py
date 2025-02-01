'''
TODO:
    Write a program that draws an animated image of the phases of the moon
    using a sample.
'''
import turtle


def setup_screen():
    """Sets up the screen with background color."""
    screen = turtle.Screen()
    screen.bgcolor('DarkBlue')  # Night sky background
    screen.setup(width=600, height=600)


def create_moon():
    """Creates and draws the moon at the center of the screen."""
    moon = turtle.Turtle()
    moon.hideturtle()
    moon.shape('circle')
    moon.color('orange')
    moon.penup()
    moon.goto(0, 0)
    moon.dot(200)  # Draw the moon
    return moon


def create_shadow_turtle():
    """Creates a turtle for the moon shadow."""
    shadow = turtle.Turtle()
    shadow.hideturtle()
    shadow.shape('circle')
    shadow.color('DarkBlue')  # Color for shadow
    shadow.penup()
    return shadow


def animate_moon_phases(shadow):
    """Animates the moon phases by moving the shadow."""
    while True:
        # Waxing phase: Shadow moves from left to right
        for i in range(-200, 200, 5):
            shadow.clear()  # Clear previous shadow
            shadow.goto(i, 0)
            shadow.dot(200)  # Draw shadow at new position
            turtle.update()  # Update screen to show the shadow movement

        # Waning phase: Shadow moves from right to left
        for i in range(200, -200, -5):
            shadow.clear()  # Clear previous shadow
            shadow.goto(i, 0)
            shadow.dot(200)  # Draw shadow at new position
            turtle.update()  # Update screen to show the shadow movement


def main():
    """Main function to set up the screen and animate the moon phases."""
    setup_screen()
    create_moon()
    shadow = create_shadow_turtle()

    # Set up the screen for animation
    # Turn off automatic screen updates for smoother animation
    turtle.tracer(0)
    animate_moon_phases(shadow)

    turtle.done()


# Run the animation
main()
