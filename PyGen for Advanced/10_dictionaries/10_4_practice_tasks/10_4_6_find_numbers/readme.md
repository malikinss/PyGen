# Phonebook Finder 📱

## Description 📝

This program allows Timur to store and search for phone numbers of his friends. The phonebook is built from a list of names and phone numbers. Users can query the phonebook to find the phone numbers of specific friends.

## Purpose 🎯

The purpose of this program is to provide a simple way to store and retrieve phone numbers for a group of friends, which can be useful for organization or quick access to contact information.

## How It Works 🔍

1. **Input**:
    - The program first takes input for the number of phonebook entries, where each entry consists of a name and a phone number.
2. **Phonebook Creation**:
    - A dictionary is created where the keys are names and the values are lists of phone numbers.
3. **Queries**:
    - The program then allows users to query the phonebook by providing a name. It returns all the phone numbers associated with that name.
4. **Output**:
    - The phone numbers of the queried name are printed, separated by spaces. If the name is not found, a "Not Found" message is displayed.

## Output 📜

The program prints:

-   The phone numbers associated with the queried name, or "Not Found" if the name does not exist in the phonebook.

### Example Input/Output:

**Input**:

```text
Enter the number of phonebook entries: 3
Enter phone and name: 1234567890 Tim
Enter phone and name: 9876543210 Tim
Enter phone and name: 1112223333 Alice
Enter the number of queries: 2
Enter the name to search: Tim
Enter the name to search: Alice
```

**Output**:

```text
1234567890 9876543210
1112223333
```

## Usage 📦

1. Copy the code into a Python file, e.g., `phonebook.py`.
2. Run the program.
3. Enter the number of phonebook entries when prompted.
4. Input each phone number and the corresponding name.
5. Enter the number of queries to make.
6. Input the names you want to search for.

### Example Run:

```python
# Sample run
Enter the number of phonebook entries: 2
Enter phone and name: 5551234567 Tim
Enter phone and name: 6669876543 Alice
Enter the number of queries: 1
Enter the name to search: Tim
Output:
5551234567
```

## Conclusion 🚀

This program offers a simple way to manage and search through a phonebook, making it easy for users to store multiple phone numbers under each friend's name and retrieve them quickly.
