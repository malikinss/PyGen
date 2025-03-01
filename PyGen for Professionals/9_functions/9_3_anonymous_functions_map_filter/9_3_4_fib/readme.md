# Fibonacci Sequence Recursive Function

## Description 📝

This Python script defines a recursive function `fib()` that calculates the n-th term of the Fibonacci sequence using anonymous function syntax (lambda).
The Fibonacci sequence starts with 1, 1 and each subsequent term is the sum of the two preceding ones.

## Purpose 🎯

The purpose of this program is to demonstrate the use of recursion and anonymous functions (lambda) in Python to calculate the Fibonacci sequence.
It also helps in understanding how lambda functions can be utilized in recursive scenarios.

## How It Works 🔍

1. **Lambda Function**: An anonymous function is used to define the recursive process of the Fibonacci sequence.
2. **Base Case**: If `n` is 1 or 2, the function returns 1, as the first two terms of the Fibonacci sequence are both 1.
3. **Recursive Case**: For `n > 2`, the function calls itself recursively with the arguments `n-1` and `n-2`, summing the results to calculate the nth term of the sequence.

## Output 📜

When the script is executed and the user inputs a value for `n`, the output will be the n-th Fibonacci number.  
For example, if the user inputs 5, the output will be:

```
5
```

## Usage 📦

1. Save the code to a file named `fibonacci_recursive.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```
    python fibonacci_recursive.py
    ```
5. Call the function `fib()` with a positive integer `n` to calculate the corresponding Fibonacci number.
   Example:
    ```python
    print(fib(5))  # Output: 5
    ```

## Conclusion 🚀

This exercise shows how recursion and anonymous functions can be combined to solve problems efficiently.
Using lambda functions for recursion demonstrates an elegant and functional approach to problem-solving.
