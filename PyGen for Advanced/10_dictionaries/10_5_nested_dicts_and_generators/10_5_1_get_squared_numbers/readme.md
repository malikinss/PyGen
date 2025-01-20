# Dictionary of Squared Numbers 📖

## Description 📝

This program generates a dictionary where the key is the position (index) of a number in the input list, and the value is the square of that number. The dictionary is created using a generator expression, which efficiently iterates through the list of numbers.

## Purpose 🎯

The purpose of this program is to demonstrate how to use a generator expression to build a dictionary from a list of numbers. It helps understand how to map list indices to corresponding squared values.

## How It Works 🔍

1. **Input**:
    - The program accepts a list of integers.
2. **Processing**:
    - It uses a generator expression with the `enumerate()` function to iterate through the list. For each element, it stores the index as the key and the square of the number as the value.
3. **Output**:
    - The result is a dictionary where the keys are the indices (starting from 0) and the values are the squares of the numbers.

## Output 📜

The program outputs a dictionary mapping indices to the squares of numbers.

### Example Input/Output:

**Input**:

```python
numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
```

**Output**:

```python
{
    0: 1156, 1: 100, 2: 16, 3: 36, 4: 100, 5: 529, 6: 8100, 7: 10000,
    8: 441, 9: 1225, 10: 9025, 11: 1, 12: 1296, 13: 1444, 14: 361, 15: 1,
    16: 36, 17: 7569
}
```

## Usage 📦

1. Copy the code into a Python file (e.g., `squared_dict.py`).
2. Call the `get_squared_numbers` function, passing a list of integers as an argument.
3. The program will return a dictionary with the index as the key and the squared value as the corresponding value.

### Example Run:

```python
# Sample run
numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
result = get_squared_numbers(numbers)
print(result)
```

**Output**:

```python
{
    0: 1156, 1: 100, 2: 16, 3: 36, 4: 100, 5: 529, 6: 8100, 7: 10000,
    8: 441, 9: 1225, 10: 9025, 11: 1, 12: 1296, 13: 1444, 14: 361, 15: 1,
    16: 36, 17: 7569
}
```

## Conclusion 🚀

This program demonstrates a simple but powerful technique for creating a dictionary based on indices and values using Python's generator expressions and the `enumerate()` function. It offers an efficient way to process and transform a list into a dictionary.
