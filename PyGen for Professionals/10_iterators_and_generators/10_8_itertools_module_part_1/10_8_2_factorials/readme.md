# `factorials()`: Factorial Sequence Generator

## Description 📝

The `factorials()` function generates a sequence of factorials from `1!` to `n!` using the `accumulate()` function from `itertools`.

## Purpose 🎯

This function efficiently computes factorials in a lazy manner, avoiding unnecessary calculations and memory usage by yielding values on demand.

## How It Works 🔍

1. **Input Parameter**:

    - `n`: A natural number (`n ≥ 1`).

2. **Logic**:
    - Uses `range(1, n+1)` to create a sequence from `1` to `n`.
    - Uses `itertools.accumulate()` with `operator.mul` to compute factorials iteratively.

## Output 📜

An iterator producing factorial values from `1!` to `n!`.

### Example: Computing Factorials

```python
>>> list(factorials(5))
[1, 2, 6, 24, 120]
```

### Example: Using `next()`

```python
gen = factorials(4)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 6
print(next(gen))  # 24
```

## Usage 📦

1. Call `factorials(n)` with a natural number.
2. Iterate over it or use `next()` to retrieve values.

```python
for fact in factorials(7):
    print(fact)  # Prints 1, 2, 6, 24, 120, 720, 5040
```

## Conclusion 🚀

The `factorials()` function is an efficient way to compute factorials using functional programming techniques.
By leveraging `accumulate()`, it minimizes redundant calculations and provides a clear, elegant solution. 🌟
