# Numbers Sum Function

## Description 📝

This Python script defines the `numbers_sum()` function, which takes a list of arbitrary objects and returns the sum of its numeric elements (integers and floats), while ignoring non-numeric objects.
If the list contains no numbers, the function returns `0`.

## Purpose 🎯

The purpose of this function is to demonstrate filtering elements based on their type and performing summation operations on lists containing mixed data types.
This helps in handling heterogeneous collections where numerical and non-numerical values are mixed.

## How It Works 🔍

1. **Input**: A list of arbitrary objects (`elems`).
2. **Filtering**: The function uses `filter()` to extract only elements of type `int` or `float`.
3. **Summation**: The numeric elements are summed using Python's built-in `sum()` function.
4. **Edge Case Handling**: If no numbers are present in the list, the function returns `0`.

## Output 📜

The function returns the sum of numeric values from the input list.  
Example outputs:

```python
print(numbers_sum([1, 2, 3, "a", 4.5, None]))  # Output: 10.5
print(numbers_sum(["hello", None, [], {}]))    # Output: 0
print(numbers_sum([5, -2.5, "test", 7]))       # Output: 9.5
```

## Usage 📦

1. Save the code to a file named `numbers_sum.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```python
    python numbers_sum.py
    ```
5. Use the function in a Python script or interactive shell:

    ```python
    from numbers_sum import numbers_sum

    result = numbers_sum([10, "apple", 20.5, True])
    print(result)  # Output: 30.5
    ```

## Conclusion 🚀

This function is useful for working with mixed data lists where numerical and non-numerical values coexist.
It effectively filters out unwanted data and performs summation efficiently.
