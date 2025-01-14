# Users with Phone Ending in 8 Finder 📱8️⃣

## Description 📝

This program identifies users whose phone numbers end with the digit '8' from a list of user data.
It checks whether the phone number ends with '8' and then outputs the names of those users in alphabetical order.

## Purpose 🎯

The purpose of this program is to filter out users whose phone numbers end with '8'.
It helps in finding specific users based on phone number patterns.

## How It Works 🔍

1. **Input**:
    - A list of dictionaries representing users, where each dictionary contains user details, including their name and phone number.
2. **Processing**:
    - The program checks whether the phone number of each user ends with the digit '8'.
3. **Output**:
    - The program collects the names of users whose phone numbers end with '8' and sorts them in alphabetical order.
    - The names are printed on a single line, separated by spaces.

## Output 📜

The output is a single line containing the names of users whose phone numbers end with '8', sorted alphabetically.

### Example:

**Input**:

```python
users = [
    {'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
    # More users...
]
```

**Output**:

```plaintext
Fedor Helga Riyad Roman
```

## Usage 📦

1. Save the code in a Python file, e.g., `find_users_with_phone_ending_in_8.py`.
2. Run the script.
3. The program will process the provided list of users and display the names of those whose phone numbers end with '8'.

### Example Run:

```plaintext
Enter the user list: [User data]
Output: Fedor Helga Riyad Roman
```

## Conclusion 🚀

This program helps identify users whose phone numbers end with '8', making it useful for filtering or sorting user data based on specific patterns.
