# Isosceles Triangle Drawer 🎨

## Description 📝

This Python script draws an isosceles triangle made of stars (`*`) with a base of 15 stars and a height of 8 rows.
The triangle is symmetrical and centered horizontally.

## Purpose 🎯

The function `draw_triangle()` demonstrates how to use loops, string manipulation, and basic geometry to draw shapes in the console. This project highlights the importance of pattern generation and formatting.

## How It Works 🔍

1. **Function `draw_triangle()`**:

    - The triangle is drawn by iterating over 8 rows (height).
    - For each row:
        - The number of stars is calculated as:
          \[
          \text{stars} = 2 \times \text{row number} - 1
          \]
        - The number of leading spaces is calculated to center the triangle:
          \[
          \text{spaces} = \frac{15 - \text{stars}}{2}
          \]
    - Each row is printed by combining spaces and stars.

2. **Visual Representation**:
    ```
          *
         ***
        *****
       *******
      *********
     ***********
    *************
    ***************
    ```

## Usage 📦

1. Copy the code into a Python file, e.g., `triangle_drawer.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python triangle_drawer.py
    ```
5. The triangle will be displayed in the console.

## Conclusion 🚀

This script is a simple yet effective demonstration of loops and geometric pattern printing in Python.
It is an excellent exercise for beginners learning about loops, conditionals, and string formatting.
