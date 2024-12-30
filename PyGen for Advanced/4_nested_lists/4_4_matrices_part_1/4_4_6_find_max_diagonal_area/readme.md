# Maximum Element to the Right and Left of Main and Secondary Diagonals Program 📝

## Description 📝

This program finds the maximum element in the areas to the left and right of the main and secondary diagonals of a square matrix.
The program includes the diagonal elements themselves in the computation.
The program first reads the square matrix from user input, then computes and prints the maximum element found in the specified areas.

## Purpose 🎯

The goal of this program is to identify the maximum element from the regions on the square matrix that are adjacent to the main and secondary diagonals, including the diagonal elements.

## How It Works 🔍

1. **Input**:

    - The program first reads an integer `n`, which represents the size of the square matrix (i.e., the number of rows and columns).
    - The following `n` lines contain `n` space-separated integers, representing the rows of the matrix.

2. **Analysis**:

    - The program identifies the elements that are either on or adjacent to the main diagonal (from top-left to bottom-right) and the secondary diagonal (from top-right to bottom-left).
    - For each element in the matrix, it checks if the element belongs to either diagonal or is adjacent to it. These elements are collected in a list.

3. **Output**:
    - The program finds and prints the maximum value from the selected elements.

### Example:

**Input:**

```plaintext
3
1 2 3
4 5 6
7 8 9
```

**Output:**

```plaintext
9
```

**Explanation:**

-   The elements of interest, based on the condition for diagonals and their adjacent areas, are:
    -   From row 1: [1, 2, 3]
    -   From row 2: [4, 5, 6]
    -   From row 3: [7, 8, 9]
-   The maximum value among these elements is 9.

## Usage 📦

1. Copy the code into a Python file (e.g., `max_diagonal_area.py`).
2. Run the script:
    ```bash
    python max_diagonal_area.py
    ```
3. Enter the size of the matrix (`n`) followed by the elements of the matrix.

## Conclusion 🚀

This program allows you to find the maximum element from the areas adjacent to both the main and secondary diagonals of a square matrix, offering an efficient approach to matrix element analysis and comparison.
