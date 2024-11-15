# Numerical Triangle Printer with Consecutive Numbers

## Description 📝

This program prints a numerical triangle where each row contains consecutive numbers starting from 1. Each row \(i\) contains \(i\) numbers, beginning from the last number printed in the previous row. The triangle grows as the rows increase.

## Purpose 🎯

To generate a numerical triangle pattern, where each row contains consecutive numbers starting from 1. This program makes use of nested loops and a counter to increment the numbers in each row.

## How It Works 🔍

1. The program takes a natural number \(n\) as input, which specifies how many rows the triangle will have.
2. The program then prints the numbers starting from 1, arranging them in a triangle shape. Each row \(i\) contains \(i\) numbers.
3. The outer loop controls the number of rows, and the inner loop prints the consecutive numbers for each row.

### Example

```bash
Input: 5
Output: 1
        2 3
        4 5 6
        7 8 9 10
        11 12 13 14 15
```

In this case:

-   The first row contains the number 1.
-   The second row contains the numbers 2 and 3.
-   The third row contains the numbers 4, 5, and 6.
-   The fourth row contains the numbers 7, 8, 9, and 10.
-   The fifth row contains the numbers 11, 12, 13, 14, and 15.

## Output 📜

The program prints a numerical triangle, with each row containing consecutive numbers.
For example:

```bash
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

## Usage 📦

1. Run the script in a Python environment.
2. Input a natural number \(n\) to specify how many rows the triangle will have.
3. The program will print the numerical triangle pattern with \(n\) rows.

### Example Usage

1. Run the script.
2. Input: `n = 5`.
3. Output:

```bash
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
```

## Conclusion 🚀

This program demonstrates how to use nested loops to generate a pattern of consecutive numbers arranged in a triangle shape.
It's a great exercise for understanding how to work with loops and incrementing counters in Python.
