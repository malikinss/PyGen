# Drawing a Spiral of Rectangles

## Description 📝

This Python program uses the Turtle graphics module to draw a spiral pattern made up of rectangles. The function `draw_spiral(initial_side, step)` creates the spiral by drawing rectangles, with each subsequent rectangle having a side length reduced by a specified step.

## Purpose 🎯

The purpose of this program is to create a visually engaging spiral pattern, where the rectangles become progressively smaller. It demonstrates the use of loops, geometric shapes, and Turtle graphics to create intricate designs.

## How It Works 🔍

1. **Drawing a Single Rectangle**:
    - The `draw_rectangle(side)` function draws one rectangle by moving forward by the given side length and turning 90 degrees twice to form the corners.
2. **Spiral Pattern**:

    - The `draw_spiral(initial_side, step)` function starts with a large rectangle of the given `initial_side` length and then draws subsequent rectangles with a side length reduced by the specified `step` value.

3. **Loop and Reduction**:
    - A `while` loop is used to repeatedly draw rectangles, decreasing the side length by `step` after each rectangle is drawn until the side length becomes 0 or negative.

## Output 📜

The program will display a spiral pattern of rectangles. Each rectangle will be smaller than the previous one by the given `step`.

### Example:

For the input:

```
initial_side = 150
step = 10
```

The output will be a spiral pattern of rectangles, with each rectangle’s side length decreasing by 10 pixels after each one.

## Usage 📦

1. Save the code in a file, e.g., `spiral_rectangles.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python spiral_rectangles.py`
5. The program will open a Turtle graphics window and draw the spiral pattern.

## Conclusion 🚀

This program showcases how to create a dynamic and visually appealing spiral pattern using Python's Turtle graphics. It highlights the use of loops and geometric transformations to generate complex shapes from simple components.
