# Find Divisors of Numbers 📖

## Description 📝

This program takes a list of integers and returns a dictionary where each integer is a key, and the value is a sorted list of its divisors in ascending order, starting with 1.

## Purpose 🎯

The purpose of this program is to generate a dictionary where each number from a list is associated with its divisors. The divisors are listed in ascending order, which can be useful in a variety of mathematical and computational problems.

## How It Works 🔍

1. **Input**:
    - A list of integers.
2. **Processing**:
    - For each number in the list, the program generates a list of its divisors by iterating over the range from 1 to the number itself.
    - It checks which values divide the number evenly (i.e., no remainder).
3. **Output**:
    - The program outputs a dictionary where the keys are the numbers and the values are the sorted lists of divisors for those numbers.

## Output 📜

The program outputs a dictionary where the numbers from the input list are the keys, and the corresponding values are lists containing the divisors of the number.

### Example Input/Output:

**Input**:

```python
numbers = [1, 6, 18]
```

**Output**:

```python
{
    1: [1],
    6: [1, 2, 3, 6],
    18: [1, 2, 3, 6, 9, 18]
}
```

## Usage 📦

1. Copy the code into a Python file (e.g., `find_divisors.py`).
2. Call the `find_divisors()` function, passing a list of numbers as an argument.
3. The function will return a dictionary with each number as the key and its divisors as a sorted list of values.

### Example Run:

```python
# Sample run
numbers = [34, 10, 4, 6, 10, 23]
result = find_divisors(numbers)
print(result)
```

**Output**:

```python
{
    34: [1, 2, 17, 34],
    10: [1, 2, 5, 10],
    4: [1, 2, 4],
    6: [1, 2, 3, 6],
    10: [1, 2, 5, 10],
    23: [1, 23]
}
```

## Conclusion 🚀

This program effectively calculates the divisors of a given list of numbers and organizes them into a dictionary format. It can be useful for mathematical analysis, number theory exploration, or any task requiring knowledge of divisors.
