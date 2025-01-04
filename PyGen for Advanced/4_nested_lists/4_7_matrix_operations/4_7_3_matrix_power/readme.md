# Matrix Power Program 🔢

## Description 📝

This Python program raises a square matrix to the power of `m` as specified by the user. The program reads matrix dimensions and elements from input, computes the matrix raised to the desired power, and outputs the resulting matrix.

## Purpose 🎯

-   Perform matrix exponentiation, a crucial operation in linear algebra and computational mathematics.
-   Matrix exponentiation is used in solving recurrence relations, graph theory, and dynamic systems.

## How It Works 🔍

1. **Function `get_matrix_size()`**:

    - Reads the size (number of rows/columns) of a square matrix from user input.

2. **Function `get_matrix()` and `read_matrix_row()`**:

    - Collects the matrix by reading rows and converting them to integers.

3. **Function `matrix_multiplication()`**:

    - Multiplies two square matrices using the standard dot product formula.

4. **Function `matrix_power()`**:

    - Uses an efficient **exponentiation by squaring** method to raise the matrix to the specified power.
    - The matrix is repeatedly squared and multiplied as necessary to achieve the desired degree.

5. **Function `print_matrix()`**:

    - Prints the matrix row by row in a readable format.

6. **Main Execution Flow**:
    - The program reads the matrix size and matrix elements.
    - The user inputs the power to which the matrix should be raised.
    - The program computes the matrix raised to the desired power and prints the result.

## Usage 📦

1. Run the Python script `matrix_power.py`.
2. Enter the size of the square matrix.
3. Input matrix rows, with space-separated integers.
4. Enter the power to which the matrix should be raised.
5. The resulting matrix will be displayed.

### Example:

```
Enter matrix size: 2
Enter matrix row: 1 2
Enter matrix row: 3 4
Enter matrix power: 3
Resulting matrix:
37 54
81 118
```

## Output 📜

-   If the matrix is successfully exponentiated, the resulting matrix is printed.
-   The program handles matrix exponentiation efficiently even for high powers using the squaring method.

## Conclusion 🚀

This program provides an optimized solution for matrix exponentiation, demonstrating core programming techniques such as recursion, matrix operations, and algorithm optimization. It is an essential tool for mathematicians, engineers, and developers working with matrix operations.
