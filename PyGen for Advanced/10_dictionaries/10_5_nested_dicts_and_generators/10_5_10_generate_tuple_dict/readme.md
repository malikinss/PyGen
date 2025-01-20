# Generate Tuple Dictionary 🧑‍💻

## Description 📝

This program takes a list of tuples where each tuple contains three integers.
It generates a dictionary where the key is the first element of each tuple, and the value is a tuple of the remaining two elements.

## Purpose 🎯

The purpose of this program is to demonstrate how to transform a list of tuples into a dictionary, where the first element of each tuple becomes the key, and the remaining two elements form the value.

## How It Works 🔍

1. **Input**:
    - A list `tuples` containing tuples, each with three integers.
2. **Processing**:
    - The program iterates over the list and constructs a dictionary where:
        - The first integer of each tuple becomes the dictionary key.
        - The remaining two integers form a tuple that becomes the value for that key.
3. **Output**:
    - A dictionary where the key is the first element of each tuple, and the value is a tuple of the other two elements.

## Output 📜

The program outputs a dictionary with keys corresponding to the first element of each tuple and values as the remaining two elements of the tuple.

### Example Input/Output:

**Input**:

```python
tuples = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),
    (10, 11, 12), (13, 14, 15), (16, 17, 18),
    (19, 20, 21), (22, 23, 24), (25, 26, 27),
    (28, 29, 30), (31, 32, 33), (34, 35, 36)
]
```

**Output**:

```python
{
    1: (2, 3), 4: (5, 6), 7: (8, 9),
    10: (11, 12), 13: (14, 15), 16: (17, 18),
    19: (20, 21), 22: (23, 24), 25: (26, 27),
    28: (29, 30), 31: (32, 33), 34: (35, 36)
}
```

## Usage 📦

1. Copy the code into a Python file (e.g., `generate_tuple_dict.py`).
2. Call the `generate_tuple_dict()` function, passing a list of tuples, each containing three integers.
3. The function will return a new dictionary where the first element of each tuple is the key, and the value is a tuple with the remaining two elements.

### Example Run:

```python
# Sample run
tuples = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),
    (10, 11, 12), (13, 14, 15), (16, 17, 18),
    (19, 20, 21), (22, 23, 24), (25, 26, 27),
    (28, 29, 30), (31, 32, 33), (34, 35, 36)
]
result = generate_tuple_dict(tuples)
print(result)
```

**Output**:

```python
{
    1: (2, 3), 4: (5, 6), 7: (8, 9),
    10: (11, 12), 13: (14, 15), 16: (17, 18),
    19: (20, 21), 22: (23, 24), 25: (26, 27),
    28: (29, 30), 31: (32, 33), 34: (35, 36)
}
```

## Conclusion 🚀

This program efficiently transforms a list of tuples into a dictionary, making it easier to access the data based on the first element of each tuple.
It can be useful in various scenarios, such as processing structured data or transforming data for further analysis.
