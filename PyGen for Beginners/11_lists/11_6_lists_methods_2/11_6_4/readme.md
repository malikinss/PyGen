# Remove Comments from Code 📝

## Description 📝

This Python program removes all comments (denoted by the `#` symbol) from a given list of code lines. It strips everything from the `#` symbol onwards, preserving the actual code before the comment.

## Purpose 🎯

The program helps to clean up Python code by removing comments, which can be useful in scenarios where you need to analyze or process code without considering non-essential comment lines.

## How It Works 🔍

1. The function `remove_comments()` accepts a list of code lines as input.
2. It processes each line by splitting it at the `#` symbol, keeping only the part before the comment.
3. It strips any trailing whitespace from the line and adds the cleaned line to the result.
4. The cleaned lines are returned as a list without comments.

## Output 📜

```bash
Example Input:
Enter the number of lines: 3
Enter line: print("Hello, World!")  # This prints a greeting
Enter line: x = 42  # Set the answer to life
Enter line: # This is a comment line

Example Output:
print("Hello, World!")
x = 42
```

## Usage 📦

1. Save the script as `remove_comments.py`.
2. Run the script in a Python environment.
3. Enter the number of lines of code when prompted.
4. Enter each line of code, including comments.
5. The script will print the cleaned code, without any comments.

### Steps:

1. Open a terminal or Python IDE.
2. Execute the script using python `remove_comments.py`.
3. Enter the number of lines of code when prompted.
4. Input the code lines.
5. View the result in the console.

## Conclusion 🚀

This program is a simple utility for cleaning up Python code by removing comments. It processes each line to ensure only the code remains, making it suitable for code analysis or debugging.
