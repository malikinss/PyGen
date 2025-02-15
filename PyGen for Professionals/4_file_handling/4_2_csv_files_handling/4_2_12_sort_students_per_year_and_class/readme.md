# Student Counts Sorting Tool 📝

## Description 📝

This Python script processes a `CSV` file containing student count data for various classes and years.
It sorts the data based on the class names in ascending order, where the classes are in the format `<class number>-<class letter>`.
The final output `CSV` will have columns sorted first by the class number and then alphabetically by the class letter.

## Purpose 🎯

The purpose of this script is to take raw student data and rearrange it in a more organized format, making it easier to analyze.
It sorts the classes numerically by their number and alphabetically by their letter, and writes the result to a new `CSV` file.

## How It Works 🔍

1. **Reading Input**: The `read_csv()` function reads the student data `CSV` file and returns it as a list of dictionaries.
2. **Sorting Columns**: The `sort_headers()` function sorts the class columns in ascending order, first by class number and then by class letter.
3. **Sorting Rows**: The `sort_rows()` function rearranges the rows based on the newly sorted class headers.
4. **Writing Output**: The `write_csv()` function writes the sorted data to a new `CSV` file (`sorted_student_counts.csv`).

## Output 📜

The output `CSV` file will contain the sorted columns with years and student counts for each class. The columns will be sorted first by class number and then alphabetically by the class letter. For example:

```csv
year,1-A,1-B,2-A,2-B,3-A,3-B,...
2000,22,17,29,20,30,19,...
2001,22,20,20,27,28,22,...
...
```

## Usage 📦

1. Ensure that the input `CSV` file (e.g., `student_counts.csv`) is in the same directory as the script.
2. Place the student count data in the expected format: `year,class number-class letter`.
3. Run the script to generate the `sorted_student_counts.csv` file:
    ```python
    sort_and_rearrange_data('student_counts.csv')
    ```
4. The script will produce a new `CSV` file (`sorted_student_counts.csv`) with sorted columns and data.

## Conclusion 🚀

This script is useful for reorganizing student count data in a way that makes it easier to analyze by sorting the columns based on class number and letter.
