# Matrix Multiplication Program 🧮

## Description 📝

This Python program multiplies two matrices. It takes the dimensions and elements of two matrices as input from the user, performs matrix multiplication, and outputs the resulting matrix.

## Purpose 🎯

-   To perform matrix multiplication, a key operation in linear algebra.
-   Matrix multiplication is used in graphics, physics simulations, neural networks, and various scientific computations.

## How It Works 🔍

1. **Function `get_matrix_size()`**:

    - Prompts the user to input the number of rows and columns of a matrix.

2. **Function `get_int_row()` and `list_convert_to_int_in_place()`**:

    - Reads and converts each row of matrix elements from strings to integers.

3. **Function `get_matrix()`**:

    - Reads the entire matrix row by row from the user.

4. **Function `matrix_multiplication()`**:

    - Multiplies two matrices by iterating through rows of the first matrix and columns of the second matrix.
    - The dot product is computed for each element of the resulting matrix.

5. **Function `print_matrix()`**:

    - Prints the resulting matrix in a readable format.

6. **Main Execution Flow**:
    - Matrix sizes and elements are collected.
    - Matrix compatibility for multiplication is checked (columns of the first matrix must equal rows of the second matrix).
    - If valid, matrix multiplication is performed, and the result is printed.

## Usage 📦

1. Run the Python script `matrix_multiplication.py`.
2. Enter the number of rows and columns for the first matrix.
3. Input the elements of the first matrix row by row.
4. Enter the number of rows and columns for the second matrix.
5. Input the elements of the second matrix row by row.
6. The program will calculate and display the resulting matrix.

## Output 📜

-   If matrix multiplication is possible, the program prints the resulting matrix.
-   If matrix dimensions are incompatible, an error message is displayed:
    ```
    Matrix multiplication is not possible.
    Columns of matrix 1 must equal rows of matrix 2.
    ```

## Conclusion 🚀

This program provides an intuitive way to perform matrix multiplication, demonstrating essential programming concepts like nested loops, user input handling, and mathematical operations.
It serves as a useful tool for students, developers, and engineers working with matrices.
