# Generate Student Info 🧑‍🏫

## Description 📝

This program takes three lists — `student_ids`, `student_names`, and `student_grades` — containing information about students.
It generates a list of nested dictionaries where each dictionary contains the student ID as the key and another dictionary containing the student's name and grade as the value.

## Purpose 🎯

The purpose of this program is to convert three parallel lists into a structured list of dictionaries, making it easier to look up student information by ID.

## How It Works 🔍

1. **Input**:
    - A list `student_ids` containing student IDs (e.g., `'S001'`).
    - A list `student_names` containing student names (e.g., `'Camila Rodriguez'`).
    - A list `student_grades` containing student grades (e.g., `86`).
2. **Processing**:
    - The program uses the built-in `zip()` function to iterate through all three lists in parallel.
    - For each student, it creates a dictionary where the key is the student ID and the value is another dictionary containing the student's name and grade.
3. **Output**:
    - A list of nested dictionaries where each dictionary follows the pattern:
        ```python
        {'S001': {'Camila Rodriguez': 86}}
        ```

## Output 📜

The program outputs a list where each element is a dictionary containing the student ID as the key and another dictionary with the student's name and grade as the value.

### Example Input/Output:

**Input**:

```python
student_ids = [
    'S001', 'S002', 'S003', 'S004',
    'S005', 'S006', 'S007', 'S008',
    'S009', 'S010', 'S011', 'S012', 'S013'
]
student_names = [
    'Camila Rodriguez', 'Juan Cruz', 'Dan Richards',
    'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
    'Khalid Hussain', 'Ethan Hawke', 'David Bowman',
    'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy'
]
student_grades = [
    86, 98, 89,
    92, 45, 67,
    89, 90, 100,
    98, 10, 96, 93
]
```

**Output**:

```python
[
    {'S001': {'Camila Rodriguez': 86}},
    {'S002': {'Juan Cruz': 98}},
    {'S003': {'Dan Richards': 89}},
    {'S004': {'Sam Boyle': 92}},
    {'S005': {'Batista Cesare': 45}},
    {'S006': {'Francesco Totti': 67}},
    {'S007': {'Khalid Hussain': 89}},
    {'S008': {'Ethan Hawke': 90}},
    {'S009': {'David Bowman': 100}},
    {'S010': {'James Milner': 98}},
    {'S011': {'Michael Owen': 10}},
    {'S012': {'Gary Oldman': 96}},
    {'S013': {'Tom Hardy': 93}}
]
```

## Usage 📦

1. Copy the code into a Python file (e.g., `generate_student_info.py`).
2. Pass three parallel lists (`student_ids`, `student_names`, `student_grades`) to the `generate_student_info()` function.
3. The function will return a list of dictionaries where the key is the student ID and the value is another dictionary containing the student's name and grade.

### Example Run:

```python
# Sample run
student_ids = [
    'S001', 'S002', 'S003', 'S004',
    'S005', 'S006', 'S007', 'S008',
    'S009', 'S010', 'S011', 'S012', 'S013'
]
student_names = [
    'Camila Rodriguez', 'Juan Cruz', 'Dan Richards',
    'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
    'Khalid Hussain', 'Ethan Hawke', 'David Bowman',
    'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy'
]
student_grades = [
    86, 98, 89,
    92, 45, 67,
    89, 90, 100,
    98, 10, 96, 93
]

result = generate_student_info(student_ids, student_names, student_grades)
print(result)
```

**Output**:

```python
[
    {'S001': {'Camila Rodriguez': 86}},
    {'S002': {'Juan Cruz': 98}},
    {'S003': {'Dan Richards': 89}},
    {'S004': {'Sam Boyle': 92}},
    {'S005': {'Batista Cesare': 45}},
    {'S006': {'Francesco Totti': 67}},
    {'S007': {'Khalid Hussain': 89}},
    {'S008': {'Ethan Hawke': 90}},
    {'S009': {'David Bowman': 100}},
    {'S010': {'James Milner': 98}},
    {'S011': {'Michael Owen': 10}},
    {'S012': {'Gary Oldman': 96}},
    {'S013': {'Tom Hardy': 93}}
]
```

## Conclusion 🚀

This program provides a simple yet effective way to transform three parallel lists into a more structured format, making it easier to access student information by their IDs.
This method can be useful for organizing and processing student data efficiently.
