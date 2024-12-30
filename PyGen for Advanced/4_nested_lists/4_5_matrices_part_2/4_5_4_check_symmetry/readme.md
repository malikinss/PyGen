# Symmetry Check for Square Matrix Program 📝

## Description 📝

This program checks whether a given square matrix is symmetric about its main diagonal.
A matrix is symmetric about its main diagonal if the element at position (i, j) is equal to the element at position (j, i) for all i, j in the matrix.

## Purpose 🎯

The program is designed to check the symmetry of a square matrix.
This is useful in various fields, such as linear algebra, image processing, and physics, where symmetry plays a key role.

## How It Works 🔍

1. **Input**:

    - The program first reads the size `n` of the square matrix.
    - It then reads `n` rows of the matrix, with each row containing `n` integers.

2. **Symmetry Check**:

    - The program iterates through the upper triangle of the matrix (from left to right, top to bottom) and checks if the element at position (i, j) is equal to the element at position (j, i).
    - If any discrepancy is found, the matrix is not symmetric.

3. **Output**:
    - If the matrix is symmetric, the program prints `YES`.
    - Otherwise, it prints `NO`.

### Example:

**Input:**

```plaintext
3
1 2 3
2 4 5
3 5 6
```

**Output:**

```plaintext
YES
```

**Explanation:**

-   The matrix is symmetric because `matrix[0][1] == matrix[1][0]`, `matrix[0][2] == matrix[2][0]`, and `matrix[1][2] == matrix[2][1]`.

**Example of a non-symmetric matrix:**

**Input:**

```plaintext
3
1 2 3
4 5 6
7 8 9
```

**Output:**

```plaintext
NO
```

**Explanation:**

-   The matrix is not symmetric because `matrix[0][1] != matrix[1][0]` and `matrix[1][2] != matrix[2][1]`.

## Usage 📦

1. Copy the code into a Python file (e.g., `check_symmetry.py`).
2. Run the script:
    ```bash
    python check_symmetry.py
    ```
3. Enter the number of rows/columns (`n`), followed by the matrix elements (one row at a time).

## Conclusion 🚀

This program provides an efficient way to check if a square matrix is symmetric about its main diagonal.
This is a common operation in mathematical computations and can be extended to other types of symmetry checks.
