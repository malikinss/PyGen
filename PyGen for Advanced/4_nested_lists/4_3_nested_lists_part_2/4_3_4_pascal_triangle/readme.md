# Pascal's Triangle Generator 📝

## Description 📝

This program generates and outputs the first `n` rows of Pascal's Triangle.
Pascal's Triangle is a triangular array of binomial coefficients where each number is the sum of the two numbers directly above it.
The program constructs and prints each row of the triangle, with the first and last elements of each row being `1`.

## Purpose 🎯

The purpose of this program is to create Pascal's Triangle up to the specified row number `n` and display each row in a separate line.

## How It Works 🔍

1. **Input**: The program takes an integer `n` as input, representing the number of rows of Pascal's Triangle to generate.
2. **Logic**:
    - The first row is always `[1]`.
    - Each subsequent row is constructed by filling the boundary elements with `1` and calculating the intermediate elements as the sum of the two elements directly above them from the previous row.
3. **Output**: The program prints the first `n` rows of Pascal's Triangle, one row per line.

### Example:

For `n = 5`, the input and output will look like this:

**Input**:

```plaintext
5
```

**Output**:

```plaintext
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```

This means the program has returned the first 5 rows of Pascal's Triangle.

## Usage 📦

1. Copy the code into a Python file, e.g., `generate_pascal_triangle.py`.
2. Run the script in the terminal:
    ```bash
    python generate_pascal_triangle.py
    ```
3. Enter a number `n` when prompted.
4. The program will output the first `n` rows of Pascal's Triangle.

## Conclusion 🚀

This program successfully generates Pascal's Triangle up to a specified number of rows and demonstrates the fundamental properties of binomial coefficients.
It is useful for understanding combinatorial mathematics and can be extended for various other applications in probability theory.
