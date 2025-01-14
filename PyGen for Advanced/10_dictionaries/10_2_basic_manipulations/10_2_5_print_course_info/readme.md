# Course Information Finder 🎓

## Description 📝

This program retrieves and displays detailed information about a course based on the given course number.
The information includes the room number, instructor's name, and class time. The program uses a dictionary to store and retrieve the course details.

## Purpose 🎯

The purpose of this program is to provide a simple way to look up the details of a course given its course number.
It outputs the room number, instructor, and time for the specified course.

## How It Works 🔍

1. **Input**:
    - The user enters the course number (e.g., 'CS101').
2. **Processing**:
    - The program looks up the entered course number in a predefined dictionary.
3. **Output**:
    - If the course number exists, the program displays the room number, instructor, and class time in a formatted string.
    - If the course number is not found, the program outputs a message stating that the course is not found.

## Output 📜

The program outputs the details of the course if it exists in the dictionary.

### Example:

**Input**:

```
Enter the course number: CS102
```

**Output**:

```
CS102: 4501, Alvarado, 9:00
```

### If Course Not Found:

**Input**:

```
Enter the course number: CS999
```

**Output**:

```
Course CS999 not found.
```

## Usage 📦

1. Save the code in a Python file, e.g., `course_info.py`.
2. Run the script.
3. Input the course number when prompted.
4. The program will display the corresponding course information.

### Example Run:

```plaintext
Enter the course number: CS103
Output: CS103: 6755, Rich, 10:00
```

## Conclusion 🚀

This program provides a quick way to retrieve and display information about a course from a predefined set of courses, making it useful for students or staff looking for class details.
