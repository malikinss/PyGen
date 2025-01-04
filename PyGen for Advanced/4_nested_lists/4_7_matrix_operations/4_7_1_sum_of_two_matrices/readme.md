# Matrix Sum Program 🧮

## Description 📝

This Python program calculates the sum of two matrices of the same size.
It reads the size of the matrices and their elements from the user, then computes the resulting matrix by adding corresponding elements from both matrices.

## Purpose 🎯

-   To provide a tool for summing two matrices element by element.
-   This function is useful in various fields such as linear algebra, computer graphics, and data analysis where matrix operations are required.

## How It Works 🔍

1. **Function `get_matrix_size()`**:

    - Prompts the user to input the number of rows and columns for the matrices.

2. **Function `get_int_row()` and `list_convert_to_int_in_place()`**:

    - Reads a row of integers from the user input and converts the string elements to integers.

3. **Function `get_matrix()`**:

    - Reads the entire matrix from the user by calling the above helper functions for each row.

4. **Function `sum_of_two_matrices()`**:

    - Adds the corresponding elements of the two input matrices and returns the resulting matrix.

5. **Function `print_matrix()`**:
    - Prints the resulting matrix row by row.

## Usage 📦

1. Run the Python script `matrix_sum.py`.
2. Enter the number of rows and columns when prompted.
3. Enter the elements of the first matrix.
4. After pressing "Enter," input the elements of the second matrix.
5. The program will then output the sum of the two matrices.

## Conclusion 🚀

This program provides a simple and effective way to sum two matrices, which can be useful in numerous mathematical and scientific applications.
