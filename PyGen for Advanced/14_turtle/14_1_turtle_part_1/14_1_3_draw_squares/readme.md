# Drawing a Figure with Three Squares using Turtle Graphics

## Description 📝

This Python program uses the Turtle graphics module to draw a figure consisting of three squares.
The function `square(side)` is used to draw individual squares, and the function `draw_squares(side, num_squares)` arranges them in a specific pattern by rotating the turtle after each square is drawn.

## Purpose 🎯

The purpose of this program is to demonstrate how to use Python's Turtle graphics module to draw multiple shapes and create a figure with squares.
The program also showcases how to rotate the drawing to arrange shapes in a specific pattern.

## How It Works 🔍

1. **Input**:
    - The user provides the side length of the square.
    - The program draws three squares in a pattern by rotating the turtle after each square is drawn.
2. **Processing**:
    - The `square(side)` function draws a square by moving the turtle forward for the length of the side and turning 90 degrees after each side.
    - The `draw_squares(side, num_squares)` function repeatedly calls the `square(side)` function and rotates the turtle after drawing each square to form a figure with multiple squares.
3. **Output**:
    - The program visually draws a figure made up of three squares.

## Output 📜

The program draws a figure consisting of three squares, with each square rotated around the center.

### Example:

For the input:

```
side = 100
```

The output will be a figure of three squares, each with a side length of 100 pixels, arranged in a rotated pattern.

## Usage 📦

1. Save the code in a file, e.g., `three_squares.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python three_squares.py`
5. Enter the side length when prompted.
6. The program will open a Turtle graphics window and draw the figure of squares.

## Conclusion 🚀

This program demonstrates how to use Python's Turtle graphics module to create a figure with multiple squares.
It shows how to rotate shapes to create complex designs and how to manipulate the turtle's movement for pattern creation.
