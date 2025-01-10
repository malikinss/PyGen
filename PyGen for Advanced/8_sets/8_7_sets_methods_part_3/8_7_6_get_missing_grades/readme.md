# Missing Biology Grades Program 📝

## Description 📝

This program takes the biology grades of three students on a 10-point scale and outputs the set of grades that none of the three students have.
The output is displayed in ascending order.

## Purpose 🎯

The goal of this program is to identify the grades that are missing from the set of grades of all three students, providing a clear view of the grades that no student has.

## How It Works 🔍

1. **Input**:
    - The program accepts three sets of grades, each representing the grades of one student. Each set contains grades in the range from 0 to 10.
2. **Logic**:
    - The program first creates a set of all possible grades from 0 to 10.
    - It then computes the union of the grades of all three students, representing all the grades they have.
    - Finally, it subtracts the union of the students' grades from the full set of possible grades to find the missing grades.
3. **Output**:
    - The program outputs the grades that none of the students have, sorted in ascending order.

### Example:

**Input**:

```
Enter grades for student 1: 5 6 7 8
Enter grades for student 2: 4 5 6 9
Enter grades for student 3: 0 1 2 3
```

**Output**:

```
10
```

-   The grades for the three students are `5`, `6`, `7`, `8`, `4`, `9`, `0`, `1`, `2`, `3`. The only grade missing is `10`.

## Output 📜

-   The grades that none of the students have, sorted in ascending order.

## Usage 📦

1. Run the program.
2. Enter the grades of the first student.
3. Enter the grades of the second student.
4. Enter the grades of the third student.
5. The program will output the grades that are missing for all students in ascending order.

## Conclusion 🚀

This program helps identify the missing grades that none of the three students have, providing a comprehensive view of the grades that are not represented among the students.
