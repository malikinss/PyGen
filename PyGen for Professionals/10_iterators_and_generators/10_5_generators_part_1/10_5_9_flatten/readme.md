# Flatten Nested List Generator

## Description 📝

This Python script defines the `flatten()` generator function, which takes a nested list as input and yields all the integers contained within the list, including those within any nested sublists.
The function flattens arbitrarily nested lists into a sequence of integers.

## Purpose 🎯

The goal of this function is to provide an efficient way to flatten a deeply nested list of integers into a simple sequence.
This is useful when working with data structures that involve nested lists and you need to process all the integers in a single, flat sequence.

## How It Works 🔍

1. **Generator Function**: The `flatten()` function is a generator that recursively traverses a nested list structure.
2. **Recursion**: For each element in the list:
    - If the element is an integer, it yields that integer.
    - If the element is another list, it recursively flattens that list and yields all integers contained within.
3. **StopIteration**: Once all the elements have been yielded, the generator naturally raises a `StopIteration` exception, as is typical with Python generators.

## Output 📜

The function yields each integer found in the nested structure in a flattened manner:
Example:

```python
nested_list = [1, [2, 3, [4, 5]], 6]
for num in flatten(nested_list):
    print(num)
```

Output:

```
1
2
3
4
5
6
```

## Usage 📦

1. Save the code to a file named `flatten_nested_list.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```python
    python flatten_nested_list.py
    ```
5. Use the generator in a loop to get the flattened list:
   Example:
    ```python
    nested_list = [1, [2, 3, [4, 5]], 6]
    for num in flatten(nested_list):
        print(num)
    ```

## Conclusion 🚀

This generator function provides an efficient and memory-friendly way to flatten nested lists of integers into a single sequence.
It handles arbitrarily nested structures and yields values one by one, making it suitable for processing large datasets without consuming too much memory.
