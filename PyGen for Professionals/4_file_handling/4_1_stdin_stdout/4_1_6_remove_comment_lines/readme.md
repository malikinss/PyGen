# Remove Comment Lines from Code

## Description 📝

This Python program reads a block of Python code and removes all lines that contain only comments.
A line is considered a comment if it starts with a `#` symbol and contains no other code or non-whitespace characters.

## Purpose 🎯

The program helps in cleaning up Python code by removing comment-only lines, which can be useful for reducing clutter and focusing on the actual code.

## How It Works 🔍

1. **Function `read_code_from_input()`**:

    - Reads a block of Python code from the input line by line and returns it as a list of strings.

2. **Function `remove_comment_lines(code_snippet)`**:

    - Iterates through each line of the input code.
    - Removes lines that contain only comments (i.e., lines that start with a `#` symbol and contain no other code or characters).
    - Returns the list of code lines without comment-only lines.

3. **Function `display_code(code_snippet)`**:
    - Displays the modified code snippet by printing it to the standard output.

### Example:

For input:

```python
# This is a comment
print("Hello, world!")  # This is a comment
# Another comment
x = 10  # Comment here too
```

The program will output:

```python
print("Hello, world!")  # This is a comment
x = 10  # Comment here too
```

## Output 📜

The program outputs the code with all lines that contain only comments removed.

Example output:

```python
print("Hello, world!")  # This is a comment
x = 10  # Comment here too
```

If all lines are comments, the output will be empty.

## Usage 📦

1. Save the code in a file named `remove_comment_lines.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script and provide input code via standard input.

### Example usage:

```bash
$ python remove_comment_lines.py
# This is a comment
print("Hello, world!")  # This is a comment
# Another comment
x = 10  # Comment here too
```

The output will be:

```python
print("Hello, world!")  # This is a comment
x = 10  # Comment here too
```

## Conclusion 🚀

This program is useful for cleaning up Python code by removing unnecessary comment-only lines, helping to make the code more concise and focused.
