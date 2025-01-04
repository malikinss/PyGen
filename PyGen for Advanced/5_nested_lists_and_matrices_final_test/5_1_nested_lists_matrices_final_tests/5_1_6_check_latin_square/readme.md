# Latin Square Checker 🔍

## Description 📝

This program checks whether a given square matrix is a Latin square.
A Latin square of order `n` is a `n*n` matrix where each row and column contains all the integers from 1 to `n` exactly once.

## Purpose 🎯

-   Verify if a given square matrix is a valid Latin square.
-   Implement matrix manipulation techniques like checking rows and columns for specific conditions.

## How It Works 🔍

1. **Function `list_convert_to_int_in_place()`**:

    - Converts a row of string values into integers in place.

2. **Function `get_int_row()`**:

    - Reads a row of space-separated integers from input and converts it using `list_convert_to_int_in_place()`.

3. **Function `get_matrix()`**:

    - Reads the entire square matrix from user input row by row.

4. **Function `get_row_from_matrix()`**:

    - Retrieves a specific row from the matrix.

5. **Function `get_column_as_row_from_matrix()`**:

    - Retrieves a specific column from the matrix as a list.

6. **Function `check_row()`**:

    - Checks if a given row contains all integers from 1 to `n` in any order.

7. **Function `check_all_rows()`**:

    - Verifies if all rows in the matrix are valid for a Latin square.

8. **Function `check_all_columns()`**:

    - Verifies if all columns in the matrix are valid for a Latin square.

9. **Function `check_latin_square()`**:

    - Combines row and column checks to determine if the matrix is a Latin square.

10. **Function `main()`**:
    - Reads the matrix size and data from user input.
    - Checks if the matrix is a Latin square and prints "YES" or "NO".

## Usage 📦

1. Run the script `latin_square_checker.py`.
2. Input the size of the matrix (`n`).
3. Input `n` rows, each containing `n` space-separated integers.
4. The program will print "YES" if the matrix is a Latin square, otherwise "NO".

### Example:

```
3
1 2 3
2 3 1
3 1 2
```

**Output**:

```
YES
```

### Explanation:

-   The matrix is a 3x3 Latin square:

```
1 2 3
2 3 1
3 1 2
```

## Output 📜

-   "YES" if the matrix is a valid Latin square.
-   "NO" if the matrix is not a valid Latin square.

## Conclusion 🚀

This program helps to verify whether a given matrix follows the properties of a Latin square.
It efficiently checks both rows and columns, ensuring that each contains all the numbers from 1 to `n` exactly once.
