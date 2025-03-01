# Star Triangle Program using Recursion 🌟

## Description 📝

This Python program uses recursion to print a star triangle with a specified height.
The triangle is printed with stars (`*`), where the number of stars increases as we move down from top to bottom.
The program takes an integer `h`, which represents the height of the triangle, and prints the triangle line by line.

## Purpose 🎯

The goal of this program is to demonstrate the use of recursion in generating a triangle pattern.
The function recursively calls itself to print each line of stars, starting from 1 star at the top and increasing by 1 star on each subsequent line.

## How It Works 🔍

-   The `triangle()` function takes one argument `h`, which represents the height of the triangle.
-   The function calls an internal helper function `print_triangle_lines()`, which prints each line of the triangle by using recursion.
-   For each line, the function decreases the current height until it reaches the base case where the height is 0, and then prints the stars.

## Output 📜

For an input `h = 5`, the program will output:

```
*
**
***
****
*****
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

This program demonstrates how recursion can be used to solve problems involving repeated tasks that decrease in size.
It's an effective way to explore the basics of recursion and pattern generation using simple techniques.
