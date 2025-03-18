# Chessboard Squares in Alphabetical Order

## Description 📝

The `print_chessboard_squares()` function generates and prints all squares of a chessboard (from a1 to h8) in alphabetical order.
It uses the `product()` function from the `itertools` module to generate all combinations of chessboard rows (letters) and columns (digits).

## Purpose 🎯

This function provides a systematic way to generate and print all squares of a chessboard in the desired format.
It helps in scenarios where you need a list of all possible chessboard squares for games or simulations.

## How It Works 🔍

-   **Using `product()`**: The `product()` function from `itertools` generates all possible combinations of the provided sequences (letters and digits).
    -   The `letters` sequence represents the columns (a-h) of the chessboard.
    -   The `digits` sequence represents the rows (1-8).
-   **Printing**: The function iterates over the resulting combinations and prints each chessboard square in the format `a1`, `a2`, ..., `h8`.

## Output 📜

Example usage:

```python
print_chessboard_squares()
# Output: a1 a2 a3 a4 a5 a6 a7 a8 b1 b2 ... h8
```

## Usage 📦

1. Save the function in a Python file, e.g., `chessboard.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the function:
    ```python
    from chessboard import print_chessboard_squares
    print_chessboard_squares()  # Output: a1 a2 a3 a4 a5 a6 a7 a8 b1 b2 ... h8
    ```

## Conclusion 🚀

The `print_chessboard_squares()` function provides an efficient solution for generating and printing all chessboard squares in alphabetical order.
It demonstrates the power of `product()` for generating combinations in Python.
