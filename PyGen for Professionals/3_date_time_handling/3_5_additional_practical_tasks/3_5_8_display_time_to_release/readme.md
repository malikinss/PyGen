# Time Until Course Release Program ⏳

## Description 📝

This program calculates how much time is left until the release of a course.
It takes the current date and time as input and outputs the time remaining until the course is released, formatted appropriately (days, hours, and minutes).
If the release time has already passed, it outputs that the course is out now.

## Purpose 🎯

The purpose of this program is to calculate and display the remaining time until a specific course release.
It helps users stay updated on the course release timeline and shows time in an easy-to-understand format.

## How It Works 🔍

1. The user inputs the current date and time in the format `'DD.MM.YYYY HH:MM'`.
2. The program compares the current time to the course release time, which is fixed at `08.11.2022 12:00`.
3. If the current time is before the release, it calculates the remaining time in days, hours, and minutes.
4. The program displays the remaining time in the appropriate format:
    - If more than a day remains: `'X days and Y hours left until the course is released'`
    - If less than a day remains: `'X hours and Y minutes left until the course is released'`
    - If only minutes remain: `'X minutes left until the course is released'`
5. If the current time is after or equal to the release time, the program outputs: `'The course is out now!'`

### Example:

```python
# Running the program will ask for input:
current_time = input()  # Enter the current time in the format 'DD.MM.YYYY HH:MM'
# The program will display the remaining time until the course release
```

## Output 📜

The program will output the remaining time in one of the following formats:

-   `'There are: <number of days> days and <number of hours> hours left until the course is released'`
-   `'There are: <number of hours> hours and <number of minutes> minutes left until the course is released'`
-   `'There are: <number of minutes> minutes left until the course is released'`
-   If the release time has already passed, it outputs: `'The course is out now!'`

### Example output:

```
There are: 2 days and 3 hours left until the course is released
```

## Usage 📦

1. Enter the current date and time in the format `'DD.MM.YYYY HH:MM'`.
2. The program will calculate and display the remaining time until the course release.

## Conclusion 🚀

This program allows you to track how much time remains until the release of a course.
It gives a clear, formatted output and helps keep track of important release deadlines.
