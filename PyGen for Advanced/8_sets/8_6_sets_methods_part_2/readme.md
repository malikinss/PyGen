# Lesson 8.6: Sets Methods Part 2 Lesson 🔧

## Description 📝

This lesson introduces advanced methods and operations for sets, covering essential set operations such as union, intersection, difference, and symmetric difference.
Additionally, it explores the use of various update methods and set operators that are commonly used for set manipulations.

## Purpose 🎯

The goal of this lesson is to:

-   Learn the fundamental set operations: `union()`, `intersection()`, `difference()`, and `symmetric_difference()`.
-   Understand how to use the update methods: `update()`, `intersection_update()`, `difference_update()`, and `symmetric_difference_update()`.
-   Get familiar with set operators: `&`, `|`, `-`, and `^`.

## Key Concepts 📚

### 1. Set Operations 🛠

-   **`union()`**: Returns a set containing all elements from both sets (similar to a mathematical union).

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}
```

-   **`intersection()`**: Returns a set containing only the elements common to both sets (similar to a mathematical intersection).

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.intersection(set2)
print(result)  # Output: {3}
```

-   **`difference()`**: Returns a set containing the elements present in the first set but not in the second (similar to a mathematical difference).

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.difference(set2)
print(result)  # Output: {1, 2}
```

-   **`symmetric_difference()`**: Returns a set containing the elements that are in either of the sets, but not in both (similar to a mathematical symmetric difference).

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 2, 4, 5}
```

### 2. Update Methods 🔄

-   **`update()`**: Adds all elements from another set or iterable to the current set. It performs a union operation.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}
```

-   **`intersection_update()`**: Updates the current set to contain only the elements that are present in both sets (intersection).

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)  # Output: {3}
```

-   **`difference_update()`**: Updates the current set to contain only the elements that are in the first set but not in the second (difference).

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.difference_update(set2)
print(set1)  # Output: {1, 2}
```

-   **`symmetric_difference_update()`**: Updates the current set to contain only the elements that are in either of the sets, but not in both (symmetric difference).

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 4, 5}
```

### 3. Set Operators 🔀

-   **`&` (Intersection)**: Performs the intersection operation between two sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 & set2
print(result)  # Output: {3}
```

-   **`|` (Union)**: Performs the union operation between two sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 | set2
print(result)  # Output: {1, 2, 3, 4, 5}
```

-   **`-` (Difference)**: Performs the difference operation between two sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 - set2
print(result)  # Output: {1, 2}
```

-   **`^` (Symmetric Difference)**: Performs the symmetric difference operation between two sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 ^ set2
print(result)  # Output: {1, 2, 4, 5}
```

## Example Programs 💻

1. **8_6_1_count_common_numbers**  
   This program takes two sequences of numbers as input and calculates the number of common numbers that appear in both sequences.

2. **8_6_2_find_common_numbers_in_ascending_order**  
   This program finds all the common numbers between two sequences and outputs them in ascending order.

3. **8_6_3_find_unique_numbers_in_ascending_order**  
   This program finds the numbers that are in the first sequence but not in the second and outputs them in ascending order.

4. **8_6_4_find_common_digits**  
   This program finds the common digits shared across multiple natural numbers and outputs them in ascending order.

## Conclusion 🚀

Mastering these set operations and methods is crucial for performing common tasks in Python, such as finding intersections, differences, and unions between sets.
The ability to update sets and use operators enhances the efficiency and flexibility of set manipulations in your programs.
