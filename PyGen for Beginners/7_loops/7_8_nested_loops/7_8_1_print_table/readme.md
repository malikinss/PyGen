# Number Table Printer

## Description 📝

This program prints an \( n \times 3 \) table where each number in the table is the given natural number \( n \) (where \( n \leq 9 \)).
The numbers in each row are separated by a single space.

## Purpose 🎯

To generate a table of a specified size, where the number \( n \) is printed multiple times in each row and column, creating a 3-column format for a given number of rows.

## How It Works 🔍

1. The program prompts the user to input a natural number \( n \) (such that \( n \leq 9 \)).
2. It then prints \( n \) rows, each consisting of the number \( n \) repeated 3 times, separated by a single space.
3. After printing each row, the program moves to the next line.

### Example

```bash
Input: 4
Output: 4 4 4 4 4 4 4 4 4

```

In this case:

-   The program prints 4 rows, each containing the number 4 repeated 3 times.

## Output 📜

The program outputs an \( n \times 3 \) table, with each number in the table being the number \( n \), separated by spaces.

## Usage 📦

1. Run the script in a Python environment.
2. Enter a natural number \( n \leq 9 \).
3. The program will print an \( n \times 3 \) table with the number \( n \) repeated in each row.

### Example Usage

1. Run the script.
2. Input: `n = 2`.
3. Output:
    ```bash
    2 2 2
    2 2 2
    2 2 2
    ```

## Conclusion 🚀

This program demonstrates the use of nested loops to print a formatted table, based on a user-defined number, providing a simple yet effective exercise in iteration and formatting.
