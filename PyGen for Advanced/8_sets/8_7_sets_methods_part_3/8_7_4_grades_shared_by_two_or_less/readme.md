# Grades Shared by Two or Fewer Students Program 📝

## Description 📝

This program takes the math grades of three students on a 10-point scale and outputs the grades that are shared by no more than two students.
The grades are output in ascending order.

## Purpose 🎯

The goal of this program is to identify which grades are shared by at most two students and output them in ascending order, excluding any grades that are shared by all three students.

## How It Works 🔍

1. **Input**:
    - The program accepts three sets of grades, each representing the grades of one student. Each set contains grades in the range from 0 to 10.
2. **Logic**:
    - The program first collects all grades (union of all three sets).
    - Then, it finds the grades shared by all three students (intersection of the three sets).
    - Finally, it subtracts the grades shared by all three students from the total grades, leaving the grades that are shared by no more than two students.
3. **Output**:
    - The program outputs the remaining grades in ascending order.

### Example:

**Input**:

```
Enter grades for student 1: 5 6 7 8 9
Enter grades for student 2: 6 7 8 10
Enter grades for student 3: 7 8
```

**Output**:

```
5 6 9 10
```

-   Grades shared by all three students are `7` and `8`. The remaining grades shared by no more than two students are `5`, `6`, `9`, and `10`, which are displayed in ascending order.

## Output 📜

-   The grades that are shared by no more than two students, sorted in ascending order.

## Usage 📦

1. Run the program.
2. Enter the grades of the first student.
3. Enter the grades of the second student.
4. Enter the grades of the third student.
5. The program will output the grades shared by no more than two students, in ascending order.

## Conclusion 🚀

This program helps to identify grades that are shared between fewer than three students.
It can be used to filter grades that appear in limited combinations, excluding grades common to all participants.
