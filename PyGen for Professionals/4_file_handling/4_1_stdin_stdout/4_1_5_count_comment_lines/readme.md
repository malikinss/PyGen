# Count Comment Lines in Code

## Description 📝

This Python program reads a block of Python code and determines the number of lines that contain only comments.
A line is considered a comment if it starts with a `#` symbol and contains no other code or non-whitespace characters.

## Purpose 🎯

The program helps in analyzing Python code to find out how many lines are entirely dedicated to comments, which can be useful for code documentation and cleanup.

## How It Works 🔍

1. **Function `read_code_from_input()`**:
    - Reads a block of Python code from the input line by line and returns it as a list of strings.
2. **Function `count_comment_lines(code_snippet)`**:
    - Iterates through each line of the input code and checks if the line contains only a comment (i.e., starts with a `#` symbol, with no other code or characters).
    - It counts such lines and returns the total count.

### Example:

For input:

```python
# This is a comment
print("Hello, world!")  # This is a comment
# Another comment
x = 10  # Comment here too
```

The program will output:

```
3
```

## Output 📜

The program outputs a single integer, which is the number of lines in the code that contain only comments.

Example output:

```
3
```

If there are no comment-only lines, the output will be:

```
0
```

## Usage 📦

1. Save the code in a file named `count_comment_lines.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script and provide input code via standard input.

### Example usage:

```bash
$ python count_comment_lines.py
# This is a comment
print("Hello, world!")  # This is a comment
# Another comment
x = 10  # Comment here too
```

The output will be:

```
3
```

## Conclusion 🚀

This program is useful for analyzing Python code and counting how many lines consist solely of comments, making it easier to track or improve the documentation of the code.
