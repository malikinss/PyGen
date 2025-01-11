# Union of Remembered Students 📚

## Description 📝

The head and the assistant of the online school BEEGEEK each have a list of students they remember. This program finds and outputs the names of all the students that both the head and the assistant remember.

## Purpose 🎯

To identify all unique students remembered by either the head or the assistant and output their names in sorted order.

## How It Works 🔍

1. **Inputs**:
    - A list of students remembered by the head of the school.
    - A list of students remembered by the assistant.
2. **Logic**:
    - The program finds the union of the two lists, which contains all unique students from both lists.
    - The result is sorted in ascending order before being output.
3. **Outputs**:
    - A sorted list of all unique student names.

## Output 📜

The program outputs the names of all students remembered by the head and the assistant, sorted in alphabetical order.

### Example:

**Input**:

```
Alice Bob Charlie
Charlie David Eve
```

**Output**:

```
Alice Bob Charlie David Eve
```

### Explanation:

-   **Head's list**: `{'Alice', 'Bob', 'Charlie'}`
-   **Assistant's list**: `{'Charlie', 'David', 'Eve'}`
-   **Union of both lists**: `{'Alice', 'Bob', 'Charlie', 'David', 'Eve'}`

The sorted output is:

```
Alice Bob Charlie David Eve
```

## Usage 📦

1. Save the code in a Python file, e.g., `union_of_students.py`.
2. Run the script.
3. Provide two lines of input:
    - The first line contains the names of students remembered by the head.
    - The second line contains the names of students remembered by the assistant.
4. View the sorted list of all unique students.

### Example Run:

```plaintext
Input:
Tom Jane Peter
John Tom Alice

Output:
Alice Jane John Peter Tom
```

## Conclusion 🚀

This program efficiently finds all the students remembered by both the head and the assistant and outputs them in a clear, sorted format. It’s particularly useful for organizing lists of names and ensuring no duplicates.
