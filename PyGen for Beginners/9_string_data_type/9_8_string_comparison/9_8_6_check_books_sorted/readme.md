# Home Library Sort Checker 📚

## Description 📝

This program checks whether a list of books in Dushnila's home library is sorted in ascending order:

1. First by the author's last name.
2. If the last names match, by the book's title.

## Purpose 🎯

To ensure that books are correctly sorted according to Dushnila's specific rules for library organization.

## How It Works 🔍

1. The program takes an integer `n` as input, representing the number of books.
2. For the next `n` lines, each line contains a book's information in the format:
   `<author's last name> <author's initials>, "<book title>"`

3. The program:

-   Extracts the author's last name and book title from each entry.
-   Checks whether the books are sorted correctly based on the last name and, if needed, the title.

4. Outputs:

-   `"YES"` if the books are sorted correctly.
-   `"NO"` otherwise.

### Example

**Input:**
3 Smith J., "Alpha"
Smith J., "Beta"
Brown P., "Gamma"

**Output:**
NO

**Explanation:**

-   The first two books have the same author's last name ("Smith"), so they are compared by title, which is correctly ordered.
-   However, "Smith" comes after "Brown," so the list is not sorted correctly.

## Usage 📦

1. Copy the code into a Python script file.
2. Run the script in a terminal or an IDE.
3. Input the number of books (`n`) and their details, each on a new line.
4. The program will output `"YES"` if the books are sorted correctly or `"NO"` otherwise.

## Conclusion 🚀

This program provides a convenient way to validate the sorting of books in a library according to specified rules. It ensures the collection adheres to a proper order, simplifying organization and retrieval.
