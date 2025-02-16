# Best Compressed File Finder 📦

## Description 📝

This program finds the file in a ZIP archive that has the **best compression ratio** (smallest compressed size relative to the original size).

## Purpose 🎯

The goal is to analyze compression efficiency and determine which file is the most efficiently compressed.

## How It Works 🔍

1. **Extracting File Information**
    - The program reads the ZIP archive and retrieves file metadata.
2. **Filtering and Cleaning File Names**
    - Only files (not directories) are considered.
    - If a file is inside a folder, only the filename is extracted.
3. **Computing Compression Ratio**
    - The compression ratio is calculated as:  
      \[
      K = \left( \frac{\text{Compressed Size}}{\text{Original Size}} \right) \times 100
      \]
4. **Finding the Best Compressed File**
    - The file with the **smallest** compression ratio is selected.
5. **Output**
    - The filename of the most efficiently compressed file is printed.

## Output 📜

The program prints the name of the most compressed file (without the path).

### Example Output:

```
data.csv
```

## Usage 📦

1. Ensure `workbook.zip` is in the script's directory.
2. Run the script to find the file with the best compression ratio.

## Conclusion 🚀

This script provides insight into how well different files compress, helping evaluate storage efficiency.
