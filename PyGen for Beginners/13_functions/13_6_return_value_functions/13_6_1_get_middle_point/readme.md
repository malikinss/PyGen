# Midpoint of a Line Segment 🎯

## Description 📝

This program calculates the midpoint of a line segment defined by two endpoints, with given coordinates.
The midpoint is the point that lies exactly halfway between the two endpoints.

## Purpose 🎯

The function `get_middle_point()` is designed to take the coordinates of the two endpoints of a line segment and return the coordinates of the midpoint.
This is useful in geometry and graphical computations.

## How It Works 🔍

1. **Function `get_middle_point(x1, y1, x2, y2)`**:
    - It takes four arguments: the coordinates of the two endpoints of a line segment `(x1, y1)` and `(x2, y2)`.
    - The midpoint is calculated using the formula:
      \[
      x*{mid} = \frac{x_1 + x_2}{2}, \quad y*{mid} = \frac{y_1 + y_2}{2}
      \]
    - The function returns a tuple `(x_mid, y_mid)` representing the midpoint coordinates.

## Usage 📦

1. Copy the code into a Python file, e.g., `midpoint_calculator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python midpoint_calculator.py
    ```
5. Enter the coordinates of the two endpoints:
    - Example:
        ```
        0
        0
        4
        4
        ```
6. The program will output the midpoint:
    ```
    2.0 2.0
    ```

## Conclusion 🚀

This program provides an easy way to calculate the midpoint of a line segment given its two endpoints.
