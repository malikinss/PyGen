# Takes Positive Decorator

## Description 📝

This Python program implements a `takes_positive` decorator that validates all arguments passed to a decorated function.
It ensures that all arguments are positive integers. If any argument is not a positive integer, it raises a `TypeError` for non-integer values and a `ValueError` for integers that are zero or negative.

## Purpose 🎯

The `takes_positive` decorator is used to ensure that a function only processes positive integers.
It helps prevent invalid input from being passed into a function and handles exceptions appropriately, making the code more robust and reliable.

## How It Works 🔍

1. **Input**:

    - The `takes_positive` decorator is applied to a function. This function can take any number of positional and keyword arguments.

2. **Processing**:

    - The decorator checks each argument:
        - If any argument is not an integer, it raises a `TypeError`.
        - If any argument is a non-positive integer (zero or negative), it raises a `ValueError`.
    - The decorator checks `TypeError` first and `ValueError` second, as specified.

3. **Output**:
    - If all arguments pass the checks, the function is executed as normal.
    - If any argument fails the checks, an exception is raised.

## Example 📜

### Example Usage:

```python
# Decorate the function with `takes_positive`
@takes_positive
def add_positive_numbers(a: int, b: int) -> int:
    return a + b

# Call the decorated function with valid arguments
try:
    result = add_positive_numbers(10, 5)
    print(result)  # Output: 15
except Exception as e:
    print(e)

# Call the decorated function with invalid arguments
try:
    result = add_positive_numbers(10, -5)
except Exception as e:
    print(e)  # Output: Argument -5 is not a positive integer
```

### Output:

```
15
Argument -5 is not a positive integer
```

In the example, the function `add_positive_numbers` is decorated with `takes_positive`. When called with valid arguments (positive integers), the function executes normally and returns the result. When called with invalid arguments (negative integer), it raises and prints a `ValueError` indicating that the argument is not positive.

## Usage 📦

1. Define the `takes_positive` decorator in your script.
2. Apply it to any function by using the `@takes_positive` syntax before the function definition.
3. Call the decorated function with the required arguments. The decorator will automatically validate the arguments and raise exceptions if necessary.

## Conclusion 🚀

The `takes_positive` decorator is a useful tool for ensuring that functions receive valid positive integer arguments.
It simplifies input validation by automatically raising appropriate exceptions when the conditions are not met, thus preventing potential errors in function execution.
