# Archive File Information Extractor 📂

## Description 📝

This script extracts details of all files within a ZIP archive, listing their **names, modification dates, original sizes, and compressed sizes** in **lexicographic order**.

## Purpose 🎯

To **analyze the contents** of a ZIP archive, displaying key information about each file in a **structured and readable format**.

## How It Works 🔍

1. **Retrieve File Information**
    - Reads the ZIP archive and collects metadata for all files.
2. **Format Data**
    - Extracts the filename **without the path**.
    - Converts the modification date to **`YYYY-MM-DD HH:MM:SS`** format.
    - Retrieves the **original and compressed sizes** of each file.
3. **Sort Files Lexicographically**
    - Files are sorted **alphabetically** before displaying.
4. **Print the Data**
    - The details of each file are displayed in the following format:

```
  <file name>
    File modification date: <modification date>
    Original file size: <size before compression> bytes
    Compressed file size: <size after compression> bytes
```

## Output 📜

The program prints file details as follows:

```
Alexandra Savior - Crying All the Time.mp3
  File modification date: 2021-11-30 13:27:02
  Original file size: 5057559 bytes
  Compressed file size: 5051745 bytes

Hollow Knight Silksong.exe
  File modification date: 2013-08-22 08:20:06
  Original file size: 805992 bytes
  Compressed file size: 494930 bytes
```

## Usage 📦

1. Ensure `workbook.zip` is present in the script's directory.
2. Run the script to list all files with their details.

## Conclusion 🚀

This script is **helpful for reviewing ZIP archive contents**, making it easy to analyze file modifications and compression efficiency.
