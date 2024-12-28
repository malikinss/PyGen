# Right Triangle Drawing Program ⭐

## Description 📝

This Python program draws a right triangle made of stars (`*`).
The triangle has **10 rows**, with the first row containing 1 star, the second row containing 2 stars, and so on, until the 10th row which contains 10 stars.
The shape formed is a right triangle where both legs have a length of 10.

## Purpose 🎯

-   Demonstrates the use of loops and list comprehensions for drawing patterns in Python.
-   Provides a way to generate and display simple geometric shapes using ASCII art.
-   A practical example of list manipulation and the `print()` function to format output.

## How It Works 🔍

1. **Function `draw_triangle`**:

    - A list comprehension is used to generate strings of stars for each row.
    - The range from 1 to 10 is used to create the increasing number of stars.
    - The `sep='\n'` argument in `print()` ensures that each row of stars is printed on a new line.

2. **Flow**:
    - The program iterates through the range `1 to 10` and for each value of `i`, it prints `i` stars.
    - The rows are printed one by one, resulting in a triangle shape.

## Output 📜

The program outputs the following triangle to the console:

```
*
**
***
****
*****
******
*******
********
*********
**********
```

## Usage 📦

1. Copy the code into a Python file, e.g., `draw_star_triangle.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python draw_star_triangle.py
    ```
5. The triangle will be displayed in the console.

## Conclusion 🚀

This program provides a simple yet effective way to create ASCII art, demonstrating how loops and list comprehensions can be used together to generate visually appealing patterns.
It can be a foundation for more complex pattern generation tasks in Python.
