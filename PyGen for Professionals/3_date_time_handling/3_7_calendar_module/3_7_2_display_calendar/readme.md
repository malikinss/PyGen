# Calendar Display

## Description 📝

This Python program displays the calendar for a given year and month.
The user is asked to input a year and the abbreviated name of a month in English.
The program then displays the corresponding calendar for the given year and month.

## Purpose 🎯

The purpose of this program is to allow the user to view the calendar for any given month and year by entering the year and month abbreviation.

## How It Works 🔍

1. **User Input**:
    - The program prompts the user to enter a year and a month abbreviation (e.g., '2024 Jan').
2. **Validation**:
    - The program checks if the input is valid. It ensures the year is a number and the month abbreviation is correct.
3. **Calendar Display**:
    - The program uses Python's built-in `calendar.prmonth()` function to print the calendar for the specified month and year.

### Example:

For input:

```
2024 Jan
```

The output will be the calendar for January 2024.

## Output 📜

The program will display the calendar for the specified month and year in the terminal.

Example:

```
    January 2024
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
```

## Usage 📦

1. Save the code in a file named `calendar_display.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python calendar_display.py`
5. Enter the year and month abbreviation when prompted, e.g., `2024 Jan`.

## Conclusion 🚀

This program allows the user to easily view the calendar for any specific month and year.
It demonstrates simple date manipulation using Python's `calendar` module and provides an easy-to-use interface for users to interact with. 📅
