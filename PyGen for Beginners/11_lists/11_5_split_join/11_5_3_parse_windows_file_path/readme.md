# Parse Windows File Path 📝

## Description 📝

This Python program takes a file path in the Windows operating system format and splits it into individual components, separated by the backslash (`\`) character. Each component is printed on a separate line.

## Purpose 🎯

The purpose of this program is to parse and display the components of a file path in Windows format. This can be useful for debugging or analyzing file paths in a structured manner, helping to understand how a file is organized in a system.

## How It Works 🔍

1. The program takes a Windows-style file path as input, which may include the drive letter, subdirectories, and file name.
2. The file path is split into parts using the backslash (`\`) character as the delimiter.
3. Each part of the path is printed on a separate line for clear viewing.

## Output 📜

```bash
Example Input:
C:\Windows\System32\calc.exe

Example Output:
C:
Windows
System32
calc.exe
```

## Usage 📦

1. Save the script as `parse_file_path.py`.
2. Run the script in a Python environment.
3. Input the full file path in Windows format (e.g., `C:\Windows\System32\calc.exe`).
4. The program will print each part of the file path on a separate line.

## Conclusion 🚀

This program provides a simple and efficient way to display the components of a file path in Windows format. It's a helpful tool for working with file structures, especially when dealing with paths in Windows operating systems.
