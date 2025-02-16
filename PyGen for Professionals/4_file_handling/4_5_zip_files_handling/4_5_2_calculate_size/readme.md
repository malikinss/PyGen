# ZIP Archive Size Calculator 📦

## Description 📝

This program calculates the total size of files in a ZIP archive in both uncompressed and compressed forms.

## Purpose 🎯

The goal is to analyze the storage efficiency of a ZIP archive by comparing the original file sizes with their compressed counterparts.

## How It Works 🔍

1. **Extracting File Information**:
    - The program uses `zipfile.ZipFile` to open the archive and retrieve metadata about its contents.
2. **Filtering Out Directories**:
    - Only actual files are considered (folders are ignored).
3. **Calculating Sizes**:
    - The program computes the total size of files before and after compression using `.file_size` and `.compress_size`.
4. **Output**:
    - It prints the sizes in the specified format.

## Output 📜

The program prints two values:

```
Размер исходных файлов: <размер до сжатия> байт(а)
Размер сжатых файлов: <размер после сжатия> байт(а)
```

### Example Output:

```
Размер исходных файлов: 105000 байт(а)
Размер сжатых файлов: 42000 байт(а)
```

## Usage 📦

1. Ensure `workbook.zip` is present in the script's directory or specify its full path.
2. Run the script. It will display the total file sizes in both original and compressed states.

## Conclusion 🚀

This script provides a quick and efficient way to evaluate the compression efficiency of ZIP archives, helping users understand storage savings.
