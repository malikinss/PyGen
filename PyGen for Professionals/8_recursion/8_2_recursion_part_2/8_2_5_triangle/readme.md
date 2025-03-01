# Triangle Program using Recursion 🌟

## Description 📝

This Python program uses recursion to print a star triangle with a specified height.
The program prints stars in a triangle shape, where the first row contains the maximum number of stars and each subsequent row has one less star until the last row contains a single star.

## Purpose 🎯

The purpose of this program is to demonstrate how recursion can be used to print a star triangle pattern in Python.
It takes an integer height `h` and prints the triangle in decreasing order of stars.

## How It Works 🔍

-   The `triangle()` function takes a single argument `h`, which represents the height of the triangle.
-   It prints `h` stars on the first line, then calls itself recursively with `h-1`, decreasing the number of stars in each row.
-   This process continues until `h` becomes 0, at which point the recursion stops.

## Output 📜

For an input `h = 5`, the program will output:

```
*****
****
***
**
*
```

## Usage 📦

1. Clone the repository or copy the code into a Python file.
2. Call the function `triangle(h)` where `h` is the desired height of the triangle.
3. Example usage:

```python
triangle(5)
```

4. The program will print a star triangle with the specified height.

## Conclusion 🚀

This program showcases how recursion can be applied to generate simple patterns like a star triangle.
It helps to understand the core concept of recursion and its ability to solve problems that involve repeating tasks with smaller inputs.
