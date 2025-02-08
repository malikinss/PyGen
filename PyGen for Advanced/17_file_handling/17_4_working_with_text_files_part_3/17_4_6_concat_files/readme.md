# File Concatenation Program

## Description 📝

This Python program reads a list of file names, concatenates their contents in the specified order, and writes the combined data into a new file called `output.txt`. The program preserves the order of the input files.

## Purpose 🎯

The program is designed to merge the contents of multiple files into a single output file without altering the order. This is useful for consolidating data from several sources into one file.

## How It Works 🔍

1. **Reading Data**:
    - The `read_data_from_file()` function reads the content of a file line by line and returns a list of strings representing each line.
2. **Getting File Names**:
    - The `get_file_names()` function prompts the user to input the names of the files to be concatenated. It collects these file names into a list.
3. **Concatenating Files**:
    - The `concat_files()` function takes the list of file names, reads each file, and appends its contents to a combined list.
4. **Writing the Result**:
    - The `write_data_to_file()` function writes the concatenated content into the `output.txt` file.

## Output 📜

The program creates or overwrites the `output.txt` file, which contains the combined contents of all the specified files. The order of the contents is preserved as per the input.

For example, if the input files are:

-   `file1.txt`:
    ```
    Line 1 from file 1
    Line 2 from file 1
    ```
-   `file2.txt`:
    ```
    Line 1 from file 2
    Line 2 from file 2
    ```

The resulting `output.txt` will contain:

```
Line 1 from file 1
Line 2 from file 1
Line 1 from file 2
Line 2 from file 2
```

## Usage 📦

1. Save the code in a file, e.g., `concatenate_files.py`.
2. Ensure the files you want to concatenate are available in the same directory.
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script using the command:
   `python concatenate_files.py`
6. When prompted, input the number of files you want to concatenate.
7. Provide the names of the files one by one.
8. The program will create or overwrite the `output.txt` file with the combined contents of the specified files.

## Conclusion 🚀

This program efficiently combines the contents of multiple files into one output file while maintaining the original order. It demonstrates basic file handling and data manipulation in Python.
