# JSON Key Adder Program 📝

## Description 📝

This program processes a JSON file containing a list of JSON objects, adds any missing keys from other objects, and assigns `null` (or `None` in Python) to those missing keys.
The modified list of JSON objects is then written to a new file (`updated_people.json`).
The program preserves the original order of the objects and does not alter the order of keys within each object.

## Purpose 🎯

The purpose of this program is to ensure that all JSON objects in a list have the same set of keys, adding `null` for any key that is missing from a specific object.
This can be useful for ensuring consistency in data or preparing data for processing where all objects need to have the same attributes.

## How It Works 🔍

1. The program reads the JSON data from the `people.json` file.
2. It retrieves a complete list of all keys present in any of the objects using the `get_all_existing_keys()` function.
3. It then iterates through the list of objects, adding any missing keys with a `null` value using the `add_missing_keys()` function.
4. The updated list of objects is written to the `updated_people.json` file.

### Key Details:

-   `people.json` contains a list of JSON objects, where each object may have a different set of keys.
-   The program adds any missing keys to each object and assigns `null` (or `None` in Python) to them.

## Output 📜

### Example:

#### Input (`people.json`):

```json
[
    {
        "age": 33,
        "country": "Lesotho"
    },
    {
        "age": 25,
        "country": "Guinea",
        "name": "Dorey"
    }
]
```

#### Output (`updated_people.json`):

```json
[
    {
        "age": 33,
        "country": "Lesotho",
        "name": null
    },
    {
        "age": 25,
        "country": "Guinea",
        "name": "Dorey"
    }
]
```

(Note: The order of keys inside each object is not guaranteed to remain the same, but the order of objects is preserved.)

## Usage 📦

1. Make sure the `people.json` file is present with the list of objects.
2. Run the program to process the data.
3. The program will output the updated JSON objects with missing keys added to `updated_people.json`.

## Conclusion 🚀

This program is designed to standardize the structure of JSON objects by ensuring each object contains all possible keys.
It is helpful when dealing with incomplete or inconsistent datasets, ensuring all entries are consistent before further processing.
