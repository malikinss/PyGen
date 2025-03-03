# Cyclic Shift Function

## Description 📝

This Python script defines the `cyclic_shift()` function, which cyclically shifts the elements of a list by a given number of steps.
The function modifies the list in place. Positive step values result in a right shift, while negative values lead to a left shift.

## Purpose 🎯

The function is designed to shift elements of a list either to the left or right based on the specified number of steps (`step`).
The operation is done cyclically, meaning that the shifted elements wrap around and appear at the opposite end of the list.

## How It Works 🔍

1. **Input**:

    - `numbers`: A list of integers or floats.
    - `step`: An integer that specifies how many steps to shift the list. Positive values shift elements to the right, while negative values shift them to the left.

2. **Processing**:  
   The function uses the `deque` from the `collections` module, which provides an efficient way to rotate the list elements. The `rotate()` method is used to perform the cyclic shift.

3. **Output**:  
   The list `numbers` is modified in place, so there is no return value.

## Output 📜

The output is a modified version of the `numbers` list with elements shifted cyclically.  
Example:

```python
numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 2)
print(numbers)
```

The output will be:

```python
[4, 5, 1, 2, 3]
```

For a negative shift:

```python
cyclic_shift(numbers, -2)
print(numbers)
```

The output will be:

```python
[3, 4, 5, 1, 2]
```

## Usage 📦

1. Save the code to a file named `cyclic_shift.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```python
    python cyclic_shift.py
    ```
5. Call the function `cyclic_shift()` with a list of numbers and a step value.  
   Example:
    ```python
    numbers = [10, 20, 30, 40, 50]
    cyclic_shift(numbers, 3)
    print(numbers)  # Output: [30, 40, 50, 10, 20]
    ```

## Conclusion 🚀

This function provides a simple and efficient way to cyclically shift elements in a list, making it a useful tool for problems involving rotations or cyclic patterns in lists.
