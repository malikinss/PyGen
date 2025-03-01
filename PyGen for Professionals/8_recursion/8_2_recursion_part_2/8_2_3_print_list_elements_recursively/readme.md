# List Element Printer (Recursive)

## Description 📝

This program prints all the elements of a list `numbers` containing 100 integers, from the first element to the last, each on a separate line in the format:

```
Element <index>: <value>
```

The function `print_list_elements_recursively()` recursively traverses the list and prints each element along with its index.

## Purpose 🎯

The goal of this program is to demonstrate the use of recursion to print all elements of a list, where each element is displayed with its index in the specified format.
This approach is useful for understanding how recursion can be applied to iterate over a collection.

## How It Works 🔍

1. The function `print_list_elements_recursively()` calls a helper function `print_element_recursive(index)` with an initial index of 0.
2. In `print_element_recursive()`, if the current index is within the bounds of the list, it prints the element at that index in the format `Element <index>: <value>`.
3. Then, it recursively calls itself with the next index (index + 1).
4. This continues until the base case is met, where the index exceeds the length of the list.

## Output 📜

The output consists of the printed elements of the list, each shown on a new line with its index:

```
Element 0: 243
Element 1: -279
Element 2: 395
...
Element 99: 430
```

## Usage 📦

1. Call the `print_list_elements_recursively(elements)` function, passing a list of integers.
2. The function will recursively print each element with its corresponding index in the list.

### Example:

```python
print_list_elements_recursively(numbers)
```

**Output:**

```
Element 0: 243
Element 1: -279
Element 2: 395
Element 3: 130
...
Element 99: 430
```

## Conclusion 🚀

This solution uses recursion to traverse and print the elements of a list.
Recursion is an elegant way to iterate through a sequence, especially in cases where a straightforward iterative loop might not be the most intuitive solution.
