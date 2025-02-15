# `CSV` File Reader Program

## Description 📝

This Python script reads the contents of a `CSV` file (`grades.csv`) with semicolon-separated values and prints each row as a list.
It demonstrates how to read and process `CSV` files with custom delimiters.

## Purpose 🎯

The goal of this program is to show how to read a `CSV` file with a semicolon delimiter using the `csv` module and process the file to print each line as a list of values.
This exercise teaches basic file handling and `CSV` file parsing in Python.

## How It Works 🔍

1. **TODO Comment**: Describes the task of reading a `CSV` file and outputting the rows correctly.
2. **csv.reader()**: Used to read the file with a semicolon delimiter.
3. **List Comprehension**: Filters out empty rows and returns only non-empty rows as lists.

## Output 📜

When the script is executed, it will output the contents of the CSV file `grades.csv` as a list of lists:

```
[['name', 'grade'], ['Timur', '100'], ['Ruslan', '97']]
```

## Usage 📦

1. Save the code to a file named `read_csv_file.py`.
2. Create a CSV file `grades.csv` in the same directory with the following contents:
    ```
    name;grade
    Timur;100
    Ruslan;97
    ```
3. Open a terminal or command prompt.
4. Navigate to the directory where the files are located.
5. Execute the script using the command:
    ```
    python read_csv_file.py
    ```
6. The program will display the contents of the `CSV` file as a list of lists.

## Conclusion 🚀

This program demonstrates reading and processing a `CSV` file with a custom delimiter.
It teaches how to handle `CSV` files, process the data, and filter empty rows.
