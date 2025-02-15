# Get Days in Month

## Description 📝

This Python program provides a function `get_days_in_month()` that, given a year and the full name of a month, returns a sorted list of all dates in that month of the given year.

## Purpose 🎯

The purpose of this program is to generate a list of all dates in a specific month of a specific year, sorted in ascending order.
This can be useful for tasks that require all the dates of a given month.

## How It Works 🔍

1. **Function `get_month_number_by_name(month_name)`**:

    - Converts the full month name (e.g., "January", "February") to its corresponding month number (1 for January, 2 for February, etc.).
    - Raises a `ValueError` if the month name is invalid.

2. **Function `get_days_in_month(year, month)`**:
    - Uses the `get_month_number_by_name()` function to convert the month name to its number.
    - Uses the `calendar.monthrange()` function to get the number of days in the month.
    - Creates a list of `date` objects for all the days in the given month and year.

### Example:

For input:

```python
get_days_in_month(2021, 'December')
```

The output will be:

```python
[datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ..., datetime.date(2021, 12, 31)]
```

## Output 📜

The function returns a sorted list of all dates in the specified month.

Example output:

```python
[datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ..., datetime.date(2021, 12, 31)]
```

## Usage 📦

1. Save the code in a file named `get_days_in_month.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script or import the `get_days_in_month()` function into another Python script to use.

### Example usage:

```python
from get_days_in_month import get_days_in_month

dates = get_days_in_month(2024, 'February')
for date in dates:
    print(date)
```

## Conclusion 🚀

This program provides a simple yet powerful utility for working with dates.
It generates a sorted list of all dates in a specified month and year, which can be used for various applications like event scheduling, date comparison, and more. 📅
