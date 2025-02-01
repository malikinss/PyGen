# Drawing a Rectangle with Dots at Each Corner

## Description 📝

This Python program uses the Turtle graphics module to draw a rectangle with dots placed at each of its four corners. The function `draw_rectangle_with_dots(width, height, dot_size)` draws a rectangle and adds a dot at every corner. The size of the rectangle and dots can be customized.

## Purpose 🎯

The purpose of this program is to demonstrate how to draw a rectangle with Turtle graphics and add custom markers (dots) at the corners. It showcases how to use basic Turtle commands to create shapes and add additional graphical elements.

## How It Works 🔍

1. **Drawing the Rectangle**:
    - The program first draws the top side of the rectangle, followed by a side, while placing dots at the corners after each side.
2. **Dot Placement**:
    - After drawing each side of the rectangle, a dot is placed at the corner using `turtle.dot(dot_size)`.
3. **Turning and Repeating**:
    - The turtle turns 90 degrees after drawing each side to complete the rectangle, placing dots at each corner.

## Output 📜

The program will display a rectangle on the Turtle graphics window. There will be a dot placed at each corner of the rectangle. The width, height, and dot size can be customized through the function parameters.

### Example:

For the input:

```

width = 100
height = 50
dot_size = 10

```

The output will be a rectangle of width 100 and height 50, with dots at each of the four corners.

## Usage 📦

1. Save the code in a file, e.g., `rectangle_with_dots.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python rectangle_with_dots.py`
5. The program will open a Turtle graphics window and draw the rectangle with dots at the corners.

## Conclusion 🚀

This program demonstrates the basics of drawing shapes using Turtle graphics and how to add additional elements, such as dots, to enhance the visual representation. You can customize the dimensions of the rectangle and the size of the dots to suit your needs.

```

```
