# Users Without Email Finder 📧❌

## Description 📝

This program identifies users who do not have email information from a list of dictionaries containing user data.
It checks if the 'email' key is either missing or empty, and then outputs the names of those users in alphabetical order.

## Purpose 🎯

The purpose of this program is to filter out users without email information from a given list of users.
The names of these users are then printed in alphabetical order, which can be useful for further processing or reporting.

## How It Works 🔍

1. **Input**:
    - A list of dictionaries representing users, each containing fields like 'name' and 'email'.
2. **Processing**:
    - The program iterates over each dictionary in the list, checking whether the 'email' key is missing or empty.
3. **Output**:
    - The program collects the names of users without email information and sorts them in alphabetical order.
    - The names are printed on a single line, separated by spaces.

## Output 📜

The output is a single line containing the names of users who do not have email information, sorted alphabetically.

### Example:

**Input**:

```python
users = [
    {'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
    {'name': 'Helga', 'phone': '555-1618'},
    {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
    # More users...
]
```

**Output**:

```plaintext
Fedor Helga John Olga Robert Roman
```

## Usage 📦

1. Save the code in a Python file, e.g., `find_users_without_email.py`.
2. Run the script.
3. The program will process the provided list of users and display the names of those without email addresses.

### Example Run:

```plaintext
Enter the user list: [User data]
Output: Fedor Helga John Olga Robert Roman
```

## Conclusion 🚀

This program helps identify users who lack email information, making it useful for database management or contact list validation.
