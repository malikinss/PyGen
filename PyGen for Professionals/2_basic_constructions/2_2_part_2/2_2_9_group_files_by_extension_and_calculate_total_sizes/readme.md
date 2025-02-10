# File Grouping and Size Calculation 🗂️

## Description 📝

This Python program groups files by their extensions, calculates the total size for each group, and displays the results.
It handles file information from a text file and outputs the file names sorted lexicographically by their extension and calculates the total size of each group in the largest possible unit (B, KB, MB, or GB).

## Purpose 🎯

The goal of this program is to:

-   Group files by their extension.
-   Calculate the total size of files in each extension group.
-   Display the files in each group, sorted by their names.
-   Provide the total size of each group in the largest possible unit, rounded to the nearest whole unit.

## How It Works 🔍

1. The program reads the file `files.txt`, which contains file names, their sizes, and units.
2. It then parses this information and groups the files by their extensions.
3. The program calculates the total size of files in each group, converts the size to the largest possible unit, and prints the results.

## Output 📜

For each extension group, the program displays:

-   A list of file names in the group, sorted alphabetically.
-   A summary line showing the total size for the group in the largest possible unit (e.g., KB, MB, GB).

### Example output:

```
boy.bmp
mario.bmp
----------
Summary: 3 MB

input.txt
output.txt
temp.txt
----------
Summary: 8 KB

data.zip
scratch.zip
----------
Summary: 1 GB
```

## Usage 📦

1. Place your file data in a file named `files.txt` in the same directory as the Python script.
2. Ensure each line in `files.txt` contains the filename, size, and unit, separated by spaces.
3. Run the script to see the grouped files and their total sizes printed in the terminal.

### Example:

```
input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4 KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB
```

4. The program will process the file, group the files by extension, and display the output as shown above.

## Conclusion 🚀

This program allows for efficient grouping and size calculation of files based on their extensions.
It handles different units of file sizes and outputs the result in a user-friendly manner, making it easier to analyze and manage file data.
