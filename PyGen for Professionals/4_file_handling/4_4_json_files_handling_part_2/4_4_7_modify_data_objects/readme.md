# Data Modifier Program 📝

## Description 📝

This program reads a JSON list from the `data.json` file and processes its objects based on a set of predefined rules.
It then writes the modified list to a new file `updated_data.json`.
The program ensures that objects are transformed according to their type, such as adding an exclamation mark to strings or inverting booleans.

## Purpose 🎯

The goal of this program is to apply specific transformations to a list of objects in JSON format and save the updated data for further use.
This can be useful for handling data preparation tasks, applying rules to different types of values, or manipulating structured data before processing.

## How It Works 🔍

1. The program first reads the JSON data from the `data.json` file using the `read_json_data_from_file()` function.
2. It processes each element of the list based on its type:
    - Strings are appended with an exclamation mark.
    - Numbers are incremented by one.
    - Booleans are inverted.
    - Lists are doubled.
    - JSON objects (dictionaries) are modified by adding a `"newkey": null` pair.
    - `null` values are ignored.
3. The modified data is then written to a new file `updated_data.json` using the `write_json_data_to_file()` function.

## Output 📜

### Example:

Input (in `data.json`):

```json
["Hello", 179, true, null, [1, 2, 3], { "key": "value" }]
```

Output (in `updated_data.json`):

```json
["Hello!", 180, false, [1, 2, 3, 1, 2, 3], { "key": "value", "newkey": null }]
```

## Usage 📦

1. Ensure that the `data.json` file exists and contains a list of objects.
2. Run the program, and it will process the list according to the specified rules.
3. The modified list will be written to the `updated_data.json` file.

## Conclusion 🚀

This utility is ideal for transforming data objects in a structured way, applying specific rules to different types, and saving the results in a new file.
