# Numerical Triangle Printer

## Description 📝

This program prints a numerical triangle where each row contains the row number repeated as many times as its position in the triangle.
For example, in the first row, the number '1' is printed once, in the second row, the number '2' is printed twice, and so on, forming a triangle pattern.

## Purpose 🎯

To generate a numerical triangle pattern, where each row consists of the number corresponding to its row number, repeated that many times.
The program makes use of nested loops to generate the pattern.

## How It Works 🔍

1. The program takes a natural number \( n \) as input, which represents the number of rows in the triangle.
2. It prints a numerical triangle where the i-th row contains the number i repeated i times.
3. The outer loop iterates through the rows, and the inner loop prints the current row number repeated that many times.

### Example

```bash
Input: 5
Output: 1
        22
        333
        4444
        55555
```

In this case:

-   The first row contains '1', printed once.
-   The second row contains '2', printed twice.
-   The third row contains '3', printed three times.
-   The fourth row contains '4', printed four times.
-   The fifth row contains '5', printed five times.

## Output 📜

The program prints a numerical triangle, with each row corresponding to the row number, printed that many times.
For example:

```bash
1
22
333
4444
55555
```

## Usage 📦

1. Run the script in a Python environment.
2. Input a natural number \( n \) to specify how many rows the triangle will have.
3. The program will print the numerical triangle pattern with \( n \) rows.

### Example Usage

1. Run the script.
2. Input: `n = 5`.
3. Output:
    ```bash
    1
    22
    333
    4444
    55555
    ```

## Conclusion 🚀

This program demonstrates a simple use of nested loops to print a numerical triangle pattern.
It provides an excellent example of how loops can be used to generate repeating patterns in Python.
