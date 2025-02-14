# Employee Age Comparison Program 👥

## Description 📝

This program reads a list of employees with their first name, last name, and date of birth.
It then determines the oldest employee and prints their birth date and full name.
If there are multiple employees with the same oldest age, the program prints the birth date and the number of such employees.

## Purpose 🎯

The goal of this program is to identify the most senior employee from a list.
It determines the employee with the earliest birth date and displays their details.
If multiple employees share the same birth date, their count is displayed.

## How It Works 🔍

1. The user inputs the number of employees (`n`).
2. For each employee, the program reads their first name, last name, and date of birth.
3. The program determines the oldest employee by finding the earliest birth date.
4. It prints either the oldest employee's full name and birth date or, if multiple oldest employees exist, their birth date and count.

### Example:

```python
# Running the program will ask for input:
num_employees = int(input())  # Enter the number of employees
# Enter data for each employee in the format: first name, last name, DD.MM.YYYY
display_oldest_employee()  # The program will display the oldest employee(s)
```

## Output 📜

The program will output either:

-   The birth date and full name of the oldest employee, or
-   The birth date and the number of employees who share the same oldest age.

### Example output:

```
01.01.1980 John Doe
```

If there are multiple oldest employees, the output will be:

```
01.01.1980 3
```

## Usage 📦

1. Enter the number of employees (`n`).
2. For each employee, input their first name, last name, and date of birth.
3. The program will output the oldest employee’s details or the count if there are multiple employees with the same birth date.

## Conclusion 🚀

This program helps determine the most senior employee in an organization based on birth dates, useful for managing employee records or simply finding the oldest employee in a list.
