# Generator for Non-Empty Lines with Line Length Handling

## Description 📝

The `nonempty_lines()` function is a generator that processes a text file and yields non-empty lines.
For lines longer than 25 characters, it replaces them with an ellipsis (`...`).
This function removes the newline character and any surrounding whitespace.

## Purpose 🎯

This function is useful for iterating over the content of a file while filtering out empty lines and handling long lines.
The generator ensures memory efficiency as it processes the file line by line, only returning relevant lines and transforming those that exceed a certain length.

## How It Works 🔍

1. **Input Parameters**:
    - `file`: The path to the text file that needs to be processed.
2. **Line Processing**:

    - The function opens the file with explicit UTF-8 encoding.
    - It reads each line from the file, stripping off leading and trailing whitespace and the newline character (`\n`).
    - If the line is non-empty:
        - If the line contains more than 25 characters, it yields an ellipsis (`...`).
        - Otherwise, it yields the original line.

3. **Generator**:
    - The function uses a generator to yield the lines one by one, making it memory-efficient for large files.

## Output 📜

The function yields a sequence of strings:

-   Non-empty lines from the file, with any lines longer than 25 characters replaced by `...`.

### Example:

```python
>>> for line in nonempty_lines('data.txt'):
>>>     print(line)
Hello World
...
This is a line with a very long text that exceeds twenty five characters.
...
Another line
```

## Usage 📦

1. Save the code to a file, e.g., `filter_lines.py`.
2. Call the `nonempty_lines()` function with the path to your text file:
    ```python
    for line in nonempty_lines('data.txt'):
        print(line)  # Outputs each non-empty line, with long lines replaced by "..."
    ```

## Conclusion 🚀

The `nonempty_lines()` generator provides an efficient way to filter out empty lines and handle long lines in a text file.
It is both memory-efficient and flexible for processing large files with varying line lengths. 🌟
