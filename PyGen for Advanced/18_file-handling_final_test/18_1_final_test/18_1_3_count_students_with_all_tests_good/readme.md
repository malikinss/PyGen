# Student Grade Evaluator

## Description 📝

This Python program analyzes student test scores from a file and counts how many students have passed all three tests.

## Purpose 🎯

The program helps determine the number of students who have successfully passed all their tests by checking if each student has met the passing criteria.

## How It Works 🔍

1. **Reading Data**:
    - The program reads a file named `grades.txt`, which contains student last names and their test scores.
2. **Processing Data**:
    - Each line is split into a student's last name and three test scores.
    - The scores are converted to integers for comparison.
3. **Checking Passing Criteria**:
    - A student is considered to have passed if all their test scores are **≥ 65**.
4. **Counting Passed Students**:
    - The program counts and outputs the number of students who passed all tests.

## Output 📜

The program outputs the number of students who passed all tests.

### Example:

If `grades.txt` contains:

```
Smith 70 85 90
Johnson 60 75 80
Williams 88 92 95
Brown 65 70 60
```

The program will output:

```
2
```

(Since only "Smith" and "Williams" passed all three tests.)

## Usage 📦

1. Save the script as `grade_evaluator.py`.
2. Ensure `grades.txt` is in the same directory.
3. Open a terminal or command prompt.
4. Navigate to the script's directory.
5. Run the script using:
    ```
    python grade_evaluator.py
    ```
6. The program will display the number of students who passed all tests.

## Conclusion 🚀

This program provides an efficient way to evaluate student performance based on their test scores.
It can be used for automated grading analysis.
