# Pickle Filter Dump 📝

## Description 📝

This program defines a function `filter_dump()` that filters a list of arbitrary objects based on their type and serializes the filtered result to a pickle file.
The pickle file contains only those objects that match the specified type.

## Purpose 🎯

The purpose of this function is to allow selective serialization of objects based on their type.
It can be useful for cases where you need to store only a specific type of data from a larger collection.

## How It Works 🔍

1. The `filter_dump()` function receives three arguments:
    - `filename`: the name of the pickle file where the filtered data will be saved.
    - `objects`: a list containing arbitrary objects.
    - `typename`: the type to filter the objects by.
2. The function filters the `objects` list, keeping only those elements that match the specified `typename`.
3. The filtered list is then serialized and saved into the specified `filename` using `pickle.dump()`.

## Output 📜

The output is a pickle file that contains the serialized list of objects that match the given type.

### Example:

**Input:**

```python
filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
```

**Output:**  
A file named `numbers.pkl` is created containing the serialized list:

```python
[1, 3, 4]
```

## Usage 📦

1. Call the `filter_dump()` function with the following arguments:
    - The desired filename for the pickle file.
    - A list of objects (e.g., integers, strings, etc.).
    - The type to filter by (e.g., `int`, `str`).
2. The function will filter the objects based on the specified type and save the result to the provided file.

## Conclusion 🚀

This function provides a way to filter and serialize data by type, making it easy to save only the relevant objects to a file for further processing or storage.
