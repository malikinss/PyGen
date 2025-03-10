# Merge Sequences in Interleaved Order

## Description 📝

The `interleave()` function merges multiple sequences (lists, tuples, strings, etc.) by producing a sequence of their elements interleaved.
Each sequence contributes its elements in order, starting from the first element of each sequence.

## Purpose 🎯

This function allows for combining sequences in a manner that alternates between their corresponding elements, making it easy to work with grouped data from multiple sources.

## How It Works 🔍

-   **Using `zip()`**: The `zip()` function is used to group corresponding elements from all sequences passed to the function. It produces tuples of elements, one from each sequence.
-   **Generator Expression**: The generator expression iterates over the tuples returned by `zip()`, yielding each element one by one.

## Output 📜

Example usage:

```python
print(list(interleave([1, 2], 'ab', (True, False))))
# Output: [1, 'a', True, 2, 'b', False]
```

## Usage 📦

1. Save the function in a Python file, e.g., `interleave.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the function:
    ```python
    from interleave import interleave
    print(list(interleave([1, 2], 'ab', (True, False))))  # Output: [1, 'a', True, 2, 'b', False]
    ```

## Conclusion 🚀

The `interleave()` function provides an elegant solution for combining multiple sequences in an interleaved order, ensuring that elements from each sequence appear in the final output as they correspond to each other.
