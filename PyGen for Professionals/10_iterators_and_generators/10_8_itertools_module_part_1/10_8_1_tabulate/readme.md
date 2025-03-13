# `tabulate()`: Infinite Sequence Generator

## Description 📝

The `tabulate()` function generates an infinite sequence of values by applying a given function to consecutive integers, starting from `1`.

## Purpose 🎯

This function is useful for generating infinite sequences of transformed values, such as squares, factorials, Fibonacci numbers, or any other mathematical series.

## How It Works 🔍

1. **Input Parameter**:

    - `func`: A callable function that accepts an integer and returns any value.

2. **Logic**:
    - Uses `itertools.count(1)` to generate an infinite sequence starting from `1`.
    - Maps each number to `func` and yields the result.

## Output 📜

An infinite iterator producing values of `func(n)` where `n = 1, 2, 3, ...`.

### Example: Squares of Numbers

```python
>>> gen = tabulate(lambda x: x**2)
>>> next(gen)
1
>>> next(gen)
4
>>> next(gen)
9
```

### Example: Multiples of 3

```python
>>> gen = tabulate(lambda x: x * 3)
>>> [next(gen) for _ in range(5)]
[3, 6, 9, 12, 15]
```

## Usage 📦

1. Define or import the function in your Python script.
2. Call `tabulate()` with any function that takes an integer.
3. Use `next()` to retrieve values or iterate over it.

```python
def cube(n):
    return n ** 3

gen = tabulate(cube)

for _ in range(5):
    print(next(gen))  # Prints 1, 8, 27, 64, 125
```

## Conclusion 🚀

The `tabulate()` function is a powerful tool for generating infinite numerical sequences with custom transformations.
It efficiently produces values on demand, making it ideal for lazy evaluation scenarios. 🌟
