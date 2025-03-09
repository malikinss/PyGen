# `dates` Generator

## Description 📝

The `dates` generator function produces a sequence of dates starting from a given `start` date.
It can generate a finite number of dates or an infinite sequence until the maximum representable date (`date.max`) is reached.

## Purpose 🎯

This generator is useful for iterating over consecutive dates efficiently without storing all dates in memory.
It can be used for scheduling, data processing, and time-based simulations.

## How It Works 🔍

-   The function takes a `start` date and an optional `count` argument.
-   If `count` is provided, it generates exactly `count` dates starting from `start`.
-   If `count` is `None`, it generates an infinite sequence of dates until `date.max`.

## Output 📜

Example usage:

```python
from datetime import date

gen = dates(date(2024, 3, 9), 5)
print(*gen)
```

**Output:**

```
2024-03-09 2024-03-10 2024-03-11 2024-03-12 2024-03-13
```

## Usage 📦

1. **Generate a fixed number of dates**:

    ```python
    for d in dates(date(2024, 3, 1), 3):
        print(d)
    ```

    **Output:**

    ```
    2024-03-01
    2024-03-02
    2024-03-03
    ```

2. **Generate an infinite sequence of dates**:

    ```python
    gen = dates(date(2024, 3, 1))
    for _ in range(5):
        print(next(gen))
    ```

    **Output:**

    ```
    2024-03-01
    2024-03-02
    2024-03-03
    2024-03-04
    2024-03-05
    ```

3. **Handle edge cases**:
    ```python
    gen = dates(date.max, 3)
    print(list(gen))
    ```
    **Output:**
    ```
    [datetime.date(9999, 12, 31)]
    ```

## Conclusion 🚀

The `dates` generator provides an efficient way to iterate over consecutive dates while handling both finite and infinite sequences.
It ensures clean and readable code when working with time-based data.
