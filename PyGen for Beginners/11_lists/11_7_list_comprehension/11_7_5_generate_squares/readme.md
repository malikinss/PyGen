# Generate and Print Squares of Numbers

## Description 📝

This Python script generates a list of squares of numbers from `1` to `n` (inclusive), where `n` is a user-provided natural number.
It then prints each square on a separate line.

## Purpose 🎯

-   To practice **list comprehensions** for creating sequences of calculated values.
-   Reinforce basic **I/O operations** (input/output) in Python.
-   Enhance understanding of **looping through lists** and printing each element line by line.

## How It Works 🔍

1. **Function `generate_squares`**:

    - Accepts an integer `n` and returns a list of squares for numbers in the range from `1` to `n`.
    - The list comprehension `[i**2 for i in range(1, n+1)]` generates the square of each number in the range.

2. **Function `print_squares`**:
    - Prompts the user to enter a natural number (`n`).
    - Calls `generate_squares(n)` to compute the list of squares.
    - Uses `print(*squares, sep='\n')` to print each square on a new line.
    - The `*` operator unpacks the list, and `sep='\n'` ensures each item appears on a separate line.

## Output 📜

The script will output squares of numbers line by line.

**Example**:

```
Enter a natural number: 5
1
4
9
16
25
```

## Usage 📦

1. Copy the code into a Python file, e.g., `squares_generator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python squares_generator.py
    ```
5. Enter a natural number when prompted.
6. View the list of squares printed line by line.

## Conclusion 🚀

This simple yet practical script showcases the power of **list comprehensions** and Python’s ability to efficiently handle mathematical operations and print output in a structured format.
It's a great exercise for beginners learning to work with sequences and loops. 🌟
