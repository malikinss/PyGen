# Maximum Element to the Left of the Main Diagonal Program 📝

## Description 📝

This program finds the maximum element to the left of the main diagonal of a square matrix, including the diagonal itself.
The program first reads the matrix from user input and then computes and prints the maximum element found to the left of the main diagonal.

## Purpose 🎯

The purpose of this program is to analyze the elements in the square matrix that are positioned to the left of the main diagonal (including the diagonal itself) and determine the maximum value among them.

## How It Works 🔍

1. **Input**:

    - The program first reads an integer `n`, which represents the size of the square matrix (i.e., the number of rows and columns).
    - The following `n` lines contain `n` space-separated integers, representing the rows of the matrix.

2. **Analysis**:

    - The program iterates over the matrix, focusing on the elements that are on the main diagonal and to the left of it.
    - For each row `i`, it checks the elements from column `0` to `i` (inclusive) and keeps track of the maximum value found.

3. **Output**:
    - The program prints the maximum value found among the elements to the left of the main diagonal, including the diagonal itself.

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
5
```

**Explanation:**

-   The elements to the left of the main diagonal (including the diagonal itself) are:
    -   From row 1: [1]
    -   From row 2: [4, 5]
    -   From row 3: [7, 8, 9]
-   The maximum value among these elements is 5.

## Usage 📦

1. Copy the code into a Python file (e.g., `max_left_diagonal.py`).
2. Run the script:
    ```bash
    python max_left_diagonal.py
    ```
3. Enter the size of the matrix (`n`) followed by the elements of the matrix.

## Conclusion 🚀

This program allows you to analyze the elements of a square matrix to find the maximum value from those that are to the left of the main diagonal, providing a simple approach to matrix manipulation and element comparison.
