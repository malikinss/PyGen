# Print Operation Table

## Description 📝

This Python script defines the `print_operation_table()` function, which generates a table of results by applying a given binary operation (such as multiplication, addition, etc.) to row and column indices.
The function prints the table directly to the output.

## Purpose 🎯

The goal of this program is to demonstrate how to apply a binary operation across a table of indices.
The function can handle any binary operation (e.g., addition, multiplication, subtraction) and create a customizable table based on the given operation, rows, and columns.

## How It Works 🔍

1. **Arguments**: The function takes three arguments:
    - `operation`: A function that defines the binary operation (e.g., multiplication, addition).
    - `rows`: The number of rows in the table.
    - `cols`: The number of columns in the table.
2. **Table Generation**: The function iterates through each row (from 1 to `rows`) and each column (from 1 to `cols`). For each element at position `(n, m)`, it applies the operation (`operation(n, m)`).
3. **Output**: The result for each row is printed, with the elements separated by a single space.

## Output 📜

The function prints a table with the values of the operation applied to the row and column indices.  
For example, when using a multiplication operation with 5 rows and 5 columns, the output will be:

```
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
```

## Usage 📦

1. Save the code to a file named `operation_table.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```python
    python operation_table.py
    ```
5. Call the function `print_operation_table()` with a binary operation, number of rows, and number of columns.
   Example:
    ```python
    print_operation_table(lambda x, y: x * y, 5, 5)
    ```

## Conclusion 🚀

This program provides a flexible way to generate and print tables based on different binary operations.
It's a useful exercise for understanding how functions can be passed as arguments, and how loops and list comprehensions work together in Python.
