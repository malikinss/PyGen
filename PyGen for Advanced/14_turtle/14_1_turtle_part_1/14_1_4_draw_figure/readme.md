# Drawing a Figure with Eight Squares using Turtle Graphics

## Description 📝

This Python program uses the Turtle graphics module to draw a figure consisting of eight squares.
The function `square(side)` is used to draw individual squares, and the function `draw_figure(num_squares, side)` arranges the squares in a circular pattern by rotating the turtle after each square is drawn.

## Purpose 🎯

The purpose of this program is to demonstrate how to use Python's Turtle graphics module to draw multiple shapes and create a figure with squares.
The program arranges the squares in a circular pattern by rotating the drawing direction after each square.

## How It Works 🔍

1. **Input**:
    - The user provides the side length of the square and the number of squares to be drawn.
    - The program draws eight squares, each rotated around the center.
2. **Processing**:
    - The `square(side)` function draws a square by moving the turtle forward for the length of the side and turning 90 degrees after each side.
    - The `draw_figure(num_squares, side)` function repeatedly calls the `square(side)` function and rotates the turtle after drawing each square to form a figure with multiple squares arranged in a circular pattern.
3. **Output**:
    - The program visually draws a figure made up of eight squares arranged in a circular pattern.

## Output 📜

The program draws a figure consisting of eight squares, with each square rotated and arranged in a circular shape.

### Example:

For the input:

```
num_squares = 8
side = 120
```

The output will be a figure of eight squares, each with a side length of 120 pixels, arranged in a circular pattern.

## Usage 📦

1. Save the code in a file, e.g., `eight_squares.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python eight_squares.py`
5. The program will open a Turtle graphics window and draw the figure of eight squares.

## Conclusion 🚀

This program demonstrates how to use Python's Turtle graphics module to create a figure made up of eight squares.
It shows how to rotate shapes to create complex designs and how to manipulate the turtle's movement for pattern creation.
