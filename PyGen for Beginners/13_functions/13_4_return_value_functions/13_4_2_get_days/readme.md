# Month Day Calculation Program 📅

## Description 📝

This Python program takes the number of a month (from 1 to 12) and returns the number of days in that month.
It assumes the year is a non-leap year.

## Purpose 🎯

-   To determine how many days are in a given month.
-   Useful for applications related to calendar management, scheduling, or date computations.

## How It Works 🔍

1. **Function `get_days(month)`**:
    - Takes one input parameter: `month` (an integer between 1 and 12 representing a month).
    - It checks which month it is and returns the number of days based on the following:
        - 31 days for months: January, March, May, July, August, October, December.
        - 30 days for months: April, June, September, November.
        - 28 days for February (since it's assumed to be a non-leap year).
2. **Example**:
   For the input `month = 2`, the output will be:
    ```
    28
    ```

## Usage 📦

1. Copy the code into a Python file, e.g., `month_days.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python month_days.py
    ```
5. Input the number of a month (1 to 12), and the program will print the number of days in that month.

## Conclusion 🚀

This program helps calculate the number of days in a specific month, assuming a non-leap year.
It can be useful for applications involving date ranges, calendars, and scheduling.
