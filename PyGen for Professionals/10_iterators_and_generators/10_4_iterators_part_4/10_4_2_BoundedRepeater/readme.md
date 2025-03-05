# Bounded Repeater Iterator Class

## Description 📝

This Python script defines the `BoundedRepeater` class, an iterator that returns the same object a specified number of times.
Once the limit is reached, it raises a `StopIteration` exception.

## Purpose 🎯

The purpose of this class is to create an iterator that repeats a given object a fixed number of times.
This is useful for controlled iteration scenarios, such as generating test data, simulating repeated behavior, or handling limited loops.

## How It Works 🔍

1. **Initialization**:

    - The constructor (`__init__`) stores the given object and the number of repetitions (`times`).
    - A `counter` is initialized to track the number of iterations.

2. **Iterator Protocol**:
    - `__iter__()`: Returns the instance itself since it is an iterator.
    - `__next__()`:
        - Returns the stored object until `times` is reached.
        - Once the count exceeds `times`, it raises `StopIteration`.

## Output 📜

Example usage of the `BoundedRepeater` class:

```python
repeater = BoundedRepeater("Hello", 3)
print(list(repeater))  # Output: ['Hello', 'Hello', 'Hello']
```

## Usage 📦

1. Save the code to a file named `bounded_repeater.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using Python and use the class as follows:
    ```python
    repeater = BoundedRepeater(42, 5)
    for item in repeater:
        print(item)
    ```
    **Expected Output:**
    ```
    42
    42
    42
    42
    42
    ```

## Conclusion 🚀

The `BoundedRepeater` class provides a structured way to generate repeated values with a defined limit.
It follows the iterator protocol and demonstrates controlled iteration with `StopIteration`.
