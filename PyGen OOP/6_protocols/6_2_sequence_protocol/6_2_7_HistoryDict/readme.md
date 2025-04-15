# HistoryDict Class Value Chronicle

## Description 📝

The `HistoryDict` class implements a dictionary that tracks the history of values for each key.
It accepts an optional dictionary `data` during instantiation (defaulting to empty), ensuring independence from the source.
The class provides methods `keys()`, `values()`, `items()`, `history()` (returns all values for a key), and `all_history()` (returns histories for current keys).
It supports length queries via `len()`, iteration over keys, and operations to get, set, and delete key-value pairs.
Deleting a key removes its history, and `history()` returns an empty list for non-existent or deleted keys.

## Purpose 🎯

This class is ideal for applications needing to audit changes, such as versioned configurations, undo/redo systems, or logging key-value updates in databases or UI states.
Its ability to recall past values enhances debugging or historical analysis, while its dictionary interface ensures ease of use.
It’s also a valuable educational tool for teaching Python’s mapping protocol and state tracking.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts optional `data` (defaults to `None`).
    -   Initializes `self._dict` as an empty dict or a copy of `data` using `dict(data)`, ensuring independence.
    -   Creates `self._history` as a dictionary mapping keys to lists of all values, starting with current values from `data`.
-   **Access Methods**:
    -   `keys()`: Returns `self._dict.keys()` for key iteration.
    -   `values()`: Returns `self._dict.values()` for value iteration.
    -   `items()`: Returns `self._dict.items()` for key-value tuple iteration.
-   **History Methods**:
    -   `history(key)`: Returns `self._history.get(key, [])`, providing all values for `key` or an empty list if absent/deleted.
    -   `all_history()`: Returns `self._history`, mapping current keys to their value histories (excludes deleted keys).
-   **Length (`__len__`)**:
    -   Returns `len(self._dict)`, counting current key-value pairs.
-   **Iteration (`__iter__`)**:
    -   Yields keys from `self._dict` using `yield from`, enabling key iteration.
-   **Get Item (`__getitem__`)**:
    -   Returns `self._dict[key]`, raising `KeyError` for non-existent keys.
-   **Set Item (`__setitem__`)**:
    -   Sets `self._dict[key] = value` to update the current value.
    -   Initializes `self._history[key] = []` if the key is new, then appends `value` to the history.
-   **Delete Item (`__delitem__`)**:
    -   Removes `key` from `self._dict` and `self._history` using `pop(key, None)`, clearing its history.
-   **Independence**: Copying `data` ensures the instance is unaffected by source changes.

## Verification ✅

Your implementation is correct:

-   **Init**: `d = HistoryDict({"a": 1})` sets `{"a": 1}` with history `{"a": [1]}`.
-   **Access**: `list(d.keys()) == ["a"]`; `list(d.values()) == [1]`; `list(d.items()) == [("a", 1)]`.
-   **History**: `d.history("a") == [1]`; `d.history("b") == []`.
-   **Updates**: `d["a"] = 2` → `d["a"] == 2`, `d.history("a") == [1, 2]`; `d["b"] = 3` → `d.history("b") == [3]`.
-   **Delete**: `del d["a"]`; `d.history("a") == []`; `d.all_history() == {"b": [3]}`.
-   **Length**: `len(d) == 1`.
-   **Iteration**: `list(d) == ["b"]`.
-   **Independence**: Source dict changes don’t affect `d`.

## Potential Considerations 🛠️

-   **Efficiency**: O(1) for most dictionary operations; history appends are O(1). Storing all values may increase memory for long histories.
-   **Edge Cases**: Handles empty dicts, deleted keys, and non-existent keys correctly, per valid data guarantee.
-   **Design**: Separate `_dict` and `_history` clarify current vs. past states, aligning with requirements.

## Usage Example (For Clarity, Not Submission) 📦

```python
d = HistoryDict({"a": 1})
d["a"] = 2
print(d.history("a"))    # [1, 2]
d["b"] = 3
print(d.all_history())   # {"a": [1, 2], "b": [3]}
del d["a"]
print(len(d))            # 1
print(list(d))           # ["b"]
print(d.history("a"))    # []
```

## Conclusion 🚀

Your `HistoryDict` implementation is precise and robust, offering a dictionary with full value history tracking.
Its intuitive interface, efficient history management, and independence make it perfect for auditing or versioned data tasks.
Fully compliant, it’s ready for any project needing historical key-value insights.
