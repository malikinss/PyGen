# Students Studying Only One Subject 📚

## Description 📝

The program helps the principal of BEEGEEK online school determine how many students are studying only one subject, either math or computer science (informatics), or both. The program takes two lists of students—one for math and one for informatics—and calculates how many students study exclusively one subject.

## Purpose 🎯

The program calculates the number of students studying only one subject and outputs the result. If there are no such students, it outputs "NO."

## How It Works 🔍

1. **Inputs**:
    - The number of math students and informatics students.
    - A list of names of math students and a list of names of informatics students.
2. **Logic**:
    - The program calculates the students who study only one subject by subtracting the set of informatics students from the math students and vice versa.
3. **Outputs**:
    - If there are students who study only one subject, the program will output the total count.
    - If there are no students who study only one subject, the program will output "NO."

## Output 📜

The program outputs the number of students studying only one subject. If there are no such students, it outputs "NO."

### Example:

**Input**:

```
4
5
Enter 4 math students' names:
Alice
Bob
Charlie
David
Enter 5 informatics students' names:
Bob
Eve
David
Frank
Grace
```

**Output**:

```
3
```

### Explanation:

-   Math students: `{'Alice', 'Bob', 'Charlie', 'David'}`
-   Informatics students: `{'Bob', 'Eve', 'David', 'Frank', 'Grace'}`
-   Students studying only math: `{'Alice', 'Charlie'}`
-   Students studying only informatics: `{'Eve', 'Frank', 'Grace'}`
-   Total number of students studying only one subject: `3`

## Usage 📦

1. Save the code in a Python file, e.g., `students_one_subject.py`.
2. Run the script.
3. Provide the number of students studying math and informatics.
4. Input the names of students studying math and informatics.
5. The program will output the number of students studying only one subject or "NO" if none.

### Example Run:

```plaintext
Input:
4
5
Enter 4 math students' names:
Alice
Bob
Charlie
David
Enter 5 informatics students' names:
Bob
Eve
David
Frank
Grace

Output:
3
```

## Conclusion 🚀

This program efficiently helps the principal understand how many students are studying only one subject at BEEGEEK. It's useful for organizing student data and ensuring no overlaps between subjects.
