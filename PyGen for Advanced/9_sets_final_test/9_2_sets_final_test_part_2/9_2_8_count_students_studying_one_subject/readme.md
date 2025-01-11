# Student Subject Count 📚

## Description 📝

At BEEGEEK online school, each student studies either math, computer science (informatics), or both. The school principal has lists of students enrolled in each subject. This program helps the principal find out how many students study only one of the subjects.

## Purpose 🎯

To determine how many students study only one subject (either math or informatics) and not both.

## How It Works 🔍

1. **Inputs**:
    - The number of students studying math.
    - The number of students studying informatics.
    - Lists of student names for each subject.
2. **Logic**:
    - The program calculates the number of students studying both subjects.
    - It then finds out how many students are studying only math or only informatics.
3. **Outputs**:
    - The number of students studying only one subject.
    - If no student is studying only one subject, output "NO".

## Output 📜

The program outputs:

-   The number of students studying only one subject (either math or informatics).
-   If there are no students studying only one subject, the program outputs `"NO"`.

### Example:

**Input**:

```
3
3
John
Paul
Mary
Paul
Anna
John
```

**Output**:

```
2
```

### Explanation:

-   **Math students**: `{'John', 'Paul', 'Mary'}`
-   **Informatics students**: `{'Paul', 'Anna', 'John'}`
-   **Students studying both subjects**: `{'John', 'Paul'}`

-   Students studying only math: `{'Mary'}`.
-   Students studying only informatics: `{'Anna'}`.

So, there are 2 students studying only one subject.

## Usage 📦

1. Save the code in a Python file, e.g., `student_subject_count.py`.
2. Run the script.
3. Provide inputs:
    - The number of students in each subject.
    - Lists of student names for math and informatics.
4. View the result:
    - The number of students studying only one subject.
    - If no such students exist, the program will print `"NO"`.

### Example Run:

```plaintext
Input:
2
3
Alice
Bob
Alice
David
Charlie

Output:
2
```

```plaintext
Input:
2
2
Eve
Frank
Frank
Eve

Output:
NO
```

## Conclusion 🚀

This program efficiently computes the number of students studying only one subject and helps streamline the process of managing student enrollment. It’s especially useful in academic institutions for reporting and planning.
