# Days in Month Finder by Month Name

## Description 📝

This Python program determines the number of days in a specified month of a given year.
The user inputs the year and the full name of the month in English, and the program outputs the number of days in that month.

## Purpose 🎯

The purpose of this program is to calculate the number of days in any given month by providing the full name of the month (e.g., "January") and the year.

## How It Works 🔍

1. **User Input**:
    - The program prompts the user to enter the year and the full name of the month (e.g., "2024 February").
2. **Month Name Processing**:
    - The input is split into the year and month name. The month name is capitalized to match the format in Python’s `calendar` module.
3. **Days Calculation**:
    - The program uses the `calendar.monthrange()` function to determine the number of days in the specified month.
    - The `calendar.month_name` list is used to map the full month name to its corresponding month number.

### Example:

For input:

```
2024 February
```

The output will be:

```
29
```

## Output 📜

The program will output the number of days in the specified month.

Example output:

```
31
```

## Usage 📦

1. Save the code in a file named `days_in_month_finder_by_name.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python days_in_month_finder_by_name.py`
5. Enter the year and full month name when prompted.

## Conclusion 🚀

This program allows users to easily find the number of days in a given month using the month’s full name.
It demonstrates how to work with the `calendar` module and process string input in Python. 📅
