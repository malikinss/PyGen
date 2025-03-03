# Matrix to Dictionary Function

## Description 📝

This Python script defines the `matrix_to_dict()` function, which converts a matrix (a nested list) into a dictionary where each key represents the row number and the value is a list of elements in that row.

## Purpose 🎯

The function is designed to transform a matrix (2D list) into a dictionary with the row number as the key, making it easier to access rows by their index.
This conversion is particularly useful when you need to map rows of a matrix to keys in a dictionary, allowing for efficient lookup and modification.

## How It Works 🔍

1. **Input**:

    - `matrix`: A 2D list (matrix) whose elements are either integers or floats.

2. **Processing**:  
   The function enumerates over the rows of the matrix and creates a dictionary. The `enumerate()` function is used with `start=1` to ensure that the row numbers in the dictionary start from 1 (as required).

3. **Output**:  
   The function returns a dictionary where:
    - The key is the row number (starting from 1).
    - The value is the list representing the row.

## Output 📜

The output is a dictionary where each row of the matrix is associated with its row number (starting from 1).  
Example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = matrix_to_dict(matrix)
print(result)
```

The output will be:

```python
{
    1: [1, 2, 3],
    2: [4, 5, 6],
    3: [7, 8, 9]
}
```

## Usage 📦

1. Save the code to a file named `matrix_to_dict.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```python
    python matrix_to_dict.py
    ```
5. Call the function `matrix_to_dict()` with a matrix as input:  
   Example:
    ```python
    matrix = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    result = matrix_to_dict(matrix)
    print(result)
    # Output:
    # {
    #     1: [10, 20, 30],
    #     2: [40, 50, 60],
    #     3: [70, 80, 90]
    # }
    ```

## Conclusion 🚀

The `matrix_to_dict()` function provides a straightforward way to convert a matrix into a dictionary with row numbers as keys.
This approach is useful for cases where you need to work with rows indexed by numbers and access them efficiently.
