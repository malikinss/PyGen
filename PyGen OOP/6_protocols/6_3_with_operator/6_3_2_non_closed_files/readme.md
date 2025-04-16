# non_closed_files Function Open File Filter

## Description 📝

The `non_closed_files` function accepts a list of file objects (`files`) and returns a new list containing only the open file objects, preserving their original order from the input list.

## Purpose 🎯

Designed for scenarios requiring identification of active file handles, such as resource management, debugging file leaks, or cleanup in applications handling multiple files.
It ensures only open files are processed, useful in scripting or system administration tasks.

## How It Works 🔍

-   **Input**: `files`, a list of file objects (type `IO`).
-   **Operation**:
    -   Uses a list comprehension to iterate over `files`.
    -   Includes only those file objects where `file.closed` is `False`.
-   **Output**: Returns a list of open file objects in the same order as in `files`.
-   **Behavior**: Filters out closed files efficiently, maintaining sequence integrity.

## Verification ✅

Implementation meets requirements:

-   **Valid Input**: For `[open_f1, closed_f2, open_f3]`, returns `[open_f1, open_f3]`.
-   **Order Preservation**: If `files = [f1, f2, f3]` with `f2` closed, output is `[f1, f3]`.
-   **Empty List**: For `[]`, returns `[]`.
-   **All Closed**: For all closed files, returns `[]`.
-   **All Open**: For all open files, returns the full list unchanged.

## Potential Considerations 🛠️

-   **Efficiency**: List comprehension is O(n), checking `file.closed` is O(1), suitable for typical use.
-   **Edge Cases**: Handles empty lists and mixed open/closed files correctly, per valid data guarantee.
-   **Design**: Simple and direct, avoiding unnecessary checks or modifications.

## Usage Example (For Clarity, Not Submission) 📦

```python
f1 = open('a.txt', 'w')
f2 = open('b.txt', 'w')
f2.close()
f3 = open('c.txt', 'w')
print(non_closed_files([f1, f2, f3]))  # [<f1>, <f3>]
```

## Conclusion 🚀

The `non_closed_files` function is concise and correct, efficiently filtering open file objects while preserving order.
It’s ready for tasks involving file handle management, fully compliant with the specification.
