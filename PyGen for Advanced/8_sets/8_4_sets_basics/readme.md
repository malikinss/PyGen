# Lesson 8_4: Sets in Python Basics 📚

## Description 📝

In this lesson, I cover fundamental set operations in Python, such as using built-in functions like `len()`, `sum()`, `min()`, `max()`, as well as the `in` membership operator.
The lesson also focuses on iterating through sets, formatting set outputs, comparing sets, and sorting them using Python's `sorted()` function.

## Purpose 🎯

The goal of this lesson is to:

-   Demonstrate how to use Python's built-in functions with sets.
-   Learn how to check if elements belong to a set using the `in` operator.
-   Understand how to iterate through sets and format the output.
-   Explore set comparisons and sorting using the `sorted()` function.

## Key Concepts 📚

### 1. Built-in Functions with Sets 🧑‍💻

Python provides several built-in functions for working with sets.
These include:

-   **`len()`**: Returns the number of elements in a set.
-   **`sum()`**: Calculates the sum of all elements in the set.
-   **`min()`**: Returns the smallest element in the set.
-   **`max()`**: Returns the largest element in the set.

Example:

```python
my_set = {1, 2, 3, 4, 5}
print(len(my_set))  # Output: 5
print(sum(my_set))  # Output: 15
print(min(my_set))  # Output: 1
print(max(my_set))  # Output: 5
```

### 2. Membership Operator `in` 🔍

The `in` operator is used to check if an element exists in a set.
Example:

```python
my_set = {1, 2, 3, 4}
print(3 in my_set)  # Output: True
print(5 in my_set)  # Output: False
```

### 3. Iterating through Sets 🔄

You can loop through the elements of a set using a `for` loop.
Since sets are unordered, the order of elements during iteration may vary.
Example:

```python
my_set = {1, 2, 3}
for elem in my_set:
    print(elem)
```

### 4. Formatting Set Output 🖨

The set elements can be displayed in a readable format using the `print()` function.
We can also format the output as needed.
Example:

```python
my_set = {1, 2, 3}
print(f"My set contains: {my_set}")  # Output: My set contains: {1, 2, 3}
```

### 5. Comparing Sets 🔍

Sets can be compared using the following operations:

-   **Union** (`|`): Combines two sets, removing duplicates.
-   **Intersection** (`&`): Returns elements that are present in both sets.
-   **Difference** (`-`): Returns elements present in the first set but not in the second.
-   **Symmetric Difference** (`^`): Returns elements that are in either set, but not in both.

Example:

```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a | set_b)  # Union: {1, 2, 3, 4, 5}
print(set_a & set_b)  # Intersection: {3}
print(set_a - set_b)  # Difference: {1, 2}
print(set_a ^ set_b)  # Symmetric Difference: {1, 2, 4, 5}
```

### 6. Sorting Sets with `sorted()` 🧮

Although sets are unordered, we can sort the elements using the `sorted()` function, which returns a sorted list.
Example:

```python
my_set = {5, 3, 8, 1}
sorted_set = sorted(my_set)
print(sorted_set)  # Output: [1, 3, 5, 8]
```

## Tasks 💻

### 1. [8_4_1_find_sum_of_min_max](#)

**Description 📝**: This program calculates the sum of the minimum and maximum values in a given set of floating-point numbers.  
**Purpose 🎯**: Compute the sum of the smallest and largest elements in a set using the `min()` and `max()` functions.

### 2. [8_4_2_calculate_arithmetic_mean](#)

**Description 📝**: This program calculates the arithmetic mean (average) of the elements in a given set of integers.  
**Purpose 🎯**: Compute the average of unique integers in a set using the `sum()` and `len()` functions.

### 3. [8_4_3_sum_of_squares](#)

**Description 📝**: This program calculates the sum of the squares of the elements in a given set of integers.  
**Purpose 🎯**: Compute the sum of squares of unique integers using list comprehensions and sets.

### 4. [8_4_4_print_sorted_fruits](#)

**Description 📝**: This program takes a set of fruit names and prints each fruit on a new line in reverse lexicographic order.  
**Purpose 🎯**: Sort and display set elements in reverse order using the `sorted()` function with the `reverse=True` flag.

### 5. [8_4_5_count_unique_chars](#)

**Description 📝**: This program takes a string of text as input and calculates the number of unique characters in that string using sets.  
**Purpose 🎯**: Count the number of unique characters by leveraging Python's `set`.

### 6. [8_4_6_has_unique_digits](#)

**Description 📝**: This program checks if all digits in a string are unique by using a set.  
**Purpose 🎯**: Check if a string of digits contains only unique digits.

### 7. [8_4_7_contains_all_digits](#)

**Description 📝**: This program checks if two strings contain every digit from 0 to 9 by using sets.  
**Purpose 🎯**: Ensure all digits from 0 to 9 are present in the combination of both strings.

### 8. [8_4_8_have_same_digit_set](#)

**Description 📝**: This program checks if two strings consist of the same set of digits, ignoring order and frequency.  
**Purpose 🎯**: Compare sets of digits between two strings.

### 9. [8_4_9_same_letter_set](#)

**Description 📝**: This program checks if three words consist of the same set of letters.  
**Purpose 🎯**: Compare sets of letters between three words.

## Conclusion 🚀

Mastering basic set operations in Python is essential for solving problems involving uniqueness, membership, and mathematical operations.
The `set` data structure is optimized for these tasks, making it an invaluable tool for Python developers.
