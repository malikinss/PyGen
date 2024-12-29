# Points in Quadrants Program 🗺️

## Description 📝

This program takes a set of points on a coordinate plane and counts how many points lie in each of the four coordinate quadrants.
It excludes points that lie on the coordinate axes (where either `x = 0` or `y = 0`).

## Purpose 🎯

The goal is to count and print the number of points in each quadrant of the Cartesian coordinate plane:

1. **First quadrant (Q1)**: Both x and y are positive.
2. **Second quadrant (Q2)**: x is negative, y is positive.
3. **Third quadrant (Q3)**: Both x and y are negative.
4. **Fourth quadrant (Q4)**: x is positive, y is negative.

Points that lie on the axes (where either x or y is zero) are not assigned to any quadrant.

## How It Works 🔍

1. **Input Format**:

    - The program first reads an integer `n`, the number of points.
    - Then, it reads `n` pairs of integers, where each pair represents the coordinates `(x, y)` of a point.

2. **Logic**:

    - The program iterates through each point and checks its coordinates:
        - If both `x` and `y` are positive, the point is in the **First quadrant**.
        - If `x` is negative and `y` is positive, the point is in the **Second quadrant**.
        - If both `x` and `y` are negative, the point is in the **Third quadrant**.
        - If `x` is positive and `y` is negative, the point is in the **Fourth quadrant**.
    - Points lying on the axes (where either `x = 0` or `y = 0`) are excluded from counting.

3. **Example**:

    - **Input**:
        ```
        5
        1 2
        -3 4
        -1 -1
        2 -3
        0 2
        ```
    - **Output**:
        ```
        First quarter: 2
        Second quarter: 1
        Third quarter: 1
        Fourth quarter: 1
        ```
    - **Explanation**: The points (1, 2), (-3, 4), (-1, -1), and (2, -3) are counted in the respective quadrants, while the point (0, 2) is ignored as it lies on the axis.

4. **Edge Cases**:
    - Points on the axes (x = 0 or y = 0) are not counted.
    - The program works with any number of points and will correctly categorize each one into its respective quadrant or ignore axis points.

## Usage 📦

1. Copy the code into a Python file, e.g., `quadrant_counter.py`.
2. Run the script in the terminal:
    ```bash
    python quadrant_counter.py
    ```
3. Enter the number of points `n` and then provide the coordinates for each point.
4. The program will output the number of points in each quadrant.

## Conclusion 🚀

This program provides a simple yet efficient way to classify points on a coordinate plane into their respective quadrants, ignoring points on the axes.
It's a useful tool for anyone working with coordinate geometry or related fields.
