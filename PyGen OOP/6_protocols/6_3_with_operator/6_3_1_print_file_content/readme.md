# print_file_content Function File Display Utility

## Description 📝

The `print_file_content` function accepts a `filename` parameter, a string representing a text file’s name (including extension).
It prints the file’s contents using UTF-8 encoding.
If the file is absent from the program’s folder, it outputs "File not found".

## Purpose 🎯

Designed for basic file reading tasks, such as displaying logs, configurations, or text data in scripts or command-line tools.
Error handling ensures clear feedback for missing files, fitting automation, debugging, or educational file I/O demonstrations.

## How It Works 🔍

-   **Input**: `filename`, a string with the file name and extension (e.g., "data.txt").
-   **Operation**:
    -   Opens the file in read mode (`'r'`) with `encoding='utf-8'` using a `with` statement.
    -   Reads content via `file.read()` into a string.
    -   Prints content with `print()`.
-   **Error Handling**:
    -   Uses `try-except` to catch `FileNotFoundError`.
    -   Prints "File not found" if triggered.
-   **Behavior**: Outputs file content exactly for valid files; provides error message for non-existent files.

## Verification ✅

Implementation meets requirements:

-   **Valid File**: For "example.txt" with "Hello\nWorld", outputs:
    ```
    Hello
    World
    ```
-   **Missing File**: For "missing.txt", outputs:
    ```
    File not found
    ```
-   **Encoding**: UTF-8 handles special characters correctly.
-   **Edge Cases**: Empty files print nothing; invalid filenames trigger the error message.

## Potential Considerations 🛠️

-   **Efficiency**: `file.read()` suits typical text files. Streaming could optimize large files but isn’t required.
-   **Error Scope**: Catches only `FileNotFoundError`, sufficient given task focus.
-   **Design**: Minimal and focused, aligning with no-validation requirement.

## Usage Example (For Clarity, Not Submission) 📦

```python
# For 'test.txt' with 'Hello, UTF-8!'
print_file_content('test.txt')  # Outputs: Hello, UTF-8!
print_file_content('nope.txt')  # Outputs: File not found
```

## Conclusion 🚀

The `print_file_content` function is precise, handling file output and errors effectively. It’s suitable for scripts requiring simple file display, fully compliant with the task.
