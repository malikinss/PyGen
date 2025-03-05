# Repeater Iterator Class

## Description 📝

This Python script defines the `Repeater` class, an iterator that indefinitely returns the same object.
Once instantiated with an object, calling `next()` on its iterator will always return that object.

## Purpose 🎯

The purpose of this class is to create an infinite iterator that repeatedly yields the same value.
This can be useful in scenarios where a constant value is needed continuously, such as in testing, simulations, or infinite loops.

## How It Works 🔍

1. **Initialization**: The constructor (`__init__`) stores the given object.
2. **Iterator Protocol**:
    - `__iter__()`: Returns the instance itself since it is an iterator.
    - `__next__()`: Always returns the stored object, creating an infinite loop.

## Output 📜

Example usage of the `Repeater` class:

```python
repeater = Repeater("Hello")
print(next(repeater))  # Output: Hello
print(next(repeater))  # Output: Hello
```

## Usage 📦

1. Save the code to a file named `repeater.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using Python and use the class as follows:
    ```python
    repeater = Repeater(42)
    print(next(repeater))  # Output: 42
    print(next(repeater))  # Output: 42
    ```

## Conclusion 🚀

The `Repeater` class provides a simple yet effective way to generate an infinite sequence of the same value.
It demonstrates the use of the iterator protocol (`__iter__` and `__next__`) and can be useful for various programming scenarios.
