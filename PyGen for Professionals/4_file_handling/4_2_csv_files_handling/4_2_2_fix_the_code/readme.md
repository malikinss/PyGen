# `CSV` File Writer Program

## Description 📝

This Python script creates and writes data to a `CSV` file (`writing_test.csv`) with specified columns and values.
The program demonstrates how to write data to a `CSV` file using the `csv` module and `DictWriter`.

## Purpose 🎯

The goal of this program is to show how to create a `CSV` file with headers and data rows.
It demonstrates file writing and handling dictionaries as rows in the `CSV` file.

## How It Works 🔍

1. **csv.DictWriter()**: Used to write a dictionary to the `CSV` file with the specified fieldnames.
2. **writeheader()**: Writes the header (column names) to the `CSV` file.
3. **writerows()**: Writes the rows of data to the file, each represented as a dictionary.

## Output 📜

When the script is executed, it will create a file called `writing_test.csv` with the following contents:

```
first_col,second_col
value1,value2
```

## Usage 📦

1. Save the code to a file named `write_csv_file.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```
    python write_csv_file.py
    ```
5. The program will create the file `writing_test.csv` with the specified contents.

## Conclusion 🚀

This program demonstrates how to write a `CSV` file in Python using `csv.DictWriter`.
It is a simple yet effective way to store data in CSV format.
