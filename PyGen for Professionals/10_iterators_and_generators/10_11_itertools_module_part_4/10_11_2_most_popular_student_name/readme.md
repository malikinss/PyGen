### `most_popular_student_name()` - Find the Most Common First Name

## Description 📝

The function `most_popular_student_name()` returns the most common first name among the students in the provided list of `Student` named tuples.

## Purpose 🎯

✔ **Find the most frequent first name** in a list of students.  
✔ **Efficient grouping** of students based on first name.  
✔ **Handles the case where the name is unique**.

## How It Works 🔍

1. **Sort the list** of students based on the first name.
2. **Group the students** by their first name using `groupby()`.
3. **Count the frequency** of each name and find the one with the maximum count.
4. **Return** the most popular first name.

## Output 📜

### Example Input

```python
students = [
    Student('Гагиев', 'Александр', 10),
    Student('Дедedkaев', 'Илья', 11),
    Student('Кодзаев', 'Георгий', 10),
    Student('Набокова', 'Алиса', 11),
    Student('Шилин', 'Александр', 11),
    Student('Чен', 'Илья', 11)
]

most_popular_student_name(students)
```

### Output

```plaintext
Илья
```

## Code Breakdown 🛠

### Step 1: Sort the List by First Name

```python
students.sort(key=key_func)
```

-   The list is sorted based on the first name of the students (`key_func` is a lambda that extracts the `name`).

### Step 2: Group Students by First Name

```python
grouped = groupby(students, key=key_func)
```

-   After sorting, `groupby()` groups the students by their first name.

### Step 3: Find the Most Common Name

```python
most_popular = max(
    ((name, len(list(group))) for name, group in grouped),
    key=lambda x: x[1]
)
```

-   For each group, the size of the group is counted using `len(list(group))`, and the most frequent name is found using `max()`.

### Step 4: Print the Most Common Name

```python
print(most_popular[0])
```

-   The most common first name is printed.

## Usage 📦

```python
students_data = [
    Student('Петров', 'Алексей', 10), Student('Смирнова', 'Анна', 11),
    Student('Иванова', 'Мария', 10), Student('Кузнецова', 'Алексей', 11)
]

most_popular_student_name(students_data)
```

**Output:**

```plaintext
Алексей
```

## Conclusion 🚀

This function is an efficient solution for finding the **most popular first name** among students in a list, using sorting, grouping, and `max()` to identify the most frequent name. It's a compact and clear approach to the problem.
