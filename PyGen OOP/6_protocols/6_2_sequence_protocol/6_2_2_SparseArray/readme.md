# SparseArray Class Efficient Element Storage

## Description 📝

The `SparseArray` class implements a sparse array that stores only non-default elements, using a dictionary to track defined indices and their values.
It accepts a single `default` argument during instantiation, which is returned for undefined indices.
The class supports getting and setting values via indexing (`arr[i]`), with non-negative indices guaranteed.
Setting a value equal to the default removes it from storage, optimizing memory usage, while accessing undefined indices returns the default value.

## Purpose 🎯

This class is designed for scenarios where most array elements are a default value, such as in numerical computations (e.g., sparse matrices in scientific computing), game development (e.g., maps with mostly empty tiles), or data processing with large datasets having few significant entries.
Its memory-efficient storage makes it ideal for big data applications, while also serving as an educational example for Python’s indexing protocol and dictionary-based data structures.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Stores the `default` value in `self.default` for use in lookups and comparisons.
    -   Initializes an empty dictionary `self._data` to hold index-value pairs for non-default elements, ensuring sparse storage.
-   **Getting Values (`__getitem__`)**:
    -   Takes a non-negative integer `key` (guaranteed valid).
    -   Uses `self._data.get(key, self.default)` to return the value at `key` if defined, or `self.default` if not, providing seamless access to undefined indices.
-   **Setting Values (`__setitem__`)**:
    -   Accepts a `key` (index) and `value` to assign.
    -   If `value` equals `self.default`, removes the key from `self._data` using `pop(key, None)` to avoid storing default values, optimizing space.
    -   Otherwise, stores `value` at `self._data[key]`, marking it as a defined element.
-   **Sparse Efficiency**: Only non-default values are stored, reducing memory usage for arrays where most elements are the default (e.g., `0` or `None`).
-   **Dynamic Access**: Supports arbitrary non-negative indices without predefining size, reflecting changes instantly via the dictionary.

## Verification ✅

Your implementation is correct and efficient:

-   **Default Access**: `arr = SparseArray(0); arr[5] == 0` (undefined index returns default).
-   **Set and Get**: `arr[1] = 42; arr[1] == 42`.
-   **Default Optimization**: `arr[1] = 0; arr[1] == 0` and `1` not in `arr._data`.
-   **Sparse Storage**: Only non-default values (e.g., `arr[10] = 5`) are stored, others return `default`.
-   **Edge Cases**: Handles `None` defaults, empty arrays, and large indices robustly.

## Potential Considerations 🛠️

-   **Efficiency**: Dictionary-based storage is O(1) for get/set, ideal for sparse data. Removing default values minimizes memory use.
-   **Edge Cases**: Non-negative indices are guaranteed, and no validation is needed, aligning with the task.
-   **Flexibility**: Supports any default value type, enhancing versatility.

## Usage Example (For Clarity, Not Submission) 📦

```python
arr = SparseArray(0)
arr[1] = 10
print(arr[1])    # 10
print(arr[2])    # 0
arr[2] = 0       # No storage used
arr[3] = 20
print(arr[3])    # 20
```

## Conclusion 🚀

Your `SparseArray` implementation is spot-on, delivering a memory-efficient sparse array with intuitive indexing.
The dictionary-based approach ensures fast access and minimal storage by omitting default values, perfectly suiting sparse data scenarios.
It fully meets the task’s requirements with a clean, robust design, ready for numerical tasks, game maps, or teaching indexing protocols.
Extensions like iteration or length tracking aren’t needed but could be added for specific use cases.
Great work—ready to optimize any project needing sparse storage!
