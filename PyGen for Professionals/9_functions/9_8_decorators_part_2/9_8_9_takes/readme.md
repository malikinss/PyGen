# Takes Decorator

## Description 📝

The `takes()` decorator ensures that the arguments passed to a decorated function are of specified types.
It accepts an arbitrary number of data types as arguments, checks if each argument matches one of these types, and raises a `TypeError` if any argument does not conform to the specified types.

## Purpose 🎯

This decorator is used to enforce type checks on function parameters, ensuring that the function only receives arguments of the expected types.
It improves code robustness by preventing type mismatches and potential bugs at runtime.

## How It Works 🔍

1. **Input**:

    - The decorator accepts multiple types as arguments (e.g., `int`, `str`, etc.).
    - These types are used to check whether the function's arguments are of one of the allowed types.

2. **Processing**:

    - The decorator wraps the original function and intercepts the function call.
    - It collects both the positional arguments (`args`) and the keyword arguments (`kwargs`).
    - It checks whether each argument matches one of the specified types.
    - If any argument does not match the allowed types, it raises a `TypeError` with a message specifying the invalid argument and type.

3. **Output**:
    - If all arguments match the specified types, the decorated function is called with the original arguments.
    - If any argument does not match, a `TypeError` is raised.

## Example 📜

```python
# Define the takes decorator
@takes(int, str)
def process_data(a: int, b: str) -> str:
    """Process an integer and a string."""
    return f"Processed {a} and {b}"

# Valid usage
print(process_data(10, "hello"))  # Output: Processed 10 and hello

# Invalid usage (raises TypeError)
try:
    print(process_data("hello", 10))
except TypeError as e:
    print(e)  # Output: Argument hello is not of type (<class 'int'>, <class 'str'>)
```

### Output:

```text
Processed 10 and hello
Argument hello is not of type (<class 'int'>, <class 'str'>)
```

In this example, the function `process_data()` is decorated with `@takes(int, str)`. It ensures that the first argument is an `int` and the second argument is a `str`. If either argument is of a different type, a `TypeError` is raised.

## Usage 📦

1. Define the `takes` decorator in your script.
2. Apply it to any function by using the `@takes(*types)` syntax, where `types` are the expected data types for the function arguments.
3. When calling the decorated function, the decorator will automatically check that each argument is of an appropriate type. If any argument has an incorrect type, it will raise a `TypeError`.

## Conclusion 🚀

The `takes()` decorator provides a convenient way to enforce type safety for function arguments.
It helps catch errors early by ensuring that the arguments passed to a function match the expected types.
This is particularly useful in large projects where type mismatches can lead to difficult-to-debug issues.
