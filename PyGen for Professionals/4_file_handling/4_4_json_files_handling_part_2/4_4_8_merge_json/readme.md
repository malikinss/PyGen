# JSON Merger Program 📝

## Description 📝

This program reads two JSON files (`data1.json` and `data2.json`), merges the JSON objects inside them, and writes the resulting merged object to a new file (`data_merge.json`).
If there are any matching keys between the two JSON objects, the value from the second file is taken.
The order of the elements in the resulting object can vary.

## Purpose 🎯

The purpose of this program is to combine two JSON objects into a single object while resolving conflicts by prioritizing the values from the second file.
This is useful for consolidating data from different sources or updating a dataset with more recent information.

## How It Works 🔍

1. The program reads the data from two input JSON files (`data1.json` and `data2.json`) using the `read_json_file()` function.
2. It merges the data using the `merge_data()` function, where the second dataset will overwrite any matching keys from the first.
3. The merged result is written to a new file (`data_merge.json`) using the `write_json_file()` function.

### Key Details:

-   `data1.json` and `data2.json` are expected to contain JSON objects.
-   If both files contain the same key, the value from the second file (`data2.json`) will be used in the merged result.

## Output 📜

### Example:

#### Input files:

`data1.json`:

```json
{
    "Timur": 99,
    "Anri": 97
}
```

`data2.json`:

```json
{
    "Dima": 99,
    "Anri": 100
}
```

#### Output in `data_merge.json`:

```json
{
    "Anri": 100,
    "Dima": 99,
    "Timur": 99
}
```

(Note: The order of the elements may vary.)

## Usage 📦

1. Place your JSON data in the `data1.json` and `data2.json` files.
2. Run the program, and it will merge the two JSON objects into one.
3. The merged JSON object will be saved in the `data_merge.json` file.

## Conclusion 🚀

This utility is designed to merge two JSON objects efficiently, resolving key conflicts by favoring values from the second JSON object.
It provides an easy way to consolidate or update data without manually handling conflicts.
