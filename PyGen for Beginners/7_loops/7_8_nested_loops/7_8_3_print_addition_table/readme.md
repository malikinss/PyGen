# Addition Table Printer (From 1 to n)

## Description 📝

This program prints an addition table for all numbers from 1 to \( n \) (inclusive), where \( n \leq 9 \). For each number \( i \) from 1 to \( n \), it displays the results of adding \( i \) to each number from 1 to 9.

## Purpose 🎯

To generate an addition table where the program outputs sums for numbers 1 through \( n \) added to the numbers 1 through 9. The results are printed in a readable format with each sum displayed in the form: "i + j = result".

## How It Works 🔍

1. The program prompts the user to input a natural number \( n \) (such that \( n \leq 9 \)).
2. It loops through numbers from 1 to \( n \), and for each number \( i \), it prints the addition of \( i \) with each number from 1 to 9.
3. After printing the addition results for each number \( i \), a blank line is printed to separate the results for different rows.

### Example

```bash
Input: 3

Output:
1 + 1 = 2
1 + 2 = 3
1 + 3 = 4
1 + 4 = 5
1 + 5 = 6
1 + 6 = 7
1 + 7 = 8
1 + 8 = 9
1 + 9 = 10

2 + 1 = 3
2 + 2 = 4
2 + 3 = 5
2 + 4 = 6
2 + 5 = 7
2 + 6 = 8
2 + 7 = 9
2 + 8 = 10
2 + 9 = 11

3 + 1 = 4
3 + 2 = 5
3 + 3 = 6
3 + 4 = 7
3 + 5 = 8
3 + 6 = 9
3 + 7 = 10
3 + 8 = 11
3 + 9 = 12

```

In this case:

-   The program prints the addition table for numbers from 1 to 3, where each row shows sums of the form "i + j = result" for \( j \) from 1 to 9.

## Output 📜

The program outputs the addition table for all numbers from 1 to \( n \), where each row contains sums of the form "i + j = result".
Each row corresponds to a different \( i \), and the numbers 1 to 9 are added to \( i \).

## Usage 📦

1. Run the script in a Python environment.
2. Enter a natural number \( n \) (with \( n \leq 9 \)).
3. The program will print an addition table from 1 to \( n \), showing all sums of the form "i + j = result".

### Example Usage

1. Run the script.
2. Input: `n = 3`.
3. Output:

    ```bash
    1 + 1 = 2
    1 + 2 = 3
    1 + 3 = 4
    1 + 4 = 5
    1 + 5 = 6
    1 + 6 = 7
    1 + 7 = 8
    1 + 8 = 9
    1 + 9 = 10

    2 + 1 = 3
    2 + 2 = 4
    2 + 3 = 5
    2 + 4 = 6
    2 + 5 = 7
    2 + 6 = 8
    2 + 7 = 9
    2 + 8 = 10
    2 + 9 = 11

    3 + 1 = 4
    3 + 2 = 5
    3 + 3 = 6
    3 + 4 = 7
    3 + 5 = 8
    3 + 6 = 9
    3 + 7 = 10
    3 + 8 = 11
    3 + 9 = 12
    ```

## Conclusion 🚀

This program generates a simple addition table for numbers from 1 to \( n \).
It helps users quickly see the addition results for a range of numbers and is a good exercise for understanding loops and formatted output in Python.
