# WriteSpy Class Dual File Writer

## Description 📝

The `WriteSpy` class is a context manager that accepts two file objects (`file1`, `file2`) and a boolean `to_close` (defaulting to `False`) during instantiation.
It enables simultaneous writing to both files within a `with` block, optionally closing them upon exit based on `to_close`.
The class provides methods `write` (writes text to both files), `close` (closes both files), `writable` (checks if both files are writable), and `closed` (checks if both files are closed).
It implements the context manager protocol with `__enter__` and `__exit__` methods.

## Purpose 🎯

Designed for scenarios requiring mirrored writes to multiple files, such as logging to dual destinations, creating redundant backups, or synchronizing outputs.
The ability to control file closure and check file states makes it suitable for resource management in scripting, logging systems, or educational demonstrations of Python’s context manager protocol and file handling.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts `file1` and `file2` (file objects) and `to_close` (boolean).
    -   Stores them as `self._file1`, `self._file2`, and `self._to_close`.
-   **Enter Method (`__enter__`)**:
    -   Returns `self`, enabling method access (e.g., `write`) within the `with` block.
-   **Exit Method (`__exit__`)**:
    -   Accepts `*args` and `**kwargs` for protocol compliance.
    -   If `self._to_close` is `True`, calls `self.close()` to close both files.
-   **Write Method (`write`)**:
    -   Takes a `text` string and checks `self.writable()`.
    -   Raises `ValueError("The file is closed or not writable")` if not writable.
    -   Writes `text` to `self._file1` and `self._file2` using their `write` methods.
-   **Close Method (`close`)**:
    -   Calls `close()` on both `self._file1` and `self._file2`.
-   **Writable Method (`writable`)**:
    -   Attempts to call `writable()` on both files, returning `True` if both return `True`.
    -   Catches `ValueError` or `AttributeError` (possible for closed or invalid files) and returns `False`.
-   **Closed Method (`closed`)**:
    -   Returns `True` if both `self._file1.closed` and `self._file2.closed` are `True`, else `False`.
-   **Behavior**:
    -   Writes identically to both files if writable.
    -   Closes files only if `to_close` is `True` or `close()` is called explicitly.
    -   Provides state checks for writability and closure.

## Verification ✅

Implementation satisfies requirements:

-   **Writing**: `with WriteSpy(f1, f2): spy.write("test")` writes "test" to both `f1` and `f2`.
-   **Closure**: `WriteSpy(f1, f2, to_close=True)` closes both files after the block; `to_close=False` leaves them open.
-   **Error Handling**: `spy.write("text")` raises `ValueError` if either file is closed or not writable.
-   **Methods**:
    -   `close()` closes both files.
    -   `writable()` returns `True` only if both files are writable, `False` for closed/non-writable.
    -   `closed()` returns `True` only if both files are closed.
-   **Protocol**: `__enter__` and `__exit__` enable `with` statement usage.

## Potential Considerations 🛠️

-   **Correctness**: `writable()` handles exceptions from closed files, ensuring robust state checks.
-   **Performance**: O(1) for most operations (`write`, `close`, `closed`); `writable()` exception handling adds minimal overhead.
-   **Design**: Explicit `to_close` control and method-based state checks align with flexible protocol implementation.

## Usage Example (For Clarity, Not Submission) 📦

```python
f1 = open('file1.txt', 'w')
f2 = open('file2.txt', 'w')
with WriteSpy(f1, f2, to_close=True) as spy:
    spy.write("hello")  # Writes "hello" to both files
# Both files are closed
print(spy.closed())  # True
```

## Conclusion 🚀

The `WriteSpy` implementation is precise, enabling dual file writes with controlled closure and robust state checks.
It’s well-suited for synchronized writing tasks or protocol education, fully compliant with the task’s requirements.
