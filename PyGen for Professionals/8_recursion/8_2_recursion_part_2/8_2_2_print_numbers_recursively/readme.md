# Natural Number Printer (Recursive)

## Description 📝

This program prints a sequence of natural numbers from 1 to 100 inclusive using recursion.
The function `print_numbers_recursively()` handles the task of printing numbers one by one, starting from 1 and ending at 100.

## Purpose 🎯

The purpose of this function is to demonstrate how recursion can be used to generate and print a sequence of numbers.
This is an alternative to using iterative loops like `for` or `while`.

## How It Works 🔍

1. The function takes two arguments: `start` (the current number to print) and `end` (the final number to print).
2. If `start` is less than or equal to `end`, the function prints `start` and then calls itself with the value `start + 1`.
3. The recursion continues until `start` exceeds `end`, at which point the recursion stops.

## Output 📜

The function prints numbers from `start` to `end` (inclusive). In this case, it prints the numbers from 1 to 100.

## Usage 📦

1. Call the `print_numbers_recursively(start, end)` function, where `start` is 1 and `end` is 100 (for printing numbers from 1 to 100).
2. The function will print each number from 1 to 100.

### Example:

```python
print_numbers_recursively(1, 100)
```

**Output:**

```
1
2
3
...
100
```

## Conclusion 🚀

This solution demonstrates how recursion can replace an iterative loop to perform repetitive tasks like printing a sequence of numbers.
The recursion ends once the starting number exceeds the ending number, stopping further calls.
