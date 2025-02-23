# Second Lowest Grade Student Finder

## Description 📝

This Python program reads a list of student names and their exam grades, then determines and prints the name of the student with the second lowest grade.

## Purpose 🎯

The program processes multiple lines of input where each line contains a student's name and their grade.
It identifies the second lowest grade and prints the corresponding student's name.

## How It Works 🔍

1. Reads multiple lines of input, where each line contains:
    ```
    <student_name> <grade>
    ```
2. Parses the input into a list of tuples: `[(name, grade), ...]`
3. Identifies the second lowest grade by sorting unique grades.
4. Finds the student(s) with this grade.
5. Prints the first student (based on input order) with the second lowest grade.

## Output 📜

The program prints only **one** student name:

-   If multiple students have the second lowest grade, the one who appeared first in the input is chosen.

### Example 1:

#### Input:

```
Alice 85
Bob 76
Charlie 90
David 76
Eve 92
```

#### Processing:

-   Unique grades: `[76, 85, 90, 92]`
-   Second lowest grade: `85`
-   Student with this grade: `Alice`

#### Output:

```
Alice
```

### Example 2:

#### Input:

```
Tom 45
Jerry 50
Spike 60
Tyke 50
```

#### Processing:

-   Unique grades: `[45, 50, 60]`
-   Second lowest grade: `50`
-   Students with this grade: `["Jerry", "Tyke"]`
-   The first occurrence in input: `"Jerry"`

#### Output:

```
Jerry
```

## Usage 📦

1. Run the script.
2. Provide input (name and grade per line).
3. The program will output the name of the student with the second lowest grade.

### Example:

```sh
# Run the script and enter:
Alice 85
Bob 76
Charlie 90
David 76
Eve 92

# Program output:
Alice
```

## Conclusion 🚀

This program efficiently processes student grades, sorts them, and finds the student with the second lowest grade, making it useful for ranking and educational analysis.
