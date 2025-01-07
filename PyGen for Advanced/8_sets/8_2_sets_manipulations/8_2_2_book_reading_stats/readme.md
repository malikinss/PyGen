# Book Reading Statistics Program 📚

## Description 📝

This program calculates statistics about the book reading behavior of students in the 10th grade of the BEEGEEK online school.
The students were assigned to read three books during their summer holidays, and the program determines how many students:

-   Read only one book
-   Read only two books
-   Did not read any of the recommended books

## Purpose 🎯

-   To calculate the number of students who read only one book, read exactly two books, and the number of students who did not read any of the recommended books, based on provided data.

## How It Works 🔍

1. **Inputs**:

    - The number of students who read each individual book (`n`, `m`, `k`).
    - The number of students who read combinations of two books or more (`x`, `y`, `z`).
    - The number of students who completed the task by reading at least one book (`t`).
    - The total number of students in the grade (`a`).

2. **Function `book_reading_stats`**:

    - The function computes the number of students who read only one book, exactly two books, and the number of students who didn't read any books.
    - It uses the inclusion-exclusion principle to calculate the intersections between students who read two or more books.

3. **Output**:
    - The program prints three values:
        1. The number of students who read only one book.
        2. The number of students who read only two books.
        3. The number of students who did not read any book.

### Example:

```
Input:
5 7 6 4 5 3 4 20

Output:
7
5
8
```

## Output 📜

For the example above, the program will output:

```
7
5
8
```

This means:

-   7 students read only one book.
-   5 students read exactly two books.
-   8 students did not read any book.

## Conclusion 🚀

This program accurately calculates the book reading statistics for the students based on the given data.
By applying the inclusion-exclusion principle, it helps track the number of students in each category and ensures a precise count of those who participated in the reading task and those who didn't.
