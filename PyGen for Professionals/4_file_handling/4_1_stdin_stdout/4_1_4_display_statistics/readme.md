# Student Heights Statistics

## Description 📝

This Python program receives a list of student heights and calculates the following statistics:

1. The height of the shortest student.
2. The height of the tallest student.
3. The average height of all students.

The program reads the heights from the input and then displays the required statistics.
If no input is provided, it will output `no students`.

## Purpose 🎯

The purpose of this program is to determine key statistics (shortest, tallest, and average height) for a group of students, which can be useful in educational settings or any other scenario involving student heights.

## How It Works 🔍

1. **Function `read_student_heights()`**:

    - Reads the heights of students from the input and returns them as a list of integers.

2. **Function `calculate_average(list_of_nums)`**:

    - Takes a list of heights and returns the average height. It calculates the sum of all heights and divides it by the number of students.

3. **Function `display_statistics()`**:
    - Displays the statistics for the heights: the shortest student, the tallest student, and the average height.
    - If no input is provided, it outputs `no students`.

### Example:

For input:

```
150
160
155
170
```

The program will output:

```
Height of the shortest student: 150
Height of the tallest student: 170
Average height: 158.75
```

## Output 📜

The program outputs the following statistics:

-   Height of the shortest student
-   Height of the tallest student
-   Average height of all students

Example output:

```
Height of the shortest student: 150
Height of the tallest student: 170
Average height: 158.75
```

If no input is provided, the output will be:

```
no students
```

## Usage 📦

1. Save the code in a file named `student_heights.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script.

### Example usage:

```bash
$ python student_heights.py
150
160
155
170
```

The output will be:

```
Height of the shortest student: 150
Height of the tallest student: 170
Average height: 158.75
```

## Conclusion 🚀

This program helps in calculating and displaying the height statistics for students, which can be useful in various scenarios like analyzing student demographics or providing insights into the distribution of heights in a group.
