# Student Classification Program 🎓

## Description 📝

This program classifies students into two categories based on their grades: "good" and "excellent".
A student is considered:

-   **Good** if their grade is 4.
-   **Excellent** if their grade is 5.

It first prints all student names and their grades, and then prints the names and grades of the good and excellent students.

## Purpose 🎯

-   To demonstrate how to classify students based on their grades.
-   To work with lists and tuples in Python.
-   To practice handling input/output and basic control structures.

## How It Works 🔍

1. **Function `get_student_data(n)`**:

    - Reads `n` student entries from the input, with each entry containing the student's last name and grade.
    - Stores the data in a list of tuples, where each tuple consists of the student's last name and grade.

2. **Function `classify_students(students)`**:

    - Filters students whose grades are 4 or 5 (good and excellent students).

3. **Function `print_students(students)`**:

    - Prints each student's last name and grade in the given order.

4. **Main Program (`main`)**:
    - Reads the number of students, processes their data, and prints the student list followed by the list of good and excellent students.

### Example:

```
Input:
5
Ivanov 3
Petrov 4
Sidorov 5
Kuznetsov 2
Vasiliev 4

Output:
Ivanov 3
Petrov 4
Sidorov 5
Kuznetsov 2
Vasiliev 4

Petrov 4
Sidorov 5
Vasiliev 4
```

## Output 📜

The program will print the following:

```
Ivanov 3
Petrov 4
Sidorov 5
Kuznetsov 2
Vasiliev 4

Petrov 4
Sidorov 5
Vasiliev 4
```

## Conclusion 🚀

The program successfully classifies students into good and excellent categories based on their grades, while printing all student data and filtered results accordingly.
