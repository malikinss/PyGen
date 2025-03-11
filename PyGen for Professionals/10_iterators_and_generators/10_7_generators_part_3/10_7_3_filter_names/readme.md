# Filter Names Generator

## Description 📝

The `filter_names()` function is a generator that filters a list of names based on specified conditions.
It removes names that:

-   Start with a specific character (case insensitive).
-   Contain at least one digit.  
    The function then yields up to a specified number of valid names, maintaining the original order.

## Purpose 🎯

This function is useful for processing name lists while enforcing constraints such as ignoring certain names or limiting the number of results.
It utilizes Python generators for efficient memory usage.

## How It Works 🔍

1. **Input Parameters**:
    - `names`: An iterable containing names.
    - `ignore_char`: A single character; names starting with this character (case insensitive) are ignored.
    - `max_names`: The maximum number of names to yield.
2. **Validation**:
    - A helper function checks whether a name:
        - Does **not** contain digits.
        - Does **not** start with `ignore_char`.
3. **Filtering**:
    - The function uses a generator expression to filter valid names.
4. **Limiting Output**:
    - The function yields names until reaching `max_names`.

## Output 📜

The function returns a generator that produces valid names in their original order.

### Example:

```python
>>> list(filter_names(["Alice", "Bob", "3Charlie", "David", "alex"], "A", 3))
['Bob', 'David']
```

-   `"Alice"` and `"alex"` are ignored because they start with `"A"`.
-   `"3Charlie"` is ignored because it contains a digit.
-   Only `"Bob"` and `"David"` are valid, and since `max_names=3`, it stops after yielding them.

## Usage 📦

1. Save the code to a file, e.g., `filter_names.py`.
2. Call `filter_names()` with your desired parameters:
    ```python
    names_list = ["John", "2Sarah", "Adam", "Eve", "aaron", "123"]
    result = list(filter_names(names_list, "A", 5))
    print(result)  # Output: ['John', 'Eve']
    ```

## Conclusion 🚀

The `filter_names()` generator efficiently processes name lists while enforcing character-based filtering and digit exclusion.
It ensures optimal memory usage by yielding names one by one instead of storing them all at once. 🎉
