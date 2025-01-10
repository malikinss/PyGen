# Grade Comparison Program 📝

## Description 📝

This program takes the grades of three students on a 10-point scale and outputs the grades that both the first and second students have, but the third student does not. The grades are output in descending order.

## Purpose 🎯

The goal is to compare the grades of three students and identify which grades are shared by the first two students, but not the third, and present them in descending order.

## How It Works 🔍

1. **Input**:
    - The program accepts three sets of grades, each representing the grades of one student. Each set contains grades from 0 to 10, input as space-separated values.
2. **Logic**:
    - The program first finds the intersection of grades between the first two students.
    - Then, it subtracts the grades of the third student from this intersection to get the final result.
    - The result is sorted in descending order.
3. **Output**:
    - The program outputs the resulting set of grades in descending order.

### Example:

**Input**:

```
Enter grades for student 1: 5 6 7 8 9
Enter grades for student 2: 6 7 8 10
Enter grades for student 3: 7 8
```

**Output**:

```
6 9
```

-   Both the first and second students have grades 6, 7, and 8. The third student also has grades 7 and 8. Therefore, the remaining grade is 6 (from the first and second students but not the third). The result is displayed in descending order as `9 6`.

## Output 📜

-   The grades that both the first and second students have but the third does not, sorted in descending order.

## Usage 📦

1. Run the program.
2. Enter the grades of the first student.
3. Enter the grades of the second student.
4. Enter the grades of the third student.
5. The program will output the grades shared by the first two students but not the third, in descending order.

## Conclusion 🚀

This program is useful for identifying the grades that two students share, while excluding grades that the third student has.
It can be applied in situations where comparisons between sets of data are necessary.
