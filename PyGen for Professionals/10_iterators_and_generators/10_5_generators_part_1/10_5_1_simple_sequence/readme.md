# `simple_sequence` Generator

## Description 📝

The `simple_sequence` function is an infinite generator that produces a sequence of natural numbers where each number appears as many times as its value.
The sequence follows this pattern:  
 `1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, ...`

## Purpose 🎯

This generator function is useful for generating a structured, predictable sequence of numbers that grows progressively in frequency.
It can be used for testing purposes, mathematical simulations, or pattern-based problems.

## How It Works 🔍

1. **Initialization**:

    - `num` starts at `1`, representing the first number in the sequence.
    - `count` tracks how many times `num` has been yielded.

2. **Infinite Loop (`while True`)**:
    - `yield num` outputs the current number.
    - `count` is incremented after each yield.
    - When `count` reaches the value of `num`, the number increments (`num += 1`) and `count` resets to `0`, starting the next sequence.

## Output 📜

Example usage:

```python
gen = simple_sequence()
for _ in range(10):
    print(next(gen), end=" ")
```

**Output:**

```
1 2 2 3 3 3 4 4 4 4
```

## Usage 📦

1. **Create the generator**:
    ```python
    gen = simple_sequence()
    ```
2. **Retrieve values using `next()`**:
    ```python
    print(next(gen))  # Output: 1
    print(next(gen))  # Output: 2
    print(next(gen))  # Output: 2
    print(next(gen))  # Output: 3
    ```
3. **Iterate using a loop**:
    ```python
    for i, num in enumerate(simple_sequence()):
        print(num, end=" ")
        if i >= 19:  # Stop after 20 numbers
            break
    ```
    **Output:**
    ```
    1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6
    ```

## Conclusion 🚀

The `simple_sequence` function efficiently generates an infinite sequence with a structured pattern.
It is memory-efficient since it does not store the entire sequence but yields numbers dynamically.
This makes it well-suited for scenarios requiring on-the-fly sequence generation.
