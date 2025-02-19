# ZIP Archive Structure Viewer 🗂️📁

## Description 📝

This script extracts and displays the file structure of a ZIP archive, showing each file's size in human-readable units (B, KB, MB, GB).

## Purpose 🎯

-   Extract folder hierarchy from `desktop.zip`.
-   Format the structure with indents for different levels.
-   Convert file sizes to the largest possible unit.

## How It Works 🔍

1. Reads ZIP archive contents using `ZipFile`.
2. Identifies folder hierarchy (based on `/` count).
3. Formats indentation (2 spaces per nesting level).
4. Converts file sizes to appropriate units (B, KB, MB, GB).
5. Prints structured output, e.g.:
    ```
    Documents
      Resume.docx 45 KB
      Budget.xlsx 23 KB
    Pictures
      Vacation
        Beach.jpg 3 MB
    ```

## Usage 📦

### Run the script

```python
display_zip_structure('desktop.zip')
```

✅ Outputs ZIP structure with file sizes.

## Conclusion 🚀

A handy tool for viewing ZIP archive contents, especially for file organization and management! 🎯
