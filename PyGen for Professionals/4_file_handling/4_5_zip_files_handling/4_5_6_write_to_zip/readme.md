# File Archiver 📦

## Description 📝

This script **creates a ZIP archive** named `files.zip`, adding all files from a predefined list.

## Purpose 🎯

To efficiently **compress and store multiple files** in a single archive.

## How It Works 🔍

1. **Define File List**
    - A list of filenames (`file_names`) is provided.
2. **Create ZIP Archive**
    - Opens `files.zip` in **write mode** (`'w'`).
3. **Add Files to ZIP**
    - Iterates through `file_names` and adds each file.
    - Uses `arcname` to **store only the filename** (not full path).

## Output 📜

The script generates `files.zip`, containing:

```
how to prove.pdf
fipi_demo_2022.pdf
Hollow Knight Silksong.exe
code.jpeg
stepik.png
readme.txt
shopping_list.txt
Alexandra Savior - Crying All the Time.mp3
homework.py
test.py
```

## Usage 📦

1. Ensure all files exist in the **script’s directory**.
2. Run the script to create `files.zip`.

## Conclusion 🚀

This script simplifies **file compression and archiving**, making it easier to manage multiple files.
