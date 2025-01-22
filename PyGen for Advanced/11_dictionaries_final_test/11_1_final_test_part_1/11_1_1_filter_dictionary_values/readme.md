# Filter Dictionary Values 🧹

## Description 📝

This program modifies the given dictionary in place by removing values greater than 20 from the lists of values, while keeping the order of the remaining elements intact.

## Purpose 🎯

The goal of this program is to filter out all values greater than 20 from the lists in the dictionary, without altering the original order of the elements in each list.

## How It Works 🔍

1. **Input**:
    - A dictionary `my_dict` where each key is a string, and each value is a list of integers.
2. **Processing**:
    - The program iterates over the dictionary.
    - For each key-value pair, the program filters out any number greater than 20 from the list while preserving the order of the remaining numbers.
3. **Output**:
    - The dictionary is modified in place, with all lists containing only numbers less than or equal to 20.

## Output 📜

There is no direct output produced by this function. The input dictionary `my_dict` is modified in place.

### Example Input/Output:

**Input**:

```python
my_dict = {
    'C1': [10, 20, 30, 7, 6, 23, 90],
    'C2': [20, 30, 40, 1, 2, 3, 90, 12],
    'C3': [12, 34, 20, 21],
    'C4': [22, 54, 209, 21, 7],
    'C5': [2, 4, 29, 21, 19],
    'C6': [4, 6, 7, 10, 55],
    'C7': [4, 8, 12, 23, 42],
    'C8': [3, 14, 15, 26, 48],
    'C9': [2, 7, 18, 28, 18, 28]
}
```

**Output** (after applying the filtering function):

```python
{
    'C1': [10, 20, 7, 6],
    'C2': [20, 1, 2, 3, 12],
    'C3': [12, 20],
    'C4': [7],
    'C5': [2, 4, 19],
    'C6': [4, 6, 7, 10],
    'C7': [4, 8, 12],
    'C8': [3, 14, 15],
    'C9': [2, 7, 18, 18]
}
```

## Usage 📦

1. Copy the code into a Python file (e.g., `filter_dictionary_values.py`).
2. Pass the dictionary `my_dict` to the `filter_dictionary_values()` function.
3. The function will modify `my_dict` in place, removing any values greater than 20.

### Example Run:

```python
# Sample run
my_dict = {
    'C1': [10, 20, 30, 7, 6, 23, 90],
    'C2': [20, 30, 40, 1, 2, 3, 90, 12],
    'C3': [12, 34, 20, 21],
    'C4': [22, 54, 209, 21, 7],
    'C5': [2, 4, 29, 21, 19],
    'C6': [4, 6, 7, 10, 55],
    'C7': [4, 8, 12, 23, 42],
    'C8': [3, 14, 15, 26, 48],
    'C9': [2, 7, 18, 28, 18, 28]
}

filter_dictionary_values(my_dict)
print(my_dict)
```

**Output**:

```python
{
    'C1': [10, 20, 7, 6],
    'C2': [20, 1, 2, 3, 12],
    'C3': [12, 20],
    'C4': [7],
    'C5': [2, 4, 19],
    'C6': [4, 6, 7, 10],
    'C7': [4, 8, 12],
    'C8': [3, 14, 15],
    'C9': [2, 7, 18, 18]
}
```

## Conclusion 🚀

This program provides a simple way to clean up the data in a dictionary by removing numbers greater than 20 from each list, making it easier to work with smaller datasets or apply further processing.
