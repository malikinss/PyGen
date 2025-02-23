# Counter Dictionary with Min and Max Values

## Description 📝

This Python script enhances the `Counter` dictionary by adding two dynamic methods:

-   **`min_values()`**: Returns a list of elements (key, value) with the smallest value.
-   **`max_values()`**: Returns a list of elements (key, value) with the largest value.

## Purpose 🎯

The program extends the `Counter` class to allow querying the most and least frequent elements while maintaining the original order.

## How It Works 🔍

1. **Filter Helper Function**:

    - `filter_items_by_specific_value()` retrieves key-value pairs where the value matches a given value.

2. **Defining Methods**:

    - `get_max_values()`: Finds the maximum value and returns all elements that have this value.
    - `get_min_values()`: Finds the minimum value and returns all elements that have this value.

3. **Attaching Methods to `Counter`**:
    - The methods are dynamically added to the `Counter` class so that any `Counter` object can use them.

## Output 📜

The script does not produce any output but enhances the `Counter` dictionary with new functionalities.

### Example Usage:

```python
from collections import Counter

# Sample Counter data
data = Counter("banana apple grape orange apple banana banana")

# Access the newly added methods
print(data.max_values())  # [('banana', 3)]
print(data.min_values())  # [('grape', 1), ('orange', 1)]
```

### Breakdown:

-   The most frequent word is **"banana"** (appears 3 times).
-   The least frequent words are **"grape"** and **"orange"** (each appears 1 time).

## Usage 📦

1. **Import the script** (if used as a module).
2. **Create a `Counter` object** from any iterable.
3. **Call `.max_values()` and `.min_values()`** to retrieve the most/least frequent elements.

### Example:

```python
from collections import Counter

data = Counter("hello world hello python")
print(data.max_values())  # [('hello', 2)]
print(data.min_values())  # [('world', 1), ('python', 1)]
```

## Conclusion 🚀

This enhancement makes it easier to analyze frequency distributions in a `Counter` object while preserving the original input order.
