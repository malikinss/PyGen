# Generator for Iterating Until a Specific Object

## Description 📝

The `stop_on()` function is a generator that iterates over the given iterable and yields elements one by one until it encounters a specified object.
Once the object is encountered, the iteration stops.
If the object is not found, the generator yields all elements of the iterable.

## Purpose 🎯

This function is useful when you need to process an iterable and stop once a specific element is encountered.
It ensures that the iteration ceases immediately upon reaching the object, making it efficient for scenarios where you only care about the elements up to that point.

## How It Works 🔍

1. **Input Parameters**:

    - `iterable`: The input iterable (e.g., a list, string, tuple, etc.).
    - `obj`: The object that will cause the generator to stop.

2. **Logic**:
    - The function iterates through each element in the iterable.
    - If the current element is equal to `obj`, the iteration stops (`break`).
    - If the object is not found in the iterable, the generator continues yielding all elements of the iterable.
    - The elements are yielded in the original order of the iterable, and the generator stops immediately once `obj` is found.

## Output 📜

The function yields a sequence of elements from the iterable until the specified object is encountered, or until the iterable ends. If the object is not found, the entire iterable is returned.

### Example:

```python
>>> for item in stop_on([1, 2, 3, 4, 5], 3):
>>>     print(item)
1
2
```

### Example when object is not found:

```python
>>> for item in stop_on([1, 2, 3, 4, 5], 6):
>>>     print(item)
1
2
3
4
5
```

## Usage 📦

1. Save the code to a file, e.g., `stop_on_function.py`.
2. Use the `stop_on()` function to process any iterable:

    ```python
    my_list = [1, 2, 3, 4, 5]
    for element in stop_on(my_list, 3):
        print(element)
    ```

3. You can use it with strings, tuples, or any other iterable:
    ```python
    my_string = "abcdef"
    for char in stop_on(my_string, 'd'):
        print(char)
    ```

## Conclusion 🚀

The `stop_on()` function is a simple yet powerful tool for processing elements of an iterable up to a certain point.
It is particularly useful for scenarios where you need to process data until a specific value is encountered, and it ensures the process stops immediately when that value is found. 🌟
