# House Drawing Program

## Description 📝

This Python program uses the Turtle graphics library to draw a simple house with a rectangular body and a triangular roof. The program defines a function to draw polygons, which is then used to draw the body and roof of the house with specified dimensions and colors.

## Purpose 🎯

The goal of this program is to demonstrate basic Turtle graphics techniques, including drawing shapes, working with angles, and using colors to fill polygons. This is a fun way to learn how to combine basic shapes to create a more complex figure like a house.

## How It Works 🔍

1. **Drawing Polygons**:

    - The `draw_shape` function is used to draw polygons with a specified number of sides, side length, angle, and color. The function draws each side of the polygon, turns at the specified angle, and fills the shape with the given color.

2. **Drawing the House**:

    - The `draw_house` function calls the `draw_shape` function twice to draw the body and roof of the house. The body is drawn as a square (4 sides) and the roof as a triangle (3 sides).

3. **House Body**:

    - The house's body is drawn with a brown color (RGB: 185, 122, 87) and is a square with side lengths of 120 units.

4. **House Roof**:
    - The roof is drawn as an equilateral triangle with side lengths of 120 units, and it is filled with a blue color (RGB: 0, 162, 232).

## Output 📜

The output is a drawing of a simple house, consisting of a square body and a triangular roof, both filled with colors. The body is brown, and the roof is blue. The drawing will be displayed in a Turtle graphics window.

### Example:

A window will appear with a house shape consisting of a square base and a triangle roof.

## Usage 📦

1. Save the code in a file, e.g., `house.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python house.py`
5. The program will open a Turtle graphics window and draw the house.

## Conclusion 🚀

This program demonstrates how to use basic Turtle graphics commands to create a simple illustration of a house. It teaches essential concepts like loops, angles, and color filling while creating a visually appealing result.
