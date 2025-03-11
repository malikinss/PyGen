# Generator for Producing Unique Elements from Iterable

## Description 📝

The `unique()` function is a generator that iterates over the provided iterable and yields only the unique elements, while preserving their original order.
The function uses a set to keep track of the elements it has already encountered, ensuring that each element is yielded only once.

## Purpose 🎯

This function is useful when you need to process an iterable and eliminate any duplicate elements, but still maintain the order in which the elements appeared.
It can be applied to lists, strings, tuples, or any other iterable data structure.

## How It Works 🔍

1. **Input Parameters**:

    - `iterable`: The input iterable (e.g., a list, string, or any other object that supports iteration).

2. **Logic**:
    - The function iterates through each element of the iterable.
    - A set (`seen`) is used to track elements that have already been yielded.
    - If the current element hasn't been seen before, it is added to the set and yielded.
    - Duplicate elements are ignored, ensuring only unique values are returned in the order they first appear.

## Output 📜

The function yields a sequence of unique elements from the input iterable, in the same order they first appear.

### Example:

```python
>>> for item in unique([1, 2, 2, 3, 1, 4]):
>>>     print(item)
1
2
3
4
```

### Example with strings:

```python
>>> for char in unique("banana"):
>>>     print(char)
b
a
n
```

## Usage 📦

1. Save the code to a file, e.g., `unique_elements.py`.
2. Use the `unique()` function to process any iterable:

    ```python
    my_list = [1, 2, 2, 3, 1, 4]
    for element in unique(my_list):
        print(element)
    ```

3. You can use it with other iterables like strings, tuples, etc.

## Conclusion 🚀

The `unique()` function is an efficient and simple way to filter out duplicates while preserving the order of elements.
It’s great for working with large data sets where order matters and duplicates are not wanted. 🌟
