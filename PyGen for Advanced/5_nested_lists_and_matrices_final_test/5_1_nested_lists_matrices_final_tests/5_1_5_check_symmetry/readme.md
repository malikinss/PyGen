# Secondary Diagonal Symmetry Checker 🔄

## Description 📝

This Python program checks if a square matrix is symmetric with respect to the **secondary diagonal**. The secondary diagonal runs from the top-right to the bottom-left of the matrix. The program reads the matrix from user input and determines if the matrix satisfies the symmetry condition.

## Purpose 🎯

-   To practice matrix manipulation and symmetry checks.
-   Demonstrates nested loops and index manipulation.
-   Provides a practical example of two-dimensional list processing.

## How It Works 🔍

1. **Function `list_convert_to_int_in_place()`**:

    - Converts all elements of a matrix row from strings to integers.

2. **Function `get_int_row()`**:

    - Reads a row of space-separated integers from the input and returns it as a list.

3. **Function `get_matrix()`**:

    - Builds the matrix by reading multiple rows from the input and storing them as a list of lists.

4. **Function `check_symmetry()`**:

    - Iterates over the matrix to check if each element is symmetric across the secondary diagonal.
    - Compares the element at `(i, j)` with the element at `(n-1-j, n-1-i)`.
    - Returns "YES" if symmetric, otherwise "NO".

5. **Function `main()`**:
    - Handles input for the matrix size and matrix elements.
    - Calls the relevant functions to process the matrix and print the result.

## Usage 📦

1. Run the script `secondary_diagonal_symmetry.py`.
2. Enter the matrix size `n` (square matrix).
3. Input the matrix row by row.

### Example:

```
3
1 2 3
4 5 6
7 8 9
```

**Output**:

```
NO
```

### Explanation:

-   The input matrix is:

```
1 2 3
4 5 6
7 8 9
```

-   The element at `(0,0)` is `1`, but the element at `(2,2)` is `9`.
-   Since these values do not match, the matrix is **not symmetric** with respect to the secondary diagonal.

### Example 2:

```
3
1 2 3
4 5 4
3 2 1
```

**Output**:

```
YES
```

-   The matrix is symmetric across the secondary diagonal.

## Output 📜

-   Prints "YES" if the matrix is symmetric with respect to the secondary diagonal.
-   Prints "NO" if the matrix is not symmetric.

## Conclusion 🚀

This program is a useful demonstration of matrix symmetry checks, allowing for quick and efficient validation of matrix properties. It reinforces skills in nested loops, list comprehensions, and index manipulation.
