# `CSV` Columns Extraction Program

## Description 📝

This program reads a `CSV` file and extracts its columns into a dictionary.
Each key in the dictionary corresponds to a column name, and each value is a list containing the elements of that column.
The program ensures that the order of the columns and their elements remains the same as in the original file.

## Purpose 🎯

The purpose of this program is to:

-   Read and process `CSV` files.
-   Convert `CSV` data into a dictionary format, where keys are column names and values are lists of column elements.
-   Ensure that the data is processed and returned in its original order.

## How It Works 🔍

1. The function `csv_columns(filename)` reads the `CSV` file specified by the `filename`.
2. The first line of the file, containing column names, is used as the keys in the resulting dictionary.
3. The subsequent rows are processed, and the corresponding values are added to each column key.
4. The program returns a dictionary with column names as keys and lists of elements as values.

## Output 📜

The function returns a dictionary where:

-   The key is the column name.
-   The value is a list of elements from that column.

Example:

For a file `exam.csv` with the following content:

```
name,grade
Timur,5
Arthur,4
Anri,5
```

The output of the function `csv_columns('exam.csv')` will be:

```python
{
    'name': ['Timur', 'Arthur', 'Anri'],
    'grade': ['5', '4', '5']
}
```

## Usage 📦

1. Prepare your `CSV` file (e.g., `data.csv` or `exam.csv`).
2. Call the `csv_columns()` function with the filename as the argument:
    ```python
    result = csv_columns('exam.csv')
    print(result)
    ```
3. The result will be printed as a dictionary where each key is a column name, and each value is a list of values from that column.

### Example:

For the following content in `exam.csv`:

```
name,grade
Timur,5
Arthur,4
Anri,5
```

Running `csv_columns('exam.csv')` will return:

```python
{
    'name': ['Timur', 'Arthur', 'Anri'],
    'grade': ['5', '4', '5']
}
```

## Conclusion 🚀

This program provides a simple way to read `CSV` files and extract columns into a dictionary format.
It preserves the original order of columns and their elements, making it a useful tool for various data processing tasks.
