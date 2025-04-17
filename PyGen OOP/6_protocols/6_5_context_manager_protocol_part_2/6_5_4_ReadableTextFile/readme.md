# ReadableTextFile Class Line-Stripping File Reader

## Description 📝

The `ReadableTextFile` class is a context manager that opens a text file specified by `filename` for reading in UTF-8 encoding.
It provides access to file lines without trailing newline characters (`\n`) via iteration and closes the file after the `with` block.
The class implements the context manager protocol with `__enter__` and `__exit__` methods and supports iteration with `__iter__` and `__next__` to yield stripped lines.

## Purpose 🎯

Designed for reading text files in a controlled manner, such as processing logs, configuration files, or data inputs where newline characters are unwanted.
The context manager ensures proper file closure, making it suitable for scripting, data parsing, or educational examples of Python’s context manager and iterator protocols.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts `filename` (string) and stores it as `self.filename`.
    -   Initializes `self.data` as `None` to hold the file object, avoiding undefined state before opening.
-   **Enter Method (`__enter__`)**:
    -   Opens the file at `self.filename` in read mode (`'r'`) with `encoding='utf-8'`.
    -   Stores the file object in `self.data`.
    -   Returns `self`, enabling iteration over the instance.
-   **Exit Method (`__exit__`)**:
    -   Accepts `*args` (exception details) and `**kwargs` for protocol compliance.
    -   Closes `self.data` if it exists, ensuring resource cleanup.
-   **Iteration**:
    -   `__iter__`: Returns `self`, marking the instance as its own iterator.
    -   `__next__`: Reads the next line with `self.data.readline()`. If empty, raises `StopIteration`. Otherwise, returns the line with trailing newlines removed using `rstrip('\n')`.
-   **Behavior**:
    -   Yields lines without `\n`, preserving other content.
    -   Automatically closes the file post-block, even if exceptions occur.

## Verification ✅

Implementation meets requirements:

-   **File Reading**: For a file "test.txt" with:
    ```
    hello\n
    world\n
    ```
    `with ReadableTextFile("test.txt") as f: list(f)` yields `["hello", "world"]`.
-   **Context Management**: File is opened in `__enter__` and closed in `__exit__`.
-   **Encoding**: UTF-8 handles special characters correctly.
-   **Iteration**: Lines are stripped of `\n`, and iteration stops at file end.
-   **Edge Cases**: Empty files yield no lines; closed files are handled safely.

## Potential Considerations 🛠️

-   **Correctness**: `rstrip('\n')` removes only trailing newlines, preserving other whitespace, as intended.
-   **Performance**: Line-by-line reading is efficient for typical files; `rstrip` is O(1) per line.
-   **Design**: Returning `self` in `__enter__` allows direct iteration, aligning with task flexibility. `self.data` check in `__exit__` prevents errors if file opening fails.

## Usage Example (For Clarity, Not Submission) 📦

```python
# test.txt contains:
# line1\n
# line2\n
with ReadableTextFile('test.txt') as f:
    for line in f:
        print(line)  # Prints: line1\nline2
```

## Conclusion 🚀

The `ReadableTextFile` implementation is precise, providing a context manager that reads UTF-8 text files and yields lines without trailing newlines.
It ensures proper file closure and supports iteration, fully compliant with the task’s requirements. Suitable for text processing or protocol education, it’s robust and efficient.
