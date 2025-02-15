# `CSV` Sorting Program

## Description 📝

This program reads data from a `CSV` file and sorts the content based on a specified column.
The program can handle both numeric and string data types, sorting them accordingly:

-   numerically for numbers and lexicographically for strings.

If two rows have the same values in the sorting column, their original order is preserved.

## Purpose 🎯

The purpose of this program is to demonstrate how to:

-   Read data from a `CSV` file.
-   Sort data by a specific column.
-   Handle both numerical and string data types for sorting.
-   Ensure that the order of rows with equal values remains unchanged.

## How It Works 🔍

1. The user is prompted to input the column number they want to sort by (column numbering starts at 1).
2. The `CSV` file is read, and its content is loaded into memory.
3. The data is sorted based on the chosen column, either numerically or lexicographically.
4. The sorted content is printed back to the user.

## Output 📜

The program will print the sorted data to the terminal, where each row from the `CSV` file is displayed in the same format (comma-separated).

Example:

```
purple,1
blue,3
red,4
green,28
```

## Usage 📦

1. Make sure you have a `CSV` file (e.g., `deniro.csv`) ready for sorting.
2. Run the program.
3. When prompted, enter the column number you want to sort by (1-based index).
4. The sorted data will be displayed in the terminal.

### Example:

For a file with the following content:

```
red,4
blue,3
green,28
purple,1
```

If you want to sort by the second column (numerically), enter `2` when prompted, and the output will be:

```
purple,1
blue,3
red,4
green,28
```

## Conclusion 🚀

This program is a simple yet effective way to manage and sort `CSV` data based on user-defined criteria.
It can be easily extended to handle more complex sorting requirements and is a useful tool for any task involving `CSV` data manipulation.
