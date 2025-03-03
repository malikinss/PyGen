# Returns Decorator

## Description 📝

The `returns()` decorator checks that the return value of the decorated function matches the specified data type.
If the return value is of a different type, a `TypeError` is raised.
This decorator is useful for enforcing type consistency and ensuring that functions return the expected type of data.

## Purpose 🎯

The purpose of this decorator is to add type-checking functionality to functions.
It ensures that the return value of a function conforms to the specified `datatype`.
If the function returns an unexpected type, it throws a `TypeError`, helping to catch potential bugs early.

## How It Works 🔍

1. **Input**:

    - The decorator accepts a single argument:
        - `datatype`: The expected data type for the return value of the decorated function.

2. **Processing**:

    - The decorator wraps the original function and executes it.
    - After execution, it checks whether the returned value matches the expected `datatype`.
    - If the return type does not match, a `TypeError` is raised.
    - If the return type matches, the function's result is returned as is.

3. **Output**:
    - The output is the same as the original function's return value if the type matches the expected type.
    - If the type does not match, a `TypeError` is raised.

## Example 📜

```python
# Define a function with the returns decorator
@returns(int)
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

# Call the decorated function
result = add(2, 3)
print(result)  # Output: 5

# This will raise a TypeError
try:
    wrong_result = add("2", 3)
except TypeError as e:
    print(e)  # Output: Expected return type <class 'int'>, but got <class 'str'>
```

### Output:

```text
5
Expected return type <class 'int'>, but got <class 'str'>
```

In this example, the function `add()` is decorated to ensure that its return value is of type `int`. When the function returns a string or any other type, the decorator raises a `TypeError`.

## Usage 📦

1. Define the `returns` decorator in your script.
2. Apply the decorator to any function using the `@returns(datatype)` syntax, where `datatype` is the expected return type.
3. Call the decorated function, and if the return value does not match the specified type, a `TypeError` will be raised.

## Conclusion 🚀

The `returns()` decorator is a simple but effective tool for enforcing type consistency in your code.
It helps ensure that the return values of your functions are of the expected type, thus improving code safety and maintainability by catching errors early.
