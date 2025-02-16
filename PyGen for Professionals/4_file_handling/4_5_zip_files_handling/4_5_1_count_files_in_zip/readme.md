# ZIP Archive File Counter 🗂️

## Description 📝

This program counts the number of files (excluding folders) inside a ZIP archive.

## Purpose 🎯

The goal is to analyze the contents of a ZIP file and determine how many actual files it contains, disregarding directories.

## How It Works 🔍

1. **Opening the ZIP Archive**:
    - The program uses the `zipfile.ZipFile` module to open the archive.
2. **Counting Files**:
    - It iterates through the contents of the archive using `.infolist()`.
    - It filters out directories using the `.is_dir()` method.
    - It counts only the actual files.
3. **Output**:
    - The script prints the total number of files found in the archive.

## Output 📜

The program prints a single number representing the total number of files in `workbook.zip`.

### Example Output:

```
42
```

## Usage 📦

1. Ensure `workbook.zip` is present in the script's directory or specify its full path.
2. Run the script. It will print the number of files inside the ZIP archive.

## Conclusion 🚀

This script provides a quick and efficient way to count the number of files inside a ZIP archive, helping users analyze archive contents programmatically.
