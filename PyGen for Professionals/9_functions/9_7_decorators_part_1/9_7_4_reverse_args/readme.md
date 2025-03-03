# Reverse Args Decorator

## Description 📝

This Python program defines a `reverse_args` decorator, which reverses the order of positional arguments before passing them to the decorated function.
The decorator allows any function to accept its arguments in reverse order without modifying the function's return value.
It can decorate functions that accept an arbitrary number of positional and keyword arguments.

## Purpose 🎯

The `reverse_args` decorator is useful when you need to reverse the order of positional arguments before a function processes them.
This can be helpful in situations where the order of arguments is important, and you want to manipulate it before passing them to the function.

## How It Works 🔍

1. **Input**:

    - The `reverse_args` decorator is applied to a function that you want to modify.
    - The function can have any number of positional and keyword arguments.

2. **Processing**:

    - The decorator defines a `wrapper` function that takes the arguments for the decorated function.
    - The wrapper reverses the positional arguments (`args`) but keeps the keyword arguments (`kwargs`) unchanged.

3. **Output**:
    - The decorated function is called with reversed positional arguments, and the output is returned from the decorated function.

## Example 📜

### Example Usage:

```python
# Decorate the function with `reverse_args`
@reverse_args
def greet(name: str, age: int) -> str:
    return f"Name: {name}, Age: {age}"

# Call the decorated function
result = greet("Alice", 30)

print(result)  # Output will use reversed arguments
```

### Output:

```
Name: 30, Age: Alice
```

In the example, the positional arguments `"Alice"` and `30` are reversed before being passed to the `greet` function, resulting in the output being `"Name: 30, Age: Alice"`.

## Usage 📦

1. Define the `reverse_args` decorator in your script.
2. Apply it to any function by using the `@reverse_args` syntax before the function definition.
3. Call the decorated function as usual, and the positional arguments will be automatically reversed.

## Conclusion 🚀

The `reverse_args` decorator allows you to reverse the order of positional arguments before they are passed to a function.
It is a flexible tool that works with functions of any complexity and can be easily applied by using the decorator syntax.
