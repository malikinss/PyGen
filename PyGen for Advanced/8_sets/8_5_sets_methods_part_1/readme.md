# Lesson 8.5: Sets Methods (Part 1) 🔧

## Description 📝

This lesson introduces various methods for adding and removing elements in sets.
Understanding how to use these methods is crucial for efficiently managing sets and performing common operations, such as adding elements, removing them, and clearing sets.

## Purpose 🎯

The goal of this lesson is to:

-   Learn how to add elements to a set using the `add()` method.
-   Explore methods for removing elements: `remove()`, `discard()`, and `pop()`.
-   Understand how to clear all elements from a set using the `clear()` method.

## Key Concepts 📚

### 1. Method for Adding an Element `add()` ➕

The `add()` method adds a single element to a set. If the element already exists in the set, the set remains unchanged since sets only store unique elements.

```python
# Adding an element to the set
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
```

### 2. Methods for Removing Elements 🗑

There are several methods to remove elements from a set:

-   **`remove()`**: Removes an element from the set. If the element is not found, it raises a `KeyError`.

```python
# Removing an element using remove()
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}
```

-   **`discard()`**: Removes an element from the set, but if the element is not present, it does nothing (does not raise an error).

```python
# Removing an element using discard()
my_set = {1, 2, 3}
my_set.discard(4)  # No error even though 4 is not in the set
print(my_set)  # Output: {1, 2, 3}
```

-   **`pop()`**: Removes and returns an arbitrary element from the set. Since sets are unordered, the element removed is not predictable.

```python
# Removing an element using pop()
my_set = {1, 2, 3}
removed_element = my_set.pop()
print(f"Removed element: {removed_element}")
print(my_set)  # Output: Set with one less element
```

### 3. Method for Clearing All Elements `clear()` 🧹

The `clear()` method removes all elements from the set, leaving it empty.

```python
# Clearing all elements from a set
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()
```

## Example Programs 💻

1. **8_5_1_process_words**  
   This program reads multiple words from user input and prints the number of unique characters in each word, ignoring case differences.
   It uses Python sets to filter out duplicates and ensure accurate counting of distinct characters.

2. **8_5_2_count_unique_characters_in_all_words**  
   This program calculates and prints the total number of unique characters across multiple words, ignoring case differences.
   It combines all input words, normalizes them to lowercase, and uses a set to extract and count unique characters.

3. **8_5_3_count_different_words**  
   This program determines the total number of different words in a line of text, ignoring punctuation marks and considering words case-insensitively. It handles multiple spaces separating words.

4. **8_5_4_check_number_repeats**  
   This program processes a sequence of numbers given as input and checks whether each number has appeared before in the sequence, printing "YES" for repeats and "NO" for new numbers. Leading zeros are ignored.

5. **8_5_5_calculate_correct_attempts**  
   This program tracks the number of unique students who solved a task correctly on Stepik, calculates the percentage of correct attempts out of all attempts, and provides feedback if no one has solved the task yet.

## Conclusion 🚀

Mastering the basic methods for adding and removing elements from sets is essential for manipulating sets effectively.
By using these methods, I can handle common tasks like filtering duplicates, removing specific elements, and clearing sets when needed.
