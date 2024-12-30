# Multiplication Table Program 📝

## Description 📝

This program generates and prints a multiplication table of size `n x m`, where `n` is the number of rows and `m` is the number of columns.
Each element in the table is calculated using the formula `mult[i][j] = i * j`, where `i` is the row index and `j` is the column index.

## Purpose 🎯

The program demonstrates how to construct and format a multiplication table, which can be useful for various mathematical and educational applications.
The table is displayed with proper alignment for better readability.

## How It Works 🔍

1. **Input**:
    - The program first reads two integers, `n` and `m`, representing the number of rows and columns in the multiplication table.
2. **Matrix Creation**:
    - The program then creates a multiplication table of size `n x m`, where each element is calculated as `mult[i][j] = i * j`.
3. **Output**:
    - The program prints each row of the table, ensuring that the elements are properly aligned for a neat presentation.

### Example:

**Input:**

```plaintext
4
5
```

**Output:**

```plaintext
  0  0  0  0  0
  0  1  2  3  4
  0  2  4  6  8
  0  3  6  9 12
```

**Explanation:**

-   The matrix has 4 rows and 5 columns. Each element in the table is the product of its row index (`i`) and column index (`j`), where indices start from 0.
-   The element at position `[i][j]` will be equal to `i * j`.

## Usage 📦

1. Copy the code into a Python file (e.g., `multiplication_table.py`).
2. Run the script:
    ```bash
    python multiplication_table.py
    ```
3. Enter the number of rows (`n`) and columns (`m`) for the multiplication table.

## Conclusion 🚀

This program provides a simple way to generate a formatted multiplication table of any size.
It can be adapted for other mathematical tables by modifying the formula used to fill the matrix.
