# Named Tuple: Animal Records from Pickle File 📝

## Description 📝

This program processes a pickle file that contains a serialized list of named tuples, where each tuple holds data about an animal.
The data consists of four fields: `name`, `family`, `sex`, and `color`.
The program then deserializes this list and prints the fields and their values in a specified format.

## Purpose 🎯

The purpose of the program is to:

-   Deserialize a pickle file containing a list of `Animal` named tuples.
-   For each tuple, print the field names and their corresponding values.
-   Ensure there is an empty line between each tuple's data.

## How It Works 🔍

1. **Deserialize the pickle file**: The program loads the list of `Animal` named tuples from a given file path using the `pickle` module.
2. **Print the fields and values**: It iterates over the list of `Animal` named tuples, printing each field name and value in the specified format.
3. **Ensure formatting**: An empty line is added between the records of different animals.

### Example Input (data.pkl)

```python
[
    Animal(name='Alex', family='dogs', sex='m', color='brown'),
    Animal(name='Nancy', family='dogs', sex='w', color='black')
]
```

### Example Output

```
name: Alex
family: dogs
sex: m
color: brown

name: Nancy
family: dogs
sex: w
color: black
```

## Output 📜

The output consists of the fields and their corresponding values printed for each animal, with an empty line between records.

## Usage 📦

To use the program, ensure the following:

1. The pickle file (`data.pkl`) contains a serialized list of `Animal` named tuples.
2. The program will automatically deserialize and process this file.

### Example:

```bash
$ python animal_records.py
```

### Expected Output (based on the example pickle data)

```
name: Alex
family: dogs
sex: m
color: brown

name: Nancy
family: dogs
sex: w
color: black
```

## Conclusion 🚀

This program demonstrates how to deserialize a pickle file and iterate through a list of named tuples to display their fields and values in a readable format.
The approach ensures flexibility and clarity in processing serialized data.
