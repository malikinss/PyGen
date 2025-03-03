# Do Twice Decorator

## Description 📝

This Python program defines a `do_twice` decorator, which ensures that the decorated function is called twice.
The decorator doesn't consume the return value of the function, and it works with functions that take any number of positional and keyword arguments.
The program returns the result from the second call of the decorated function.

## Purpose 🎯

The goal of the `do_twice` decorator is to modify a function so that it runs twice consecutively when called.
This is useful when you want to repeat an action or a function call, but without altering the original function’s behavior, input, or output.

## How It Works 🔍

1. **Input**:

    - The `do_twice` decorator is applied to any function that you wish to call twice.
    - The function accepts any number of positional and named arguments.

2. **Processing**:

    - The decorator wraps the original function in a new function (`wrapper`).
    - The `wrapper` function calls the original function twice with the same arguments, without using the result from the first call.

3. **Output**:
    - The output returned by the original function is from the second call, not the first.

## Example 📜

### Example Usage:

```python
# Decorate the function with `do_twice`
@do_twice
def greet(name: str) -> str:
    print(f"Hello, {name}!")
    return f"Hello, {name}!"

# Call the decorated function
result = greet("Alice")

print(result)  # Output is from the second call
```

### Output:

```
Hello, Alice!
Hello, Alice!
Hello, Alice!
```

In the example, `greet` is called twice, and the print statements display the message both times.
The result of the second call is returned.

## Usage 📦

1. Define the `do_twice` decorator in your script.
2. Apply it to any function by using the `@do_twice` syntax before the function definition.
3. Call the decorated function as usual, and it will run twice.

## Conclusion 🚀

The `do_twice` decorator provides a simple mechanism to execute any function twice in sequence.
It is flexible and works with functions that have any number of arguments.
