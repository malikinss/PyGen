# Swap Keys and Values in Months Dictionary 📖

## Description 📝

This program swaps the keys and values of a dictionary where the keys are integers representing the months (1 to 12), and the values are the corresponding month names.
The output is a new dictionary where the month names become the keys and their respective numbers become the values.

## Purpose 🎯

The goal of this program is to demonstrate how to manipulate a dictionary by swapping its keys and values using a dictionary comprehension.

## How It Works 🔍

1. **Input**:
    - A dictionary where the keys are integers (representing the month numbers from 1 to 12) and the values are the corresponding month names as strings.
2. **Processing**:
    - The program uses a dictionary comprehension to swap the keys and values of the given dictionary. It iterates over the original dictionary and creates a new dictionary where the keys are month names and the values are the corresponding month numbers.
3. **Output**:
    - The program returns a new dictionary with the month names as keys and the month numbers as values.

## Output 📜

The program outputs a dictionary where the month names are the keys, and their corresponding month numbers are the values.

### Example Input/Output:

**Input**:

```python
months = {
    1: 'January', 2: 'February', 3: 'March',
    4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September',
    10: 'October', 11: 'November', 12: 'December'
}
```

**Output**:

```python
{
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}
```

## Usage 📦

1. Copy the code into a Python file (e.g., `swap_months.py`).
2. Call the `swap_months()` function, passing the dictionary of months as an argument.
3. The program will return a new dictionary with swapped keys and values.

### Example Run:

```python
# Sample run
months = {
    1: 'January', 2: 'February', 3: 'March',
    4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September',
    10: 'October', 11: 'November', 12: 'December'
}
result = swap_months(months)
print(result)
```

**Output**:

```python
{
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}
```

## Conclusion 🚀

This program effectively swaps the keys and values of a dictionary and is an excellent example of using dictionary comprehension to manipulate data. It is useful for tasks where reversing the order of key-value pairs is needed.
