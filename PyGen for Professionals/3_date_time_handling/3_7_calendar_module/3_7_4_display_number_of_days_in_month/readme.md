# Days in Month Finder

## Description 📝

This Python program determines the number of days in a specified month of a given year.
The user inputs the year and the serial number of the month, and the program outputs the number of days in that month.

## Purpose 🎯

The purpose of this program is to calculate the number of days in any given month based on the year and the month number.

## How It Works 🔍

1. **User Input**:
    - The program prompts the user to enter the year and the serial number of the month (starting from 1 for January).
2. **Month and Year Processing**:
    - The input is split into the year and the month number.
3. **Days Calculation**:
    - The program uses Python's `calendar.monthrange()` function to determine the number of days in the specified month.

### Example:

For input:

```
2024 2
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

1. Save the code in a file named `days_in_month_finder.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python days_in_month_finder.py`
5. Enter the year and month number when prompted.

## Conclusion 🚀

This program allows users to easily find the number of days in a given month of any year.
It demonstrates how to work with the `calendar` module in Python for handling date-related tasks. 📅
