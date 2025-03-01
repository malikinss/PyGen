# Find Maximum Expression Result Program

## Description 📝

This Python script reads multiple lines of valid mathematical expressions from the user, evaluates each expression, and outputs the value of the largest result.
It handles various mathematical operations and ensures the expressions comply with Python syntax.

## Purpose 🎯

The goal of this program is to demonstrate how to read multiple lines of input, evaluate mathematical expressions dynamically, and handle errors gracefully.
It helps in working with user input and evaluating expressions using Python’s built-in `eval()` function.

## How It Works 🔍

1. **read_input() Function**:

    - Reads multiple lines of input from the user.
    - Strips leading and trailing whitespace from each line and returns a list of non-empty lines.

2. **find_max_expression_result() Function**:

    - Evaluates each expression in the list obtained from `read_input()`.
    - Uses the `eval()` function to evaluate the expressions safely.
    - Checks that the result is a valid number (either integer or float).
    - Returns the largest evaluated result. If no valid result is found, returns negative infinity.

3. **Error Handling**:
    - If an expression causes a `SyntaxError`, `NameError`, `ZeroDivisionError`, or `ValueError`, an error message is printed to the standard error stream.

## Output 📜

When the script is executed, the program will output the largest value among the valid mathematical expressions provided. For example:

### Input:

```
3 + 5
10 * 2
8 / 2
```

### Output:

```
20
```

### Example of Invalid Input:

```
3 + 5
10 / 0
8 + 'a'
```

Output:

```
Error evaluating expression '10 / 0': division by zero
Error evaluating expression '8 + 'a'': invalid syntax
5
```

## Usage 📦

1. Save the code to a file named `max_expression_result.py`.
2. Open a terminal or command prompt.
3. Run the program:
    ```
    python max_expression_result.py
    ```
4. Provide multiple valid mathematical expressions, one per line.
5. The program will output the largest result from the expressions provided.

## Conclusion 🚀

This program showcases how to evaluate mathematical expressions safely in Python and find the maximum result.
It is useful for applications that require dynamic expression evaluation and error handling.
