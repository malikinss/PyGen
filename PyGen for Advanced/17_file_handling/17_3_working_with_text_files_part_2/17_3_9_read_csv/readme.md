# Program to Read and Parse CSV Data into a List of Dictionaries 📊

## Description 📝

This program reads a CSV file named **"data.csv"** and converts its contents into a list of dictionaries, where each dictionary represents a row with keys from the header and values from the row data.

## Purpose 🎯

To parse the CSV file into a usable format, where each row of data is a dictionary with column names as keys and corresponding row values as values.

## How It Works 🔍

1. **Reading the File (`read_file`)**:
    - The program reads the entire content of the file **"data.csv"** and stores each line as a string in a list.
2. **Extracting the Keys (`get_keys_from`)**:

    - The first line of the CSV file (header) is split by commas, and each element is treated as a key in the dictionary.

3. **Extracting the Rows (`get_rows_from`)**:

    - All the lines after the header (data rows) are extracted.

4. **Building Dictionaries (`build_csv_dict`)**:

    - Each row is split by commas to separate the values. A dictionary is created where the keys come from the header and the values come from the row.

5. **Main Function (`read_csv`)**:
    - Combines all the steps: reads the file, extracts the keys, processes the rows, and returns the final list of dictionaries.

## Example Usage:

**File (`data.csv`):**

```
name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
```

**Program Output:**

```python
[{'name': 'Alice', 'age': '30', 'city': 'New York'},
 {'name': 'Bob', 'age': '25', 'city': 'Los Angeles'},
 {'name': 'Charlie', 'age': '35', 'city': 'Chicago'}]
```

## Conclusion 🚀

This program provides an easy way to read CSV files and convert the data into a format that is easier to work with in Python, making it useful for various data processing tasks!
