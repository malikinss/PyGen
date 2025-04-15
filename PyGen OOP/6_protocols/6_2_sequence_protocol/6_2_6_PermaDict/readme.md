# PermaDict Class Immutable-Key Dictionary

## Description 📝

The `PermaDict` class implements a dictionary that allows adding and removing key-value pairs but prohibits changing values for existing keys.
It accepts an optional dictionary `data` during instantiation (defaulting to empty), ensuring independence from the source.
The class provides methods `keys()`, `values()`, and `items()` for accessing components, supports length queries via `len()`, iterates over keys, and enables key-based access (`d[key]`), addition (`d[key] = value`), and deletion (`del d[key]`).
Attempting to modify an existing key’s value raises a `KeyError` with the message "Changing the value by key is impossible."

## Purpose 🎯

This class is suited for scenarios requiring a dictionary with fixed values once keys are set, such as configuration stores, immutable mappings in data pipelines, or audit logs where updates to existing entries are restricted.
Its familiar dictionary interface makes it ideal for integration into existing systems, while also serving as an educational tool for teaching Python’s mapping protocol and controlled mutability.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts an optional `data` dictionary (defaults to `None`).
    -   Initializes `self._dict` as an empty dict if `data` is `None`, or as a copy of `data` using `dict(data)`, ensuring independence from the source dictionary.
-   **Access Methods**:
    -   `keys()`: Returns `self._dict.keys()`, an iterable of keys.
    -   `values()`: Returns `self._dict.values()`, an iterable of values.
    -   `items()`: Returns `self._dict.items()`, an iterable of key-value tuples.
    -   These delegate to the underlying dictionary for standard behavior.
-   **Length (`__len__`)**:
    -   Returns `len(self._dict)`, the number of key-value pairs.
-   **Iteration (`__iter__`)**:
    -   Yields keys from `self._dict` using `yield from`, enabling key iteration in loops.
-   **Get Item (`__getitem__`)**:
    -   Returns `self._dict[key]`, raising `KeyError` if the key doesn’t exist, mimicking standard dictionary access.
-   **Set Item (`__setitem__`)**:
    -   Checks if `key` exists in `self._dict`. If it does, raises `KeyError("Changing the value by key is impossible")`.
    -   Otherwise, sets `self._dict[key] = value`, adding the new pair.
-   **Delete Item (`__delitem__`)**:
    -   Removes `key` from `self._dict` using `del`, raising `KeyError` if the key doesn’t exist.
-   **Independence**: Copying `data` ensures changes to the original dictionary don’t affect the instance.

## Verification ✅

Your implementation is correct:

-   **Init**: `d = PermaDict({"a": 1, "b": 2})` creates `{"a": 1, "b": 2}`; `PermaDict()` is empty.
-   **Methods**: `list(d.keys()) == ["a", "b"]`; `list(d.values()) == [1, 2]`; `list(d.items()) == [("a", 1), ("b", 2)]`.
-   **Length**: `len(d) == 2`.
-   **Iteration**: `list(d) == ["a", "b"]`.
-   **Access**: `d["a"] == 1`.
-   **Add**: `d["c"] = 3` adds `c: 3`.
-   **Delete**: `del d["b"]` removes `b`.
-   **Restricted Update**: `d["a"] = 2` raises `KeyError`.
-   **Independence**: Changing the source dict doesn’t affect `d`.

## Potential Considerations 🛠️

-   **Efficiency**: Dictionary operations are O(1) for get/set/delete, with minimal overhead for the existence check in `__setitem__`.
-   **Edge Cases**: Handles empty dicts, missing keys, and valid data robustly, per the guarantee.
-   **Design**: Using a single `_dict` keeps the implementation simple and standard, aligning with dictionary-like behavior.

## Usage Example (For Clarity, Not Submission) 📦

```python
d = PermaDict({"a": 1})
print(len(d))        # 1
print(list(d))       # ["a"]
d["b"] = 2
print(d["b"])        # 2
del d["a"]
# d["b"] = 3         # Raises KeyError
print(list(d.items()))  # [("b", 2)]
```

## Conclusion 🚀

Your `PermaDict` implementation is precise, delivering a dictionary with immutable key-value bindings as required.
Its standard interface, clear error handling, and independence make it versatile for controlled mappings or teaching dictionary protocols.
Fully compliant and efficient, it’s ready for any project needing restricted updates.
