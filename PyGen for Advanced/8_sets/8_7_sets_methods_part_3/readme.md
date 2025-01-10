# Lesson 8.7: Sets Methods Part 3 🔧

## Description 📝

In this lesson, we explore methods for comparing sets and analyzing their relationships.
We'll cover set comparison methods like `issuperset()`, `issubset()`, and `isdisjoint()`, as well as comparison operators such as `<`, `>`, `<=`, and `>=`.

## Purpose 🎯

The goal of this lesson is to:

-   Understand how to check subset, superset, and disjoint relationships between sets using the methods `issuperset()`, `issubset()`, and `isdisjoint()`.
-   Learn to compare sets with the comparison operators `<`, `>`, `<=`, and `>=` for more intuitive and logical set analysis.

## Key Concepts 📚

### 1. Set Comparison Methods 🛠

-   **`issuperset()`**: Returns `True` if the set is a superset of another set (i.e., the first set contains all elements of the second set).

```python
set1 = {1, 2, 3}
set2 = {1, 2}
result = set1.issuperset(set2)
print(result)  # Output: True
```

-   **`issubset()`**: Returns `True` if the set is a subset of another set (i.e., all elements of the set are contained within the second set).

```python
set1 = {1, 2}
set2 = {1, 2, 3}
result = set1.issubset(set2)
print(result)  # Output: True
```

-   **`isdisjoint()`**: Returns `True` if the two sets do not have any elements in common (i.e., the intersection of the sets is an empty set).

```python
set1 = {1, 2}
set2 = {3, 4}
result = set1.isdisjoint(set2)
print(result)  # Output: True
```

### 2. Set Comparison Operators 🔀

-   **`<` (Proper Subset)**: Checks if the set is a proper subset of another set (i.e., the first set is a subset, but not equal to the second set).

```python
set1 = {1, 2}
set2 = {1, 2, 3}
result = set1 < set2
print(result)  # Output: True
```

-   **`>` (Proper Superset)**: Checks if the set is a proper superset of another set (i.e., the first set contains the second set, but is not equal to it).

```python
set1 = {1, 2, 3}
set2 = {1, 2}
result = set1 > set2
print(result)  # Output: True
```

-   **`<=` (Subset or Equal)**: Checks if the set is a subset or equal to another set.

```python
set1 = {1, 2}
set2 = {1, 2, 3}
result = set1 <= set2
print(result)  # Output: True
```

-   **`>=` (Superset or Equal)**: Checks if the set is a superset or equal to another set.

```python
set1 = {1, 2, 3}
set2 = {1, 2}
result = set1 >= set2
print(result)  # Output: True
```

## Example Programs 💻

1. **8_7_1_have_same_digits**  
   This program checks if two given numbers contain exactly the same digits, regardless of their order or frequency.

2. **8_7_2_contains_all_digits**  
   This program checks if all the digits in a second number are present in a first number, regardless of order or repetition.

3. **8_7_3_find_grades**  
   This program compares the grades of three students and outputs the grades shared by the first two students but not the third, sorted in descending order.

4. **8_7_4_grades_shared_by_two_or_less**  
   This program identifies the grades shared by no more than two students and outputs them in ascending order.

5. **8_7_5_get_unique_grades**  
   This program identifies the unique grades of the third student that are not found in the first two students' grades, sorted in descending order.

6. **8_7_6_get_missing_grades**  
   This program identifies the grades missing from the set of grades of all three students and outputs them in ascending order.

## Conclusion 🚀

Understanding set comparisons is essential for tasks that involve determining relationships between sets.
Whether you're identifying common elements, subsets, or superset structures, these methods and operators provide the tools needed for efficient set analysis and manipulation.
