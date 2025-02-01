# Star Drawing Program

## Description 📝

This Python program allows the user to draw stars of different sizes, colors, and shapes by clicking the left mouse button on a black screen. The stars are drawn at the location of the mouse click and can have varying numbers of beams and figures. The stars' colors are generated randomly.

## Purpose 🎯

The program demonstrates how to use the `turtle` graphics library for interactive drawing. It allows users to draw stars with random properties at any location they click on the screen. The program also showcases handling mouse click events to trigger drawing actions.

## How It Works 🔍

1. **Random Star Properties**:

    - Each time the user clicks the screen, the program generates a star with random properties:
        - **Beams**: The number of beams or points of the star.
        - **Size**: The radius of the star.
        - **Color**: A random RGB color.

2. **Star Shapes**:

    - The stars can be of various shapes, including uneven stars (with more beams and figures) and square-like stars with 4 beams.
    - The drawing logic is handled by two main functions: `draw_uneven_star()` and `draw_square()`, which use geometric principles to generate the shapes based on the number of beams and other properties.

3. **Mouse Click Interaction**:

    - The program listens for left mouse clicks, and each click triggers the `left_mouse_click()` function, which draws a new star at the clicked location with random properties.

4. **Turtle Setup**:
    - The background color is set to black to make the stars stand out. The turtle is hidden for aesthetic purposes, and the drawing speed is set to the maximum for instant rendering.

## Output 📜

The output consists of a graphical display where the user can click on the screen to draw stars. Each star is randomly generated with different sizes, colors, and beam configurations.

### Example:

-   **Star with Random Size**: A star with a random radius between 15 and 40 units.
-   **Random Color**: Each star has a random color.
-   **Random Number of Beams**: The number of beams of each star is randomly chosen between 5 and 33.

## Usage 📦

1. Save the code in a file, e.g., `star_drawing.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python star_drawing.py`
5. The program will open a Turtle graphics window with a black background. Click anywhere on the screen to draw a star at that location.

## Conclusion 🚀

This program provides an interactive and fun way to explore drawing with turtle graphics. The random properties of the stars, including their size, color, and number of beams, ensure that each star is unique. It is a great demonstration of how to handle mouse events and generate random graphics in Python.
