# Drawing Nested Squares

## Description 📝

This Python program uses the Turtle graphics module to draw a series of nested squares. The function `draw_nested_squares(initial_side, step)` creates a pattern where each square has a side length reduced by a specified step after drawing each square.

## Purpose 🎯

The purpose of this program is to create a visually appealing pattern of nested squares, each smaller than the previous one. This demonstrates how to use loops and Turtle graphics to create geometric patterns.

## How It Works 🔍

1. **Drawing a Single Square**:
    - The `draw_square(side)` function draws one square by moving forward by the given side length and turning 90 degrees to form the corners.
2. **Nested Squares**:

    - The `draw_nested_squares(initial_side, step)` function starts with an initial square of the given size and then draws subsequent squares with a side length reduced by the specified `step`.

3. **Loop and Reduction**:
    - A loop is used to draw a total of 9 squares, reducing the side length by `step` for each new square.

## Output 📜

The program will display a pattern of 9 nested squares, with each square smaller than the last by the given step value.

### Example:

For the input:

```
initial_side = 100
step = 10
```

The output will be a series of 9 nested squares, where each square’s side length decreases by 10 pixels.

## Usage 📦

1. Save the code in a file, e.g., `nested_squares.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python nested_squares.py`
5. The program will open a Turtle graphics window and draw the pattern of nested squares.

## Conclusion 🚀

This program demonstrates how to create a series of nested geometric shapes using Python's Turtle graphics. By adjusting the side length of each square, a visually engaging pattern is formed.
