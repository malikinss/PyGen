# Summer Reading List Checker 📚

## Description 📝

At the end of the school year, Ruslan received a summer reading list from his school. To prepare, he needs to determine which books from the list are already available in his home library. This program helps Ruslan check each book in his reading list against his library collection.

## Purpose 🎯

To help Ruslan (or anyone with a similar task) determine which books from a required list are present in their library and which are missing.

## How It Works 🔍

1. **Inputs**:
    - The number of books in Ruslan's library.
    - The number of books on the summer reading list.
    - A list of book titles in Ruslan's library.
    - A list of book titles in the summer reading list.
2. **Logic**:
    - For each book in the summer reading list:
        - Check if the book exists in Ruslan's library (using a set for quick lookup).
    - Print `"YES"` if the book is available and `"NO"` if it is not.
3. **Output**:
    - The program outputs one line for each book in the summer reading list:
        - `"YES"` if the book is found in the library.
        - `"NO"` if the book is not found.

## Output 📜

For each book in the summer reading list, the program outputs whether Ruslan already has the book.

### Example:

**Input**:

```
5
3
War and Peace
Crime and Punishment
The Brothers Karamazov
Anna Karenina
Dead Souls
War and Peace
The Idiot
Crime and Punishment
```

**Output**:

```
YES
NO
YES
```

### Explanation:

-   Ruslan's library contains:
    `["War and Peace", "Crime and Punishment", "The Brothers Karamazov", "Anna Karenina", "Dead Souls"]`
-   Summer reading list:
    `["War and Peace", "The Idiot", "Crime and Punishment"]`
-   `"War and Peace"` and `"Crime and Punishment"` are in the library, but `"The Idiot"` is not.

## Usage 📦

1. Save the code in a Python file, e.g., `reading_list_checker.py`.
2. Run the script.
3. Provide inputs in the following order:
    - Number of books in Ruslan's library.
    - Number of books on the summer reading list.
    - Titles of books in the library (one per line).
    - Titles of books in the summer reading list (one per line).
4. The program will output whether each book is present in the library or not.

### Example Run:

```plaintext
Input:
4
2
1984
Brave New World
Fahrenheit 451
To Kill a Mockingbird
1984
Moby Dick

Output:
YES
NO
```

## Conclusion 🚀

This program simplifies the task of verifying book availability by efficiently comparing a summer reading list against a library collection.
It's a practical tool for students, teachers, or book enthusiasts who need to organize their reading plans.
