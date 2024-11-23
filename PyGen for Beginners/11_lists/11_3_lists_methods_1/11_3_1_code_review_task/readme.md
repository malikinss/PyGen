# Code Review Task 19 🪲

## Description 📝

This task edits the given Python code to:

1. Display the length of the list `numbers`.
2. Display the last element of the list.
3. Display the list in reverse order.
4. Print `YES` if the list contains the numbers 5 and 17, and `NO` otherwise.
5. Output a list with the first and last elements removed.

## Purpose 🎯

The purpose of this program is to:

1. Demonstrate how to manipulate lists, including checking for values, reversing, and modifying the list.
2. Practice using Python's list indexing and slicing features.

## How It Works 🔍

-   The program performs the following tasks on the `numbers` list:
    1. Displays the length of the list using `len()`.
    2. Displays the last element using negative indexing `numbers[-1]`.
    3. Displays the reversed list using slicing `[::-1]`.
    4. Checks if both 5 and 17 are in the list using the `in` operator, printing `YES` or `NO` accordingly.
    5. Removes the first and last elements using slicing and prints the modified list.

## Output 📜

-   The program prints the following outputs:
    1. The length of the list.
    2. The last element of the list.
    3. The reversed list.
    4. `YES` or `NO` depending on whether both 5 and 17 are in the list.
    5. The modified list with the first and last elements removed.

## Identified Errors in the Original Code 🕵🏾:

1. **Checking for the presence of 5 and 17**:

    - The original code didn't check for the presence of both numbers at once.
    - Fix: Combined the conditions using `and` to check if both numbers are in the list.

2. **Slicing to remove first and last elements**:
    - The original code didn't include the slicing part to remove the first and last elements.
    - Fix: Applied `numbers[1:-1]` to remove the first and last elements.

## Fixed Code 🛠:

```python
# List of numbers
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8,
           5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2,
           10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

# Display the length of the list
print(len(numbers))  # Length of the list

# Display the last element of the list
print(numbers[-1])  # Last element

# Display the list in reverse order
print(numbers[::-1])  # Reversed list

# Check if the list contains 5 and 17
if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')

# Remove the first and last elements from the list and display it
numbers = numbers[1:-1]
print(numbers)  # List after removing first and last elements
```

## Explanation of Changes 🧾:

1. **List Length**: Used `len(numbers)` to output the length of the list.
2. **Last Element**: Used `numbers[-1]` to display the last element of the list.
3. **Reversed List**: Used `numbers[::-1]` to display the list in reverse order.
4. **Check for 5 and 17**: Used `if 5 in numbers and 17 in numbers:` to check if both numbers exist in the list.
5. **Remove First and Last Elements**: Applied `numbers[1:-1]` to slice out the first and last elements of the list.

## Conclusion 🚀

This task covers various Python list manipulations, including checking for values, slicing, reversing, and modifying lists. It demonstrates how to achieve multiple tasks on a list efficiently.
