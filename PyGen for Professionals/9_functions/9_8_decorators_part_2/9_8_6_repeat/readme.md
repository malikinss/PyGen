# Repeat Decorator

## Description 📝

The `repeat()` decorator allows you to execute a decorated function multiple times based on a specified number (`times`).
This is useful when you want to repeat a function call for testing purposes or other scenarios where repeated execution is required.
The decorator ensures that the function's name and docstring are preserved.

## Purpose 🎯

The goal of this decorator is to run the decorated function a specified number of times without modifying the original function's behavior.
The decorator will return the result of the last execution.

## How It Works 🔍

1. **Input**:

    - The decorator accepts one argument:
        - `times`: An integer that defines how many times to call the decorated function.

2. **Processing**:

    - The `repeat()` decorator wraps the original function and runs it `times` times in a loop. The result of the function is stored, but only the return value of the last execution is returned.

3. **Output**:
    - The output is the return value from the last execution of the decorated function.

## Example 📜

```python
# Define a function with the repeat decorator
@repeat(3)
def greet(name: str) -> str:
    """Greets a person."""
    return f"Hello, {name}!"

# Call the decorated function
result = greet("Alice")
print(result)
```

### Output:

```text
Hello, Alice!
```

In this case, the function is executed three times, but only the result of the last execution is returned.

```python
# Another example with a function that performs an operation
@repeat(2)
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

# Call the decorated function
result = add_numbers(5, 3)
print(result)
```

### Output:

```text
8
```

## Usage 📦

1. Define the `repeat` decorator in your script.
2. Apply the decorator to any function using the `@repeat` syntax.
3. Pass the desired number of repetitions as an argument to the decorator.
4. Call the decorated function, and it will execute the function the specified number of times.

## Conclusion 🚀

The `repeat` decorator offers an efficient way to repeat the execution of a function a set number of times.
This is particularly useful in scenarios where you need repeated calls to a function but want to avoid manually repeating code.
The decorator preserves function metadata, ensuring the clarity and maintainability of the code.
