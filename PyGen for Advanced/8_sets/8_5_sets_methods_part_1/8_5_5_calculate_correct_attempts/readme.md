# Stepik Task Solver Tracker Program 📝

## Description 📝

This program processes a list of student attempts to solve a task on Stepik and provides the following information:

1. The number of unique students who solved the task correctly.
2. The percentage of correct attempts out of all attempts, rounded to the nearest integer.
3. If no student solved the task correctly, it outputs a message encouraging the user to be the first.

## Purpose 🎯

-   Track and display the number of unique students who solved the task correctly.
-   Calculate the percentage of correct solutions out of total attempts.
-   Provide feedback to students if no one has solved the task yet.

## How It Works 🔍

1. **Input**:
    - The program first reads the total number of attempts `n`.
    - It then processes each of the `n` lines, which contain a student's nickname and their result (either "Correct" or "Wrong").
2. **Logic**:
    - **Unique Correct Solvers**: The program maintains a set to track unique students who solved the task correctly.
    - **Correct Attempt Count**: The program counts the number of correct attempts and calculates the percentage.
    - **Rounding**: The percentage of correct attempts is rounded according to mathematical rules (round up if the decimal part is >= 0.5, otherwise round down).
3. **Output**:
    - If there are correct solvers, it prints the number of students who solved correctly and the percentage of correct attempts.
    - If no one solved the task correctly, it encourages the user to be the first.

### Example:

**Input**:

```
5
alice: Correct
bob: Wrong
carol: Correct
dave: Correct
eve: Wrong
```

**Output**:

```
Correctly solved 3 students
Of all attempt 60% correct
```

-   In this example, 3 students solved the task correctly, and 60% of all attempts were correct.

## Output 📜

-   The program will print the number of students who solved the task correctly and the percentage of correct attempts. If no correct solution is submitted, it will prompt the user to be the first to solve the task.

## Usage 📦

1. Run the program.
2. Enter the number of attempts.
3. Enter each attempt in the format `<nickname>: <result>`.
4. The program will output the results based on the input data.

## Conclusion 🚀

This program helps track task-solving attempts on Stepik and provides feedback on the progress of task completion.
It encourages students to be the first to solve a task if no one has done so yet and provides an accurate percentage of correct attempts.
