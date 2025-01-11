# Students Studying Only Math Counter 🧑‍🎓📚

## Description 📝

At BEEGEEK online school, students study either math, computer science, or both. The principal has a list of students studying each subject, and the task is to determine how many students study **only math**. The problem ensures there are no students with the same last name, simplifying the identification of students.

## Purpose 🎯

The program helps the school principal determine the number of students who are studying **only math** by comparing the two sets of students — one for math and the other for computer science (informatics).

## How It Works 🔍

1. **Inputs**:
    - The total number of students studying math.
    - The total number of students studying computer science (informatics).
    - The list of names of students studying math.
    - The list of names of students studying computer science.
2. **Logic**:
    - Find students who are studying both subjects by computing the intersection of the two sets.
    - Subtract the intersection (students studying both) from the math students set to get only math students.
3. **Outputs**:
    - The program outputs the count of students who study only math.

## Output 📜

The program prints a single integer, which is the number of students who study only math.

### Example:

**Input**:

```
5
4
Alice
Bob
Charlie
David
Eve
Alice
Bob
Charlie
Frank
```

**Output**:

```
2
```

### Explanation:

-   **Math students**: `Alice`, `Bob`, `Charlie`, `David`, `Eve`
-   **Informatics students**: `Alice`, `Bob`, `Charlie`, `Frank`
-   **Students studying both**: `Alice`, `Bob`, `Charlie`
-   **Only math students**: `David`, `Eve`
    Thus, the result is `2` because two students study only math.

## Usage 📦

1. Save the code in a Python file, e.g., `math_only_students.py`.
2. Run the script.
3. Provide inputs:
    - The number of math students.
    - The number of informatics students.
    - The list of names of math students.
    - The list of names of informatics students.
4. View the result, which will be the number of students who study only math.

### Example Run:

```plaintext
Input:
3
3
John
Alice
Mark
Alice
Mark
Paul

Output:
1
```

```plaintext
Input:
4
3
Amy
Bob
Charlie
David
Bob
Charlie
Eve

Output:
2
```

## Conclusion 🚀

This program allows the school principal to easily determine how many students are studying only math, making student tracking and academic analysis more efficient. It's perfect for educational institutions that track students' enrollment in different subjects.
