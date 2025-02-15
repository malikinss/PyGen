# `CSV` Condensation Tool 📝

## Description 📝

This Python script processes `CSV` files that contain object properties, condensing the data into a more readable and structured format.
The script reads a `CSV` file with object properties and generates a new `CSV` where each object is represented by a single row, and each property appears as a column.

## Purpose 🎯

The main goal of the script is to transform a `CSV` file with repetitive data into a more concise and structured format.
It groups the data by object names and arranges their properties in corresponding columns.

## How It Works 🔍

1. **Reading Input**: The `read_csv_file()` function reads the original `CSV` file with the data.
2. **Extracting Unique IDs**: The `extract_ids()` function extracts unique object names from the first column.
3. **Generating Headers**: The `extract_headers()` function generates the header row by combining the object properties.
4. **Building Records**: The `create_records()` function arranges the data into dictionaries, organizing it by unique object names and properties.
5. **Writing Output**: The `write_csv()` function writes the processed data to a new `CSV` file with the condensed format.

## Output 📜

The output `CSV` file will contain a column for object names (`id_name`) followed by columns for each property of the objects. For example:

```csv
ID,color,size,notes
ball,purple,4,it's round
cup,blue,1,none
```

## Usage 📦

1. Place the input `CSV` file (e.g., `data.csv`) in the same directory as the script.
2. Ensure that the input file follows the expected format: each line contains an object name, property, and its value.
3. Run the script with the desired ID column name:
    ```python
    condense_csv('data.csv', id_name='ID')
    ```
4. The script will create a `condensed.csv` file with the transformed data.

## Conclusion 🚀

This script helps to process and condense `CSV` files that contain object data with repetitive properties, transforming them into a clean and readable format suitable for analysis or further processing.
