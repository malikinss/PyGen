# Pascal's Triangle Program 📝

## Description 📝

This program generates a specific row of Pascal's Triangle.
Pascal's Triangle is a triangular arrangement of binomial coefficients where each number is the sum of the two numbers directly above it.
The program takes an input number `n` and returns the nth row of Pascal's Triangle as a list.

## Purpose 🎯

The goal is to create a function that returns a specific row from Pascal's Triangle, based on the given row index `n`.

## How It Works 🔍

1. **Input**: The program accepts an integer `n`, which represents the row number (starting from 0) of Pascal's Triangle that you want to retrieve.
2. **Logic**:

    - The first row (row 0) is `[1]`.
    - Each subsequent row is built by adding the two numbers above each position.
      The first and last elements of each row are always `1`.
    - The program constructs each row by iterating through the previous row, adding adjacent elements, and then inserting `1` at the beginning of the row.

3. **Output**: The program prints the `n`th row of Pascal's Triangle.

### Example:

For `n = 4`, the input and output will look like this:

**Input**:

```plaintext
4
```

**Output**:

```plaintext
[1, 4, 6, 4, 1]
```

This means the program has returned the 4th row of Pascal's Triangle.

## Usage 📦

1. Copy the code into a Python file, e.g., `pascal_triangle.py`.
2. Run the script in the terminal:
    ```bash
    python pascal_triangle.py
    ```
3. Enter a number `n` when prompted.
4. The program will output the `n`th row of Pascal's Triangle.

## Conclusion 🚀

This program efficiently computes the nth row of Pascal's Triangle using a simple iterative approach.
It highlights how binomial coefficients work in a triangular structure, and is useful in combinatorics and probability theory.
