# Starry Night Program

## Description 📝

This Python program uses the Turtle graphics library to create a "starry night" image. It randomly generates 200 stars of various sizes and colors scattered across the screen. The stars are drawn in random positions with random orientations, simulating a starry sky.

## Purpose 🎯

The purpose of this program is to demonstrate how to use randomization in Turtle graphics to create an aesthetically pleasing and dynamic image. It also showcases the use of turtle functions to draw stars of different sizes and colors.

## How It Works 🔍

1. **Setting Up the Screen**:

    - The screen is configured with a black background to simulate the night sky. The screen also uses color mode set to 255 (for RGB color values) and turtle animation is set with a slow update rate to display the stars efficiently.

2. **Generating Random Position**:

    - The stars are placed at random positions across the screen using the `randint()` function to generate random x and y coordinates within a specified range (-300 to 300).

3. **Generating Random Colors**:

    - Each star is assigned a random color by generating three random integers (0 to 255) representing RGB values.

4. **Drawing Stars**:

    - The `draw_star()` function creates a star with five points. The size of the star is random, with each star having a random size between 2 and 50 units.

5. **Random Orientation and Speed**:

    - Each star is drawn with a random orientation (heading) and drawing speed for variation.

6. **Drawing the Stars**:
    - The program draws 200 stars, each with a random position, color, size, and orientation. The stars are drawn one by one in the turtle window, creating a random starry sky.

## Output 📜

The output is a randomly generated starry night scene, with 200 stars of various sizes, colors, and orientations scattered across the screen.

### Example:

The Turtle graphics window will show a black background with 200 stars scattered randomly. Each star will have a different size and color, creating a dynamic and unique image each time the program is run.

## Usage 📦

1. Save the code in a file, e.g., `starry_night.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python starry_night.py`
5. The program will open a Turtle graphics window displaying the starry night scene.

## Conclusion 🚀

This program is a fun and creative way to use Turtle graphics to generate random images. It demonstrates basic randomization, positioning, and drawing techniques in Python, all while producing a visually appealing result.
