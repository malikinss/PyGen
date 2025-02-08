# Teacher Timur's Test Checker 📚

## Description 📝

This program helps Teacher Timur ensure that each class in an online school has at least one student who scored a grade of 5 on a math test. The program uses the built-in functions `all()` and `any()` to check the conditions.

## Purpose 🎯

The program checks if every group (class) has at least one "excellent" student who received a grade of 5. If any group does not have such a student, it returns `"NO"`; otherwise, it returns `"YES"`.

## How It Works 🔍

1. **Input**:
    - The program first asks for the number of groups (classes).
    - For each group, it expects the number of students followed by their names and grades in a single input line.
2. **Check**:

    - For each group, the program checks whether any student received a grade of 5 using the `any()` function.
    - The `all()` function is used to ensure that the condition is true for every group.

3. **Output**:
    - If every group has at least one student with a grade of 5, the program prints `"YES"`.
    - If any group does not have a student with a grade of 5, it prints `"NO"`.

## Example Output:

```
YES
```

## Usage 📦

1. The user inputs the number of groups.
2. For each group, the number of students is input, followed by their names and grades.
3. The program will then output `"YES"` if all groups have at least one student with a grade of 5, otherwise, it outputs `"NO"`.

## Conclusion 🚀

This program ensures that every group in an online school has at least one excellent student, helping the teacher efficiently assess the class performance with minimal effort.
