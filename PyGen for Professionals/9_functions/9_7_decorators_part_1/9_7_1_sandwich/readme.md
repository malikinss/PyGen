# Sandwich Decorator

## Description 📝

This Python script defines a `sandwich` decorator that prints "bread slices" before and after calling the decorated function.
It adds a top slice before the function executes and a bottom slice afterward, creating a "sandwich" around the function call.

## Purpose 🎯

The decorator is designed to be used on functions where you want to add additional behavior (in this case, printing bread slices) before and after the function execution.
The return value of the decorated function is not affected, and the decorator works with functions that take any number of positional and keyword arguments.

## How It Works 🔍

1. **Input**:

    - A function (`original_func`) is passed to the decorator.
    - The function can accept any number of positional (`*args`) and keyword arguments (`**kwargs`).

2. **Processing**:  
   The `sandwich` decorator:

    - Prints a top slice message before the function executes.
    - Calls the original function with any arguments passed to it.
    - Prints a bottom slice message after the function executes.

3. **Output**:  
   The decorator returns a new function (`wrapper`) that maintains the original function's behavior while adding the additional print statements before and after the function call.

## Example 📜

### Example Usage:

```python
@sandwich
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Calling the decorated function
print(greet("Alice"))
```

### Output:

```
---- Top slice of bread ----
Hello, Alice!
---- Bottom slice of bread ----
```

## Usage 📦

1. Define the `sandwich` decorator in your script.
2. Decorate any function with `@sandwich` to add "bread slices" before and after the function execution.
3. Call the decorated function to see the output.

## Conclusion 🚀

The `sandwich` decorator provides a fun and useful way to add extra behavior around any function call, allowing you to enhance functions without altering their core functionality.  
Enjoy decorating your functions! 🍞
