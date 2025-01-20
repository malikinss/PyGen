# Filter Letters Dictionary 📖

## Description 📝

This program takes a dictionary of letter mappings and a list of keys to be removed.
It then returns a new dictionary with the entries whose keys are not in the list of keys to be excluded.

## Purpose 🎯

The purpose of this program is to provide an easy way to filter out specific key-value pairs from a dictionary.
It can be useful for tasks that require removing unwanted entries from a dictionary based on certain conditions.

## How It Works 🔍

1. **Input**:
    - A dictionary `letters` where keys are integers and values are characters.
    - A list `remove_keys` that contains the keys to be excluded from the dictionary.
2. **Processing**:
    - The program iterates over the dictionary and filters out any key-value pairs where the key is in the `remove_keys` list.
3. **Output**:
    - The program returns a new dictionary with only the key-value pairs where the key is not in the `remove_keys` list.

## Output 📜

The program outputs a filtered dictionary that excludes the entries with the specified keys.

### Example Input/Output:

**Input**:

```python
letters = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
    5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
    15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
    20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'
}
remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
```

**Output**:

```python
{
    0: 'A', 2: 'C', 3: 'D', 4: 'E',
    6: 'G', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
    13: 'N', 14: 'O', 15: 'P', 16: 'Q', 18: 'S',
    20: 'U', 22: 'W', 23: 'X', 26: 'Z'
}
```

## Usage 📦

1. Copy the code into a Python file (e.g., `filter_letters.py`).
2. Call the `filter_letters()` function, passing a dictionary of letters and a list of keys to be removed.
3. The function will return a new dictionary with the filtered key-value pairs.

### Example Run:

```python
# Sample run
letters = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
    5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
    15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
    20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'
}
remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
result = filter_letters(letters, remove_keys)
print(result)
```

**Output**:

```python
{
    0: 'A', 2: 'C', 3: 'D', 4: 'E',
    6: 'G', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
    13: 'N', 14: 'O', 15: 'P', 16: 'Q', 18: 'S',
    20: 'U', 22: 'W', 23: 'X', 26: 'Z'
}
```

## Conclusion 🚀

This program efficiently filters a dictionary, removing unwanted key-value pairs based on specified keys.
It can be easily integrated into other programs that require dictionary manipulation.
