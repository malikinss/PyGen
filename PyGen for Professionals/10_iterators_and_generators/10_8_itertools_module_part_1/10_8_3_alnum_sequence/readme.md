# `alnum_sequence()`: Alternating Numbers and Letters Generator

## Description 📝

The `alnum_sequence()` function generates an **infinite cyclic sequence** of natural numbers (`1-26`) and uppercase Latin letters (`A-Z`).

## Purpose 🎯

This function is useful for cyclic ordering, encoding, or any application requiring a structured alternation between numbers and letters.

## How It Works 🔍

1. **Uses `cycle()` from `itertools`**:

    - Numbers: `1` to `26` cycle indefinitely.
    - Letters: `'A'` to `'Z'` cycle indefinitely.

2. **Pairs Elements Using `zip()`**:
    - Pairs each number with a letter (e.g., `1, 'A'` → `2, 'B'`).
    - Uses a generator expression to yield elements one by one.

## Output 📜

An **infinite iterator** alternating between numbers and letters.

### Example: Generating First 10 Elements

```python
>>> seq = alnum_sequence()
>>> [next(seq) for _ in range(10)]
[1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']
```

### Example: Printing the First 30 Elements

```python
seq = alnum_sequence()
for _ in range(30):
    print(next(seq), end=" ")
# Output: 1 A 2 B 3 C ... 25 Y 26 Z 1 A 2 B ...
```

## Usage 📦

1. Call `alnum_sequence()` to get an infinite iterator.
2. Use `next()` or iterate over it with a loop.

```python
seq = alnum_sequence()
while True:
    print(next(seq))  # Generates numbers and letters infinitely
```

## Conclusion 🚀

The `alnum_sequence()` function efficiently cycles through **numbers and letters** indefinitely.
It's an elegant way to create structured, repeating sequences! 🔄
