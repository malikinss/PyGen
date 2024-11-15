# Number Table Printer (Size n x 5)

## Description 📝

This program prints a table of size \( n \times 5 \), where each row contains the number \( i \) (where \( 1 \leq i \leq n \)), repeated 5 times.
The numbers in each row are separated by a single space.

## Purpose 🎯

To generate a table with \( n \) rows, where each row consists of the number corresponding to the row number repeated 5 times.
The program allows a user to specify the number \( n \), where the table will have \( n \) rows.

## How It Works 🔍

1. The program prompts the user to input a natural number \( n \) (such that \( n \leq 9 \)).
2. It prints \( n \) rows. In each row, the program prints the row number \( i \) five times, separated by a space.
3. After printing each row, the program moves to the next line.

### Example

```bash
Input: 3
Output: 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3

```

In this case:

-   The program prints 3 rows, with each row containing the number corresponding to the row repeated 5 times.

## Output 📜

The program outputs an \( n \times 5 \) table, where each number is the row number, and each row contains that number repeated 5 times, separated by spaces.

## Usage 📦

1. Run the script in a Python environment.
2. Enter a natural number \( n \) (with \( n \leq 9 \)).
3. The program will print a table of size \( n \times 5 \).

### Example Usage

1. Run the script.
2. Input: `n = 4`.
3. Output:
    ```bash
    1 1 1 1 1
    2 2 2 2 2
    3 3 3 3 3
    4 4 4 4 4
    ```

## Conclusion 🚀

This program showcases the use of loops to create a table of numbers where the row number determines the values printed in each row.
It provides a simple example of formatted output and iteration.
