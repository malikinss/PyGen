# Lesson 8_3: Sets in Python 📚

## Description 📝

This lesson introduces the concept of sets in Python, focusing on their creation, empty sets, and the built-in `set()` function.
Sets in Python are similar to mathematical sets and support efficient operations such as element membership checks, adding and removing elements, and performing union and intersection operations.

## Purpose 🎯

The goal of this lesson is to:

-   Understand how to create sets in Python.
-   Learn about empty sets and the use of the built-in `set()` function.
-   Get familiar with displaying and manipulating sets in Python.

## Key Concepts 📚

### 1. Creating Sets in Python 🧑‍💻

A set in Python is an unordered collection of unique elements.
It is created by placing elements inside curly braces `{}` or by using the `set()` function.
Sets automatically remove duplicates and are highly efficient for checking membership, adding, and deleting elements.

```python
# Example of creating a set with curly braces
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
```

### 2. Empty Sets 🏷

To create an empty set in Python, I cannot use `{}` because it would create an empty dictionary.
Instead, I must use the `set()` function.

```python
# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()
```

### 3. Built-in `set()` Function 🛠

The `set()` function is a built-in Python function used to create a set from a list, tuple, or other iterable.
It automatically removes duplicate values.

```python
# Creating a set from a list
my_list = [1, 2, 2, 3, 3, 4]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3, 4}
```

### 4. Displaying Sets 👀

To display the elements of a set, I can simply use the `print()` function.
Note that sets are unordered collections, so the output may not necessarily match the order in which elements were added.

```python
# Displaying a set
my_set = {10, 20, 30, 40}
print(my_set)  # Output might be: {10, 20, 30, 40}
```

## How It Works 🔍

-   **Creating a set**: Sets are created using curly braces or the `set()` function, and they store only unique elements.
-   **Empty sets**: To create an empty set, use the `set()` function. The `{}` notation creates an empty dictionary, not a set.
-   **Displaying sets**: I can display sets using the `print()` function. The output is unordered, meaning the elements might not appear in the order they were added.

## Conclusion 🚀

Understanding sets in Python is essential for working with collections of unique elements.
Sets are optimized for fast membership testing, and the `set()` function provides a simple way to create sets from various data types.
Mastering sets will allow me to perform complex operations efficiently.

For further reading and examples, you can refer to the lesson [here](https://stepik.org/lesson/481524/step/1?unit=472629).
