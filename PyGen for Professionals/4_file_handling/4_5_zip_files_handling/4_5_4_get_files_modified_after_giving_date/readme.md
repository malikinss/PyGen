# Filter Recently Modified Files 📂

## Description 📝

This script finds and prints the names of files in a ZIP archive that were **created or modified after** `2021-11-30 14:22:00`.

## Purpose 🎯

To filter files that have been updated more recently than the given date and display them in **lexicographic order**.

## How It Works 🔍

1. **Extract File Information**
    - Reads the ZIP archive and retrieves file metadata.
2. **Convert Date Format**
    - The modification date from the archive is converted into a `datetime` object.
3. **Filter Files**
    - The script checks if a file's modification date is **later** than `2021-11-30 14:22:00`.
    - If so, its filename (without the path) is added to the results.
4. **Sort and Print**
    - The filenames are sorted in **lexicographic order** and printed **line by line**.

## Output 📜

The program prints filenames of all modified files after `2021-11-30 14:22:00`, sorted alphabetically.

### Example Output:

```
countries.json
data_sample.csv
report.pdf
```

## Usage 📦

1. Ensure `workbook.zip` is present in the script's directory.
2. Run the script to list all files modified **after** the specified date.

## Conclusion 🚀

This script is useful for identifying recently updated files in an archive, helping track changes efficiently.
