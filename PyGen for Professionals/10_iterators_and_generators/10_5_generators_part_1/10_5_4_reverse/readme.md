# `reverse` Generator

## Description 📝

The `reverse` function is a generator that produces elements of a given sequence in reverse order.
It supports any sequence type, such as `list`, `str`, or `tuple`, that allows indexing and has a defined length.

## Purpose 🎯

This generator is useful when you need to iterate over a sequence in reverse without modifying the original data structure.
It provides a memory-efficient way to traverse sequences backward.

## How It Works 🔍

-   The function takes a sequence as input.
-   It uses Python's built-in `reversed()` function to iterate over the sequence in reverse order.
-   The `yield from` statement efficiently delegates iteration to `reversed()`, reducing boilerplate code.

## Output 📜

Example usage:

```python
gen = reverse([1, 2, 3, 4, 5])
print(*gen)
```

**Output:**

```
5 4 3 2 1
```

## Usage 📦

1. **Reverse a list**:
    ```python
    for item in reverse([10, 20, 30]):
        print(item)
    ```
2. **Reverse a string**:

    ```python
    print("".join(reverse("hello")))
    ```

    **Output:**

    ```
    olleh
    ```

3. **Reverse a tuple**:
    ```python
    print(tuple(reverse((1, 2, 3, 4))))
    ```
    **Output:**
    ```
    (4, 3, 2, 1)
    ```

## Conclusion 🚀

The `reverse` generator provides a simple and efficient way to iterate over sequences in reverse order without creating unnecessary copies.
It leverages Python’s built-in `reversed()` for optimal performance and readability.
