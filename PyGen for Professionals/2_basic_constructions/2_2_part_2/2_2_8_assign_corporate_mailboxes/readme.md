# Corporate Emailbox Assigner for BEEGEEK Online School

## Description 📝

This program assigns unique corporate email addresses to new employees at the BEEGEEK online school.
The email addresses are generated based on the employee's first and last name in the format `<first-name-last-name>@beegeek.bzz`.
If an email address already exists, a number is appended to the email to make it unique.

## Purpose 🎯

The program ensures that every employee gets a unique email address by adding a number to the email if the initial one is already taken.
It handles cases where employees may share the same name.

## How It Works 🔍

1. The program first reads the number of already assigned email boxes and the list of these emails.
2. It then reads the number of new employees and their first and last names.
3. For each new employee:
    - It checks if their email address already exists.
    - If the address is taken, it adds a number (starting from 1) to generate a unique address.
4. The program outputs the list of new email addresses assigned to the employees.

## Output 📜

Example usage and expected outputs:

```python
Enter the number of already issued emailboxes: 3
timyr-guev@beegeek.bzz
timyr-guev1@beegeek.bzz
timyr-guev2@beegeek.bzz

Enter the number of new employees: 2
timyr-guev
timyr-guev

# Output:
timyr-guev3@beegeek.bzz
timyr-guev4@beegeek.bzz
```

If there are no conflicts and no number is required:

```python
Enter the number of already issued emailboxes: 1
timyr-guev@beegeek.bzz

Enter the number of new employees: 2
alex-smith
timyr-guev

# Output:
alex-smith@beegeek.bzz
timyr-guev1@beegeek.bzz
```

## Usage 📦

1. Clone this repository.
2. Navigate to the project directory.
3. Use the program in your script or interactive Python shell.

Example:

```python
from email_assigner import assign_corporate_emailboxes

assigned_emails = assign_corporate_emailboxes()
print("\n".join(assigned_emails))
```

## Conclusion 🚀

The program efficiently assigns unique email addresses to new employees while avoiding conflicts with already assigned addresses.
It ensures that each employee has a recognizable and distinct email for work communication.
