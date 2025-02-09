# Last 10 Lines Viewer

## Description 📝

This Python program reads a specified text file and prints its last 10 lines.
If the file contains fewer than 10 lines, it prints the entire content.

## Purpose 🎯

The program is useful for quickly viewing the most recent content of a file, similar to the Unix `tail` command.

## How It Works 🔍

1. **Reading the File**:
    - The user provides a file name as input.
    - The program attempts to read the file.
2. **Extracting Last 10 Lines**:
    - If the file contains 10 or more lines, it prints only the last 10.
    - If the file has fewer than 10 lines, it prints all available lines.
3. **Handling Errors**:
    - If the file does not exist, an error message is displayed.

## Output 📜

The program prints the last 10 lines of the file, one per line.

### Example:

If `log.txt` contains:

```
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Line 11
Line 12
```

The program will output:

```
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Line 11
Line 12
```

If `log.txt` contains only 5 lines:

```
Line A
Line B
Line C
Line D
Line E
```

The output will be:

```
Line A
Line B
Line C
Line D
Line E
```

If the file does not exist:

```
File 'log.txt' not found.
```

## Usage 📦

1. Save the script as `last_10_lines.py`.
2. Place the target text file in the same directory.
3. Open a terminal or command prompt.
4. Navigate to the script's directory.
5. Run the script using:
    ```
    python last_10_lines.py
    ```
6. Enter the file name when prompted.

## Conclusion 🚀

This script provides a simple and efficient way to view the last 10 lines of a file, making it useful for log file analysis and debugging.
