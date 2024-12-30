# Matrix Trace Program 📝

## Description 📝

This program calculates and outputs the trace of a given square matrix.
The trace of a matrix is the sum of the elements on the main diagonal, where the main diagonal consists of elements where the row and column indices are the same (i.e., `matrix[i][i]`).

## Purpose 🎯

The purpose of this program is to compute the trace of a square matrix.
The trace is used in various areas of mathematics, including linear algebra and matrix theory, and is important for understanding matrix properties.

## How It Works 🔍

1. **Input**:
    - The program first reads an integer `n`, representing the size of the square matrix.
    - The next `n` lines contain space-separated integers representing the rows of the matrix.
2. **Matrix Construction**:
    - The matrix is constructed by reading the values into a list of lists, where each inner list represents a row of the matrix.
3. **Trace Calculation**:

    - The trace is computed by summing the diagonal elements, which are the elements where the row and column indices are equal.

4. **Output**:
    - The program outputs the calculated trace of the matrix.

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
15
```

**Explanation:**

-   The matrix is:
    ```
    1 2 3
    4 5 6
    7 8 9
    ```
-   The diagonal elements are 1, 5, and 9.
-   The trace is the sum of these elements: 1 + 5 + 9 = 15.

## Usage 📦

1. Copy the code into a Python file (e.g., `matrix_trace.py`).
2. Run the script:
    ```bash
    python matrix_trace.py
    ```
3. Enter the size of the matrix (`n`) followed by the elements of the matrix.

## Conclusion 🚀

This program demonstrates a straightforward method for calculating the trace of a square matrix using Python's list comprehensions and basic matrix manipulation techniques.
