# Filter Favorite Numbers Dictionary 📖

## Description 📝

This program filters out entries from a dictionary of favorite numbers, keeping only the ones where the values are two-digit numbers (between 10 and 99 inclusive).

## Purpose 🎯

The purpose of this program is to demonstrate how to filter a dictionary based on a condition (two-digit numbers) using a generator expression inside a dictionary comprehension.

## How It Works 🔍

1. **Input**:
    - A dictionary where the keys are names and the values are favorite numbers.
    - Some of the values are single-digit or multi-digit numbers.
2. **Processing**:
    - The program uses a helper function `is_two_digit()` to check if a number is a two-digit number (between 10 and 99 inclusive).
    - It then filters out the key-value pairs where the value is a two-digit number using a dictionary comprehension.
3. **Output**:
    - The program returns a new dictionary containing only the key-value pairs where the value is a two-digit number.

## Output 📜

The program outputs a dictionary that contains only the names and their corresponding two-digit favorite numbers.

### Example Input/Output:

**Input**:

```python
favorite_numbers = {
    'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123,
    'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36,
    'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89,
    'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777,
    'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404,
    'olga': 271, 'anna': 55, 'madlen': 876
}
```

**Output**:

```python
{
    'timur': 17, 'larisa': 19, 'ronald': 76, 'dorothy': 62, 'harold': 36,
    'rosaly': 18, 'rustam': 89, 'sveta': 75, 'anna': 55
}
```

## Usage 📦

1. Copy the code into a Python file (e.g., `filter_favorite_numbers.py`).
2. Call the `filter_favorite_numbers()` function, passing the dictionary of favorite numbers as an argument.
3. The program will return a new dictionary with only the entries where the value is a two-digit number.

### Example Run:

```python
# Sample run
favorite_numbers = {
    'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123,
    'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36,
    'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89,
    'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777,
    'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404,
    'olga': 271, 'anna': 55, 'madlen': 876
}
result = filter_favorite_numbers(favorite_numbers)
print(result)
```

**Output**:

```python
{
    'timur': 17, 'larisa': 19, 'ronald': 76, 'dorothy': 62, 'harold': 36,
    'rosaly': 18, 'rustam': 89, 'sveta': 75, 'anna': 55
}
```

## Conclusion 🚀

This program effectively filters out favorite numbers that are not two-digit numbers and returns a clean dictionary of valid entries.
It demonstrates how to apply conditions within a dictionary comprehension to manipulate data efficiently.
