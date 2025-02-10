# Find Duplicate Numbers Function

## Description 📝

The `find_duplicate_numbers()` function takes a sequence of non-negative integers, identifies the numbers that occur more than once, and returns them in ascending order without repetitions.

## Purpose 🎯

This function is useful for:

-   Finding and displaying duplicate numbers in a given sequence.
-   Returning a sorted list of numbers that appear more than once, with no duplicates in the output.

## How It Works 🔍

1. The function first converts the space-separated string of integers into a list of integers.
2. It then counts the occurrences of each number in the list.
3. The function extracts all numbers that occur more than once.
4. Finally, it sorts the numbers in ascending order and returns them.

If there are no duplicates in the input sequence, the function returns an empty result.

## Output 📜

Example usage and expected outputs:

```python
find_duplicate_numbers("1 2 3 4 2 5 6 7 8 9 10 2")
# Input: "1 2 3 4 2 5 6 7 8 9 10 2"
# Output: [2]

find_duplicate_numbers("10 20 30 40 50 60 70 80 90 100")
# Input: "10 20 30 40 50 60 70 80 90 100"
# Output: []

find_duplicate_numbers("5 6 7 5 8 9 5 10 11")
# Input: "5 6 7 5 8 9 5 10 11"
# Output: [5]
```

## Usage 📦

1. Clone this repository.
2. Navigate to the project directory.
3. Use the function in your script or interactive Python shell.

Example:

```python
from find_duplicates import find_duplicate_numbers

input_data = "1 2 3 4 2 5 6 7 8 9 10 2"
duplicates = find_duplicate_numbers(input_data)
print(" ".join(map(str, duplicates)))  # Output: 2
```

## Conclusion 🚀

The `find_duplicate_numbers()` function helps efficiently identify duplicate numbers in a sequence and returns them sorted without repetitions.
It is particularly useful for analyzing datasets to detect redundancy or repetitive values.
