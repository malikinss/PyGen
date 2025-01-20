# Parse Number:Word Pairs into Dictionary 📖

## Description 📝

This program takes a string of space-separated `number:word` pairs and converts it into a dictionary. The numbers from the string become the dictionary keys (as integers), and the corresponding words become the values (as strings).

## Purpose 🎯

The purpose of this program is to demonstrate how to parse and process a string of number:word pairs and convert it into a dictionary format suitable for further usage.

## How It Works 🔍

1. **Input**:
    - A string containing space-separated number:word pairs, where each pair is in the format `number:word`.
2. **Processing**:
    - The program first splits the input string into individual number:word pairs.
    - Then, each pair is further split by the `:` delimiter.
    - The numbers are converted to integers, and the words are used as strings to form the dictionary.
3. **Output**:
    - The program returns a dictionary with integer keys (numbers) and string values (words).

## Output 📜

The program outputs a dictionary where the numbers from the input string are the keys and the corresponding words are the values.

### Example Input/Output:

**Input**:

```python
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
```

**Output**:

```python
{
    1: 'men', 2: 'kind', 90: 'number', 0: 'sun', 34: 'book',
    56: 'mountain', 87: 'wood', 54: 'car', 3: 'island', 88: 'power',
    7: 'box', 17: 'star', 101: 'ice'
}
```

## Usage 📦

1. Copy the code into a Python file (e.g., `parse_string.py`).
2. Call the `parse_string_to_dict()` function, passing the string `s` as an argument.
3. The function will return a dictionary with integers as keys and strings as values.

### Example Run:

```python
# Sample run
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = parse_string_to_dict(s)
print(result)
```

**Output**:

```python
{
    1: 'men', 2: 'kind', 90: 'number', 0: 'sun', 34: 'book',
    56: 'mountain', 87: 'wood', 54: 'car', 3: 'island', 88: 'power',
    7: 'box', 17: 'star', 101: 'ice'
}
```

## Conclusion 🚀

This program efficiently converts a string of number:word pairs into a dictionary, demonstrating simple string manipulation and dictionary comprehension. It’s a useful tool when working with formatted data that needs to be processed into a structured format.
