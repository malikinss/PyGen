# Valid Triangle Check Program 🔺

## Description 📝

This Python program takes three natural numbers representing the sides of a triangle as input and determines if those sides can form a valid (non-degenerate) triangle.
The program checks if the sides satisfy the triangle inequality theorem.

## Purpose 🎯

-   To verify whether three given sides can form a valid triangle.
-   The triangle inequality theorem ensures that the sum of any two sides of the triangle must be greater than the third side.

## How It Works 🔍

1. **Function `is_valid_triangle(side1, side2, side3)`**:

    - The function takes three sides of a triangle as input.
    - It checks if the sum of any two sides is greater than the third side, using the triangle inequality theorem.
    - If all three conditions are met, the sides can form a valid triangle, and the function returns `True`. Otherwise, it returns `False`.

2. **Example**:

    - **Input**: `side1 = 3`, `side2 = 4`, `side3 = 5`
    - **Output**: `True` (This is a valid triangle, as the sum of any two sides is greater than the third side)

    - **Input**: `side1 = 1`, `side2 = 2`, `side3 = 3`
    - **Output**: `False` (This is not a valid triangle, as 1 + 2 = 3, which is not greater than 3)

## Usage 📦

1. Copy the code into a Python file, e.g., `valid_triangle.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python valid_triangle.py
    ```
5. Input the three sides when prompted. The program will then check if they form a valid triangle and print the result.

## Conclusion 🚀

This function is a practical implementation of the triangle inequality theorem, providing an easy way to validate whether three given sides can form a non-degenerate triangle.
