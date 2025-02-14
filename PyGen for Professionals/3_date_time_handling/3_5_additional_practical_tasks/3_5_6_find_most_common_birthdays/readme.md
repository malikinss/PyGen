# Employee Birthday Popularity Program 🎉

## Description 📝

This program reads a list of employees with their first name, last name, and birth date, and determines which date has the most employees born.
If multiple dates have the same number of employees, the program outputs them all in ascending order.

## Purpose 🎯

The purpose of this program is to identify which birth dates are most common among employees.
The program reads employee birth dates, counts the occurrences, and displays the dates with the highest frequency.

## How It Works 🔍

1. The user inputs the number of employees (`n`).
2. For each employee, the program reads their first name, last name, and birth date.
3. The program counts how many employees share the same birth date.
4. It outputs the most common birth dates, sorted in ascending order, in the format `DD.MM.YYYY`.

### Example:

```python
# Running the program will ask for input:
num_employees = int(input())  # Enter the number of employees
# Enter data for each employee in the format: first name, last name, DD.MM.YYYY
display_dates(most_common_birthdays)  # The program will display the most common birthdays
```

## Output 📜

The program will output the date(s) with the most employees born on it.
If there are multiple dates, they will be printed in ascending order, each on a separate line.

### Example output:

```
01.01.1980
15.05.1990
```

## Usage 📦

1. Enter the number of employees (`n`).
2. For each employee, input their first name, last name, and birth date.
3. The program will output the most popular birth dates, sorted in ascending order.

## Conclusion 🚀

This program helps determine which birth dates are the most popular among employees, making it useful for analyzing employee demographics or planning company events based on birthdays.
