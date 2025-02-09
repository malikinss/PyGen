# Functions Without Explanatory Comments

## Description 📝

This Python program reads a Python file and identifies function definitions that are not preceded by explanatory comments.
It outputs the names of functions that lack comments or returns a message ("Best Programming Team") if all functions are properly commented.
The program checks each function definition and ensures there is a comment on the preceding line.

## Purpose 🎯

The purpose of this program is to ensure that all functions in a given Python code are documented with explanatory comments.
If any functions lack comments, their names are printed.
Otherwise, the message "Best Programming Team" is displayed, indicating all functions are well-documented.

## How It Works 🔍

1. **Reading the File**:

    - The program reads the Python file line by line and stores the lines in a list.

2. **Identifying Function Definitions**:

    - Each line that starts with `def ` is considered a function definition. The program checks whether the preceding line is a comment (i.e., starts with `#`).

3. **Checking for Comments**:

    - If a function definition is not preceded by a comment, the function name is added to the output list.

4. **Output**:
    - The program either prints the list of function names without comments or the message "Best Programming Team" if all functions are documented.

## Output 📜

### Example

#### **Input (`example.py`)**

```python
def func1():
    pass

# This is a comment for func2
def func2():
    pass

def func3():
    pass
```

#### **Output**

```
func1
func3
```

## Usage 📦

1. Save the script as `check_comments.py`.
2. Create a Python file (e.g., `example.py`) with functions.
3. Ensure the script and the Python file are in the same directory.
4. Run the script using:
    ```bash
    python check_comments.py
    ```
5. The function names without comments will be printed or the message "Best Programming Team" will appear if all functions are commented.

## Conclusion 🚀

This program helps ensure good documentation practices by checking if functions are preceded by explanatory comments.\
It's a useful tool for maintaining code quality in a team setting, encouraging developers to document their code properly.
