# Selective File Archiver 📂

## Description 📝

This script adds only small files (≤ 100 bytes) from a given list to an existing ZIP archive (`files.zip`).

## Purpose 🎯

To efficiently filter and archive small-sized files, avoiding unnecessary storage of large files.

## How It Works 🔍

1. Filter Small Files
    - Uses `os.path.getsize()` to check each file's size.
    - Keeps only files ≤ 100 bytes.
2. Update ZIP Archive
    - Opens `files.zip` in append mode (`'a'`).
    - Adds filtered files using their base names.

## Output 📜

The script updates `files.zip`, ensuring it contains only small files.

## Usage 📦

1. Ensure `files.zip` exists in the script’s directory.
2. Ensure files from `file_names` are present.
3. Run the script to add only small files to `files.zip`.

## Conclusion 🚀

This script helps manage efficient file archiving, ensuring that only small-sized files are included in the ZIP archive.
