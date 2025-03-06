# Cycle Class

## Description 📝

The `Cycle` class is an infinite iterator that repeatedly cycles through the elements of a given iterable in their original order.
When it reaches the end of the iterable, it starts again from the beginning.

## Purpose 🎯

This iterator is useful when a program needs to loop indefinitely over a fixed set of values, such as repeating a sequence in animations, UI elements, or cyclic processes.

## How It Works 🔍

1. **Initialization (`__init__`)**:

    - Accepts an iterable (not an iterator or set) and validates it.
    - Stores the iterable and creates an initial iterator from it.

2. **Iterator Protocol**:
    - `__iter__()`: Returns `self` since the class implements `__next__()`.
    - `__next__()`:
        - Returns the next element from the iterator.
        - If the end of the iterable is reached, it resets and starts again from the beginning.

## Output 📜

Example usage:

```python
cycler = Cycle([1, 2, 3])
for _ in range(10):
    print(next(cycler), end=' ')
```

**Expected Output:**

```
1 2 3 1 2 3 1 2 3 1
```

## Usage 📦

1. Save the class in a file, e.g., `cycle.py`.
2. Use the following code to create an infinite cycle:
    ```python
    cycle_iter = Cycle('abc')
    for _ in range(5):
        print(next(cycle_iter), end=' ')
    ```
    **Expected Output:**
    ```
    a b c a b
    ```

## Conclusion 🚀

The `Cycle` iterator provides a simple way to repeat an iterable infinitely, making it useful for cyclic behaviors, animations, and round-robin scheduling tasks.
