# Unique Physics Grades for Third Student Program 📝

## Description 📝

This program takes the physics grades of three students on a 10-point scale and outputs the grades for the third student that are not found in either the first or second student's grades.
The output is displayed in descending order.

## Purpose 🎯

The goal of this program is to identify the unique grades of the third student that are not shared by the first or second students.

## How It Works 🔍

1. **Input**:
    - The program accepts three sets of grades, each representing the grades of one student. Each set contains grades in the range from 0 to 10.
2. **Logic**:
    - The program computes the union of the grades of the first and second students (all the grades they share).
    - It then finds the grades for the third student that are not in this union, which results in the unique grades for the third student.
3. **Output**:
    - The program outputs the unique grades of the third student in descending order.

### Example:

**Input**:

```
Enter grades for student 1: 5 6 7 8 9
Enter grades for student 2: 6 7 8 10
Enter grades for student 3: 5 9 10
```

**Output**:

```
10 9
```

-   The grades for the third student are `5`, `9`, and `10`. The grades shared by the first and second students are `6`, `7`, and `8`. Therefore, the unique grades for the third student are `9` and `10`, which are displayed in descending order.

## Output 📜

-   The grades of the third student that are not found in either the first or second student, sorted in descending order.

## Usage 📦

1. Run the program.
2. Enter the grades of the first student.
3. Enter the grades of the second student.
4. Enter the grades of the third student.
5. The program will output the grades that are unique to the third student in descending order.

## Conclusion 🚀

This program helps identify the unique grades of the third student that are not shared by the other two students, providing a clear way to filter out common grades and focus on those that are exclusive to the third student.
