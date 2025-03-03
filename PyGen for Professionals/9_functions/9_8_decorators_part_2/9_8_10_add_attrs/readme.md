# `add_attrs` Decorator

## Description 📝

The `add_attrs` decorator adds arbitrary named attributes to the decorated function.
These attributes are set as properties of the function, with the attribute name being the argument's name and the attribute value being the argument's value.

## Purpose 🎯

This decorator allows for dynamic addition of attributes to functions, which can be useful for attaching metadata or other information to functions without altering their core logic.
The added attributes can later be accessed via the function's `__dict__` attribute.

## How It Works 🔍

1. **Input**:
    - The decorator takes named arguments (key-value pairs), where each key represents an attribute name, and each value represents the value of that attribute.
2. **Processing**:

    - The decorator wraps the original function and then sets the provided named arguments as attributes of the function. These attributes are stored in the function's `__dict__` attribute.

3. **Output**:

    - The original function is returned, now with additional attributes.

4. **Accessing Added Attributes**:
    - After decoration, the added attributes can be accessed using the `__dict__` attribute of the function.

## Example 📜

```python
# Define the add_attrs decorator
@add_attrs(color='blue', size=10)
def example_function():
    """A sample function."""
    return "Hello, world!"

# Access added attributes
print(example_function.__dict__)  # Output: {'color': 'blue', 'size': 10}

# Call the function
print(example_function())  # Output: Hello, world!
```

### Output:

```text
{'color': 'blue', 'size': 10}
Hello, world!
```

In this example, the function `example_function()` is decorated with `@add_attrs(color='blue', size=10)`. The decorator adds `color` and `size` as attributes to the function, and you can access them via the function’s `__dict__`.

## Usage 📦

1. Define the `add_attrs` decorator in your script.
2. Apply it to any function by using the `@add_attrs(**attributes)` syntax, where `attributes` are the named arguments to be set as function attributes.
3. After decoration, you can access the added attributes by calling the `__dict__` attribute on the decorated function.

## Conclusion 🚀

The `add_attrs` decorator provides a flexible way to attach metadata or other attributes to functions.
This can be particularly useful when you need to associate information with a function, such as configuration settings, flags, or other dynamic properties, without modifying the function's core behavior.
