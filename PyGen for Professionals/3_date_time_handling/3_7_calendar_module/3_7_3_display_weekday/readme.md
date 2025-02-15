# Day of the Week Finder

## Description 📝

This Python program takes a date in the `YYYY-MM-DD` format and outputs the full name of the corresponding day of the week in English.
The user is prompted to input a date, and the program then displays the full name of the weekday for that date.

## Purpose 🎯

The purpose of this program is to enable users to easily find out which day of the week a particular date falls on.

## How It Works 🔍

1. **User Input**:
    - The program asks the user to enter a date in the `YYYY-MM-DD` format.
2. **Date Conversion**:
    - The input string is converted into a `datetime.date` object.
3. **Weekday Calculation**:
    - The program calculates the day of the week using Python's `calendar.day_name[]` and outputs the corresponding full name of the weekday.

### Example:

For input:

```
2024-02-15
```

The output will be:

```
Thursday
```

## Output 📜

The program will display the full name of the weekday for the entered date.

Example output:

```
Monday
```

## Usage 📦

1. Save the code in a file named `day_of_week_finder.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python day_of_week_finder.py`
5. Enter a date in the `YYYY-MM-DD` format when prompted.

## Conclusion 🚀

This program allows users to quickly determine which day of the week a particular date falls on.
It demonstrates how to work with dates and times using Python's `datetime` and `calendar` modules. 🌍
