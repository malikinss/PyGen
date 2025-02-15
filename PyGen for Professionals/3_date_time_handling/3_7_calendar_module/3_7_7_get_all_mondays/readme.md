# Get All Mondays in a Year

## Description 📝

This Python program provides a function `get_all_mondays()` that takes a year as an argument and returns a sorted list of all Mondays in that year.

## Purpose 🎯

The purpose of this program is to generate a list of all Mondays in a specific year.
This can be useful for scheduling, planning, or any other tasks that need to identify all the Mondays in a given year.

## How It Works 🔍

1. **Function `get_all_weekdays_in_year(year, target_weekday)`**:

    - Iterates through all the months of the specified year.
    - Checks each day to see if it matches the target weekday (0 for Monday, 1 for Tuesday, etc.).
    - Returns a sorted list of all dates that fall on the specified weekday.

2. **Function `get_all_mondays(year)`**:
    - Calls `get_all_weekdays_in_year()` with the target weekday set to `0` (Monday).
    - Returns a list of all Mondays in the given year.

### Example:

For input:

```python
get_all_mondays(2021)
```

The output will be:

```python
[datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., datetime.date(2021, 12, 27)]
```

## Output 📜

The function returns a sorted list of all dates in the specified year that fall on a Monday.

Example output:

```python
[datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., datetime.date(2021, 12, 27)]
```

## Usage 📦

1. Save the code in a file named `get_all_mondays.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script or import the `get_all_mondays()` function into another Python script to use.

### Example usage:

```python
from get_all_mondays import get_all_mondays

mondays = get_all_mondays(2024)
for monday in mondays:
    print(monday)
```

## Conclusion 🚀

This program provides a simple yet powerful utility for retrieving all Mondays in a specific year.
Whether you need to schedule events, plan tasks, or simply track all the Mondays in a year, this function will help you do so efficiently. 🗓️
