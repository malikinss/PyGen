# limited_hash Function Range-Bound Hasher

## Description 📝

The `limited_hash` function creates a custom hash function that maps an object’s hash value to a specified integer range `[left, right]`.
It accepts three arguments: `left` (lower bound), `right` (upper bound), and an optional `hash_function` (defaulting to Python’s built-in `hash`).
The returned function computes the hash of an input object using the provided hash function and ensures the result falls within `[left, right]`.
If the hash is already in range, it’s returned unchanged; otherwise, it’s cyclically transformed—values above `right` wrap to `left` and increment, while values below `left` wrap to `right` and decrement—maintaining a consistent mapping.

## Purpose 🎯

This function is designed for applications requiring hash values confined to a specific range, such as indexing in fixed-size hash tables, generating bounded identifiers, or simulating constrained random number generation.
It’s particularly useful in algorithmic challenges, educational exercises on hashing, or systems like caching or load balancing where hash outputs need to fit within predefined limits, ensuring predictable and uniform distribution without losing the uniqueness of the original hash.

## How It Works 🔍

-   **Function Signature**: Takes `left` (integer), `right` (integer), and `hash_function` (callable, defaulting to `hash`), returning a new callable function.
-   **Inner Function (`func`)**: The returned function accepts any object (`obj`) and computes its hash:
    -   Computes the raw hash using `hash_function(obj)`, which could be the built-in `hash` or a custom function.
    -   Checks if the hash falls within `[left, right]` using `left <= hashed <= right`. If true, returns it unchanged to preserve the original value when possible.
    -   If outside the range, transforms the hash cyclically:
    -   Calculates the range size: `range_size = right - left + 1`.
    -   Applies the transformation `((hashed - left) % range_size) + left`, which:
    -   Shifts the hash relative to `left` (`hashed - left`).
    -   Uses modulo `range_size` to wrap the value into `[0, range_size-1]`.
    -   Adds `left` to map it back to `[left, right]`.
    -   This ensures values like `right + 1` map to `left`, `right + 2` to `left + 1`, and `left - 1` to `right`, `left - 2` to `right - 1`, etc., creating a cyclic pattern.
-   **Cyclic Mapping**:
    -   For hashes above `right`: `right + k` maps to `left + (k-1)`, e.g., `right + 1` → `left`, `right + 2` → `left + 1`.
    -   For hashes below `left`: `left - k` maps to `right - (k-1)`, e.g., `left - 1` → `right`, `left - 2` → `right - 1`.
    -   The modulo operation guarantees the result stays within `[left, right]` regardless of how far the hash deviates.
-   **Flexibility**: Works with any hash function, allowing customization, and handles any object type that the hash function accepts, leveraging Python’s dynamic typing.

## Usage 📦

1. **Save the Code**: Store the `limited_hash` function in a Python file, e.g., `limited_hash.py`, containing only the function definition for submission to a testing system, as no calling code is permitted.
2. **Apply in Context**: Use in scenarios needing bounded hashes:
    - Create a hash function for a specific range: `hasher = limited_hash(1, 5)`.
    - Hash objects: `hasher("test")` returns a value in `[1, 5]`.
    - Use with custom hash functions for specialized needs.
3. **Test Cases (Not for Submission)**: If testing locally, try:
    ```python
    hasher = limited_hash(1, 3)
    print(hasher("abc"))  # Some value in [1, 3], e.g., 2
    custom_hasher = limited_hash(0, 2, lambda x: hash(x) + 4)
    print(custom_hasher("abc"))  # Maps hash("abc") + 4 to [0, 2]
    ```
4. **Explore Behavior**: Experiment with different ranges (`left=0, right=10`, `left=-5, right=5`) and objects (strings, numbers, lists) to observe how out-of-range hashes cycle back into `[left, right]`, ensuring consistency across inputs.

## Conclusion 🚀

The `limited_hash` function provides a powerful and elegant solution for generating range-bound hash values in Python, transforming arbitrary hash outputs into a user-defined interval `[left, right]` with a clever cyclic mapping.
Its design ensures that in-range hashes remain unchanged for efficiency, while out-of-range values are seamlessly wrapped using a modulo-based transformation, making it both intuitive and robust.
This makes it an excellent tool for applications like hash table indexing, bounded randomization, or algorithmic experiments, as well as a clear educational example of functional programming and closure usage in Python.
The implementation is concise yet versatile, supporting custom hash functions and handling any input object gracefully.
While fully meeting the task’s requirements, it could be extended with features like range validation or additional transformation rules, but its current form is precise, efficient, and ready to enhance any project needing constrained hashing with deterministic, range-compliant results.
