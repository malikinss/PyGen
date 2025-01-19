# Lesson 10.3: Methods of Dictionaries 🗂️

## Description 📝

This lesson focuses on the various methods of dictionaries in Python, such as adding, modifying, and deleting elements, as well as using built-in functions like `get()`, `update()`, `pop()`, `popitem()`, `clear()`, `copy()`, and `setdefault()`. It also includes practical tasks that demonstrate these methods. The lesson contains 7 tasks and can be found on the course page on the Stepik platform.

## Purpose 🎯

The purpose of this lesson is to provide a comprehensive understanding of the methods available for dictionaries in Python. By mastering these methods, I will be able to manipulate dictionaries efficiently in my Python programs.

## Key Concepts 📚

### Adding and Modifying Elements in a Dictionary

-   **Adding elements**:

```python
my_dict['new_key'] = 'new_value'
```

-   **Modifying elements**:

```python
my_dict['existing_key'] = 'new_value'
```

### Deleting Elements from a Dictionary

-   **Using `del`**:

```python
del my_dict['key_to_remove']
```

-   **Using `pop()`**:

```python
value = my_dict.pop('key_to_remove')
```

-   **Using `popitem()`**:

```python
key, value = my_dict.popitem()
```

### Built-in Methods

-   **`get()`**: Returns the value for a given key, or a default value if the key is not found:

```python
value = my_dict.get('key', 'default_value')
```

-   **`update()`**: Updates the dictionary with elements from another dictionary:

```python
my_dict.update(other_dict)
```

-   **`clear()`**: Clears all items from the dictionary:

```python
my_dict.clear()
```

-   **`copy()`**: Returns a shallow copy of the dictionary:

```python
new_dict = my_dict.copy()
```

-   **`setdefault()`**: Returns the value of a key if it exists, otherwise inserts the key with a default value:

```python
value = my_dict.setdefault('new_key', 'default_value')
```

## Practical Tasks 💻

### 10_3_1: Generate Squares Dictionary

-   **Description**: This task generates a dictionary where the keys are numbers within a specified range, and the values are the squares of the respective keys. It demonstrates dictionary comprehensions.
-   **Purpose**: Efficient creation of a dictionary mapping numbers to their squares.

### 10_3_2: Merge Dictionaries

-   **Description**: This task merges two dictionaries, summing values for common keys and preserving unique keys.
-   **Purpose**: To combine dictionaries efficiently.

### 10_3_3: Count Character Occurrences

-   **Description**: This task counts the number of occurrences of each character in a string, returning a dictionary with the counts.
-   **Purpose**: Useful for text analysis or pattern recognition.

### 10_3_4: Most Frequent Word

-   **Description**: This task finds the most frequent word in a string. In case of a tie, it returns the lexicographically smallest word.
-   **Purpose**: To identify the most common word in a text.

### 10_3_5: Group Dogs by Owner

-   **Description**: This task groups dogs by their owners in a dictionary, where the key is a tuple of the owner's information, and the value is a list of dog names.
-   **Purpose**: To organize pets by their owners.

### 10_3_6: Find Least Frequent Word

-   **Description**: This task finds the least frequent word in a string, ignoring case and punctuation.
-   **Purpose**: To identify uncommon words in a text.

### 10_3_7: Correct Identifiers

-   **Description**: This task processes a string of identifiers to ensure there are no duplicates by appending a number to the duplicate identifiers.
-   **Purpose**: To ensure uniqueness of identifiers in datasets or code.

## Conclusion 🚀

This lesson covers essential dictionary methods that are crucial for working with data in Python. By understanding and using these methods, I will be able to manipulate dictionaries more effectively in real-world applications.
