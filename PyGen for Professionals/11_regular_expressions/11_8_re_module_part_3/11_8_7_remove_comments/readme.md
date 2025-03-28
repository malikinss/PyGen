# Python Comment Remover 🧹

## Description 📝

This program removes all types of comments from Python code, including:

-   **Single-line comments** (`#`)
-   **Inline comments** (after a statement)
-   **Multiline comments** (`""" """`)

## Purpose 🎯

The purpose of this program is to clean Python code by stripping unnecessary comments while preserving the actual logic.

## How It Works 🔍

1. **Reads Input**:

    - The program reads Python code from standard input.

2. **Removes Comments**:

    - Uses regular expressions to detect and remove:
        - Single-line comments that start with `#`
        - Inline comments that follow a line of code
        - Multiline comments enclosed in triple double quotes (`""" """`)

3. **Outputs Cleaned Code**:
    - The program prints the cleaned Python code without comments.

## Output 📜

### Example Input:

```python
# This is a single-line comment
def add(a, b):
    """This is a
    multiline comment"""
    return a + b  # Inline comment
```

### Example Output:

```python
def add(a, b):
    return a + b
```

## Usage 📦

1. Run the script and provide Python code as input:

    ```sh
    python comment_remover.py < input.py
    ```

2. The script will remove all comments and output the cleaned code.

## Conclusion 🚀

This tool helps in cleaning up Python code by removing all unnecessary comments, making the code more readable and compact.
