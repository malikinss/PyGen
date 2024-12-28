# Star Box Drawing Program ⭐

## Description 📝

This Python program draws a rectangular box made of stars.
The box has **14 rows** and **10 columns**.
The top and bottom rows are filled with stars (`*`), while the middle rows have stars on the edges and spaces inside, forming a hollow box.

## Purpose 🎯

-   Demonstrates the use of loops and conditionals for drawing patterns in Python.
-   Reinforces basic control structures (`for` loops and `if` statements).
-   Provides a simple yet effective way to create ASCII art and visual output in the console.

## How It Works 🔍

1. **Function `draw_box`**:

    - A `for` loop iterates **14 times** to create 14 rows.
    - The first (`i == 0`) and last (`i == 13`) rows print **10 stars** (`**********`).
    - Rows in between print a star at the beginning and end, with **8 spaces** in between (`*        *`).

2. **Flow**:
    - Loop through a fixed range of 14.
    - Print full rows of stars for the first and last iterations.
    - Print stars with spaces for the middle 12 rows.

## Output 📜

The program outputs the following box to the console:

```
**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********
```

## Usage 📦

1. Copy the code into a Python file, e.g., `draw_star_box.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python draw_star_box.py
    ```
5. The box will be displayed in the console.

## Conclusion 🚀

This program is a great exercise for practicing loops and conditionals.
It highlights how simple patterns can be created with minimal code, forming the foundation for more complex ASCII art and console-based designs.
