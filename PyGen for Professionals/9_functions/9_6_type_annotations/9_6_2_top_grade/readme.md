# Top Grade Function

## Description 📝

This Python script defines the `top_grade()` function, which calculates the highest grade for each student from a dictionary containing student names and their corresponding grades.
The function returns a dictionary containing the student's name and their highest grade.

## Purpose 🎯

The purpose of this function is to extract the highest grade for each student from a dictionary where the student names are keys, and their grades are the values (lists of integers).
The function returns a dictionary with the student's name and the highest grade.

## How It Works 🔍

1. **Input**: The function takes one argument:
    - `grades`: A dictionary where the keys are student names (strings), and the values are lists of integers representing the student's grades.
2. **Processing**: The function iterates over the dictionary, and for each student, it finds the maximum grade using the `max()` function.
3. **Output**: The function creates and returns a new dictionary where the key is the student's name, and the value is their highest grade.

## Output 📜

For a given dictionary of student names and grades, the output will be a dictionary containing the student's name and their highest grade.  
For example:

```python
grades = {
    "Alice": [88, 92, 85],
    "Bob": [75, 80, 95],
    "Charlie": [98, 90, 92]
}
top_grade(grades)
```

The output will be:

```python
{'name': 'Charlie', 'top_grade': 98}
```

## Usage 📦

1. Save the code to a file named `top_grade.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```python
    python top_grade.py
    ```
5. Call the function `top_grade()` with a dictionary of student names and their grades.
   Example:
    ```python
    grades = {"John": [85, 88, 92], "Sara": [90, 80, 87]}
    result = top_grade(grades)
    print(result)  # Output: {'name': 'Sara', 'top_grade': 90}
    ```

## Conclusion 🚀

This function provides a simple and effective way to identify the highest grade for each student in a dataset, making it a useful tool for working with student grades and academic performance.
