# `alternating_sequence` Generator

## Description 📝

The `alternating_sequence` function generates an alternating sequence of natural numbers, where the sign of each number alternates between positive and negative.
The sequence starts with `1` and continues indefinitely, switching the sign for each subsequent number.
The sequence looks like this:  
`1, -2, 3, -4, 5, -6, 7, -8, 9, -10, ...`

## Purpose 🎯

This generator provides an efficient way to generate an alternating sequence of natural numbers, which can be useful for problems involving alternating signs, oscillating behaviors, or sequence manipulation tasks.

## How It Works 🔍

1. **`get_signed_number` Helper Function**:

    - This function alternates the sign of a number. If the number is even, it returns the negative value; otherwise, it returns the number as-is.

2. **Infinite Sequence (`count is None`)**:
    - The function will keep generating numbers indefinitely, alternating their signs, until the generator is manually stopped or iterated over in a loop.
3. **Finite Sequence (`count is a natural number`)**:
    - If `count` is provided, the function will generate exactly `count` numbers, then raise a `StopIteration` exception to stop the iteration.

## Output 📜

Example usage:

```python
gen = alternating_sequence()
for _ in range(10):
    print(next(gen), end=" ")
```

**Output:**

```
1 -2 3 -4 5 -6 7 -8 9 -10
```

If `count` is specified:

```python
gen = alternating_sequence(5)
for num in gen:
    print(num, end=" ")
```

**Output:**

```
1 -2 3 -4 5
```

## Usage 📦

1. **Create the generator**:
    ```python
    gen = alternating_sequence()
    ```
2. **Retrieve values using `next()`**:
    ```python
    print(next(gen))  # Output: 1
    print(next(gen))  # Output: -2
    print(next(gen))  # Output: 3
    print(next(gen))  # Output: -4
    ```
3. **Iterate with a loop**:
    ```python
    for i, num in enumerate(alternating_sequence()):
        print(num, end=" ")
        if i >= 19:  # Stop after 20 numbers
            break
    ```
    **Output:**
    ```
    1 -2 3 -4 5 -6 7 -8 9 -10 11 -12 13 -14 15 -16 17 -18 19 -20
    ```

## Conclusion 🚀

The `alternating_sequence` function is an efficient and flexible generator that can produce both infinite and finite alternating sequences.
It's particularly useful for problems involving alternating patterns or sign manipulation without needing to store the entire sequence in memory.
