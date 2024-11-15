# Number Triangle Printer

## Description 📝

This program prints a number triangle where each row contains numbers increasing from 1 up to the row number, and then decreasing back to 1.
The height of the triangle is determined by the input natural number \(n\).

## Purpose 🎯

To print a number triangle with a specific height, where each row \(i\) contains numbers that first increase from 1 to \(i\) and then decrease back to 1.

### Example

```bash
Input: 5
Output: 1
        121
        12321
        1234321
        123454321
```

In this case:

-   The first row contains only the number 1.
-   The second row contains the numbers 1, 2, and then back to 1.
-   The third row contains the numbers 1, 2, 3, 2, and 1.
-   The fourth row contains the numbers 1, 2, 3, 4, 3, 2, and 1.
-   The fifth row contains the numbers 1, 2, 3, 4, 5, 4, 3, 2, and 1.

## How It Works 🔍

1. The program accepts a natural number \(n\) as input to determine the height of the triangle.
2. For each row, it first prints increasing numbers from 1 to the current row number \(i\).
3. After reaching the middle number (which is \(i\)), it prints the decreasing numbers back down to 1.
4. The pattern is printed row by row, starting from 1 up to the input \(n\).

## Output 📜

The program prints a number triangle based on the value of \(n\).
For example:

```bash
1
121
12321
1234321
123454321
```

## Usage 📦

1. Run the Python script in your environment.
2. Input a natural number \(n\), where \(n\) is the height of the triangle.
3. The program will print the number triangle with \(n\) rows.

### Example Usage

1. Run the script.
2. Input: `n = 5`.
3. Output:

```bash
1
121
12321
1234321
123454321
```

## Conclusion 🚀

This program demonstrates how to create a number triangle by using nested loops, which is useful for practicing loop constructs and understanding how to manage sequences and symmetry in Python.
