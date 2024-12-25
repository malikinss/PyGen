# Generate and Print Cubes of Numbers

## Description 📝

This Python program takes a string of space-separated integers as input, computes their cubes, and prints the cubes on the same line.
The program uses list comprehension for efficient processing.

## Purpose 🎯

-   To practice using **list comprehensions** for transforming a list of values.
-   To work with **input/output** operations in Python, specifically handling strings and performing arithmetic operations on them.
-   To demonstrate how to compute cubes of numbers and print them on a single line.

## How It Works 🔍

1. **Function `generate_cubes`**:

    - Accepts a string of space-separated integers (`numbers`).
    - Splits the string into individual number strings using `split()`.
    - For each number, it converts it to an integer, computes the cube (`int(i) ** 3`), and returns a list of cubes.

2. **Function `print_cubes`**:
    - Prompts the user to input a string of space-separated integers.
    - Calls `generate_cubes` to compute the cubes of the numbers.
    - Prints the cubes using `print(*cubes)` to display all cubes on the same line. The `*` operator unpacks the list, printing each element separated by a space.

## Output 📜

The cubes of the input numbers will be printed on the same line.

**Example**:

```
Enter space-separated integers: 1 2 3 4
1 8 27 64
```

## Usage 📦

1. Copy the code into a Python file, e.g., `cubes_generator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python cubes_generator.py
    ```
5. Enter a string of space-separated integers when prompted.
6. View the cubes printed on the same line.

## Conclusion 🚀

This script demonstrates how to handle user input, process a string of numbers, and output the transformed data (cubes) in a concise and readable format.
It’s a great exercise for learning **list comprehension** and basic string manipulation in Python. 🌟
