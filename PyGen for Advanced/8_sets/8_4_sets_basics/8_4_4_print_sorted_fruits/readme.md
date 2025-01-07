# Fruit Sorting Program 🍎🍍🍌

## Description 📝

This program takes a set of fruit names and prints each fruit on a new line in reverse lexicographic order.
By utilizing Python’s `sorted` function with the `reverse=True` flag, the program arranges the fruit names from Z to A.

## Purpose 🎯

-   To demonstrate how to sort and display set elements in reverse order.
-   To reinforce knowledge of Python's `sorted()` function and set operations.

## How It Works 🔍

1. **Function `print_sorted_fruits`**:

    - Accepts a set of fruit names as input.
    - Sorts the set in reverse lexicographic order.
    - Prints each fruit on a new line.

2. **Set Initialization**:

    - A set of fruit names is initialized with some duplicates.
    - The set automatically filters out duplicates.

3. **Result Printing**:
    - The sorted list of fruits is printed line by line using unpacking and `sep="\n"`.

### Example:

```python
fruits = {
    'apple', 'banana', 'cherry', 'avocado',
    'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'
}
print_sorted_fruits(fruits)
```

**Output**:

```
pineapple
grapefruit
cherry
banana
avocado
apricot
apple
```

## Output 📜

-   The program prints the fruits in reverse order (Z to A).
-   Since the input is a set, any duplicate fruits (like 'banana' and 'avocado') are automatically removed.

## Conclusion 🚀

This program highlights the power of Python’s set and sorting capabilities to efficiently manipulate and display data.
It's a practical example of how simple operations can lead to clean and organized output.
