# Hash as Key Program

## Description 📝

This Python script implements a `hash_as_key()` function that takes a list of objects and returns a dictionary.
The dictionary uses the hash value of each object as a key, and the corresponding value is the object itself or a list of objects with the same hash value.
The function also ensures that objects with identical hash values are grouped together while maintaining their original order.

## Purpose 🎯

The goal of this program is to demonstrate how to create a dictionary with hash values as keys and objects as values.
It highlights handling hashable objects and managing collisions where multiple objects share the same hash value.
This exercise provides practice in using dictionaries and hash functions in Python.

## How It Works 🔍

1. **hash_as_key() Function**: Iterates over the list of objects and computes the hash value for each object.
2. **defaultdict**: A `defaultdict(list)` is used to automatically create a list for each new hash key, allowing multiple objects to be stored with the same hash value.
3. **Handling Single-Element Lists**: If only one object corresponds to a hash value, it is stored directly rather than in a list.
4. **Error Handling**: A `ValueError` is raised if an unhashable object is found.

## Output 📜

When the script is executed with the list `[-1, -2, -3, -4, -5]`, the output will be:

```
{-1: -1, -2: -2, -3: -3, -4: -4, -5: -5}
```

## Usage 📦

1. Save the code to a file named `hash_as_key.py`.
2. Create a list of objects (e.g., numbers, strings) that you want to hash.
3. Open a terminal or command prompt.
4. Navigate to the directory where the file is located.
5. Execute the script using the command:
    ```
    python hash_as_key.py
    ```
6. The program will display a dictionary with hash values as keys and objects (or lists of objects) as values.

## Conclusion 🚀

This program demonstrates the use of hash functions to group objects in a dictionary by their hash values.
It shows how to handle hash collisions and maintain the original order of objects.
