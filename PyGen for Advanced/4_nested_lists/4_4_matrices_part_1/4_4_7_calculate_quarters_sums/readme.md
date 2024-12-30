# Matrix Quarters Sum Program 📝

## Description 📝

This program calculates the sum of the elements in the four quarters of a square matrix.
The matrix is divided into four regions based on the main and secondary diagonals:

1. **Upper Quarter**: Above the main diagonal and to the left of the secondary diagonal.
2. **Right Quarter**: Above the main diagonal and to the right of the secondary diagonal.
3. **Lower Quarter**: Below the main diagonal and to the left of the secondary diagonal.
4. **Left Quarter**: Below the main diagonal and to the right of the secondary diagonal.

The program computes the sums of these quarters and prints them.

## Purpose 🎯

The goal of this program is to partition a square matrix into four quarters and calculate the sum of the elements in each quarter.
This provides a better understanding of matrix partitioning and summing specific regions based on diagonal boundaries.

## How It Works 🔍

1. **Input**:

    - The program first reads an integer `n`, which represents the size of the square matrix (i.e., the number of rows and columns).
    - The following `n` lines contain `n` space-separated integers, representing the rows of the matrix.

2. **Analysis**:
    - The matrix is divided into four quarters based on the main and secondary diagonals:
        - **Upper Quarter**: The elements that lie above the main diagonal and left of the secondary diagonal.
        - **Right Quarter**: The elements that lie above the main diagonal and right of the secondary diagonal.
        - **Lower Quarter**: The elements that lie below the main diagonal and left of the secondary diagonal.
        - **Left Quarter**: The elements that lie below the main diagonal and right of the secondary diagonal.
3. **Sum Calculation**:
    - For each of the quarters, the program sums the elements within that region.
4. **Output**:
    - The program prints the sum of elements in each of the four quarters.

### Example:

**Input:**

```plaintext
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
```

**Output:**

```plaintext
upper quarter: 3
right quarter: 12
lower quarter: 34
left quarter: 24
```

**Explanation:**

-   The matrix is divided into quarters based on the diagonals:
    -   **Upper Quarter**: Elements [1, 2], sum = 3
    -   **Right Quarter**: Elements [3, 4], sum = 12
    -   **Lower Quarter**: Elements [9, 10, 11, 12], sum = 34
    -   **Left Quarter**: Elements [5, 6, 7, 8], sum = 24

## Usage 📦

1. Copy the code into a Python file (e.g., `matrix_quarters_sum.py`).
2. Run the script:
    ```bash
    python matrix_quarters_sum.py
    ```
3. Enter the size of the matrix (`n`) followed by the elements of the matrix.

## Conclusion 🚀

This program helps to understand how a square matrix can be partitioned into quarters based on the diagonals and how to compute the sums of these regions efficiently.
