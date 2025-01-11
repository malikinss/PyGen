# Students Attending All Lessons 📚

## Description 📝

This program helps the head of BEEGEEK online school determine which students attended all lessons from the beginning of the school year. For each lesson, a list of students who attended is provided, and the program calculates the students who attended every lesson.

## Purpose 🎯

The program calculates and outputs the names of students who attended all lessons. It takes the number of lessons and their respective student attendance lists, then determines the students present in every lesson.

## How It Works 🔍

1. **Inputs**:
    - The number of lessons.
    - A list of student names for each lesson.
2. **Logic**:
    - The program starts by assuming that all students in the first lesson attended all lessons.
    - For each subsequent lesson, the program narrows down the list to only include students who attended that lesson as well.
3. **Outputs**:
    - The program outputs the names of the students who attended every lesson, sorted alphabetically.

## Output 📜

The program outputs the names of the students who attended all lessons, one per line. The names are sorted in alphabetical order.

### Example:

**Input**:

```
3
5
Alice
Bob
Charlie
David
Eve
4
Bob
Charlie
David
Eve
3
Alice
Charlie
David
```

**Output**:

```
Charlie
David
```

### Explanation:

-   Lesson 1 students: `{'Alice', 'Bob', 'Charlie', 'David', 'Eve'}`
-   Lesson 2 students: `{'Bob', 'Charlie', 'David', 'Eve'}`
-   Lesson 3 students: `{'Alice', 'Charlie', 'David'}`

After processing all lessons, the students who attended every lesson are `{'Charlie', 'David'}`.

## Usage 📦

1. Save the code in a Python file, e.g., `students_all_lessons.py`.
2. Run the script.
3. Input the number of lessons.
4. For each lesson, input the number of students followed by their names.
5. The program will output the sorted list of students who attended all lessons.

### Example Run:

```plaintext
Input:
3
5
Alice
Bob
Charlie
David
Eve
4
Bob
Charlie
David
Eve
3
Alice
Charlie
David

Output:
Charlie
David
```

## Conclusion 🚀

This program helps the head of BEEGEEK easily track which students have been consistent in attending all lessons, making it useful for managing student attendance records.
