# Lesson 3.7: Calendar Module 🗓️

## Description 📝

In this lesson, I learned how to use Python's `calendar` module, which provides functions and attributes for working with calendars.
The module includes useful functions like `isleap()`, `monthrange()`, and `prmonth()`, as well as data attributes like `month_name`, `day_name`, and `day_abbr`.
Through a series of practical tasks, I gained experience in working with different aspects of the calendar, such as checking leap years, displaying calendars, and finding specific weekdays or dates.

## Purpose 🎯

The purpose of this lesson was to understand and apply the `calendar` module for tasks such as:

-   Checking if a year is a leap year.
-   Displaying a calendar for a given month and year.
-   Finding specific weekdays for a given date.
-   Identifying important dates like Mondays or third Thursdays of the month.

By completing these tasks, I gained a deeper understanding of how to manipulate and display calendar data in Python.

## How It Works 🔍

The `calendar` module contains various attributes and functions that are helpful for date and time calculations, such as:

-   `day_name`, `day_abbr`, `month_name`, and `month_abbr` for accessing weekday and month names.
-   `setfirstweekday()` and `firstweekday()` for setting and getting the first weekday of the calendar.
-   `isleap()` and `leapdays()` for checking leap years and calculating the number of leap years between two years.
-   `weekday()`, `monthrange()`, and `monthcalendar()` for working with weekdays and month-related data.
-   `calendar()`, `prmonth()`, and `prcal()` for displaying the calendar.

The practical tasks allowed me to apply these functions in real-world scenarios.

## Output 📜

The output for each task was as follows:

1. For the leap year checker, the program printed `True` or `False` based on whether a year is a leap year.
2. The calendar display printed the calendar for a specific month and year.
3. The weekday finder displayed the full name of the weekday for a given date.
4. The days-in-month finder calculated and displayed the number of days in a month.
5. The get days in month function returned a sorted list of all the dates in the given month and year.
6. The get all Mondays function returned a sorted list of all Mondays in a given year.
7. The get all third Thursdays function calculated and displayed the third Thursday of each month in a given year.

## Usage 📦

1. I cloned this repository to my local machine.
2. I navigated to the directory of the task I wanted to work on.
3. I implemented the function for each task based on the provided instructions.
4. I ran the programs to check if they provided the expected results.

## Tasks 🎯

The following tasks were included in this lesson:

### 1. `3_7_1_leap_year`

#### Leap Year Checker

This program checks if a given year is a leap year. The user inputs a year, and the program outputs whether the year is a leap year or not. This is based on the rules of the Gregorian calendar.

### 2. `3_7_2_display_calendar`

#### Calendar Display

This program displays the calendar for a given year and month. The user inputs a year and the abbreviated name of a month (e.g., "Jan"), and the program outputs the corresponding calendar.

### 3. `3_7_3_display_weekday`

#### Day of the Week Finder

This program finds and displays the day of the week for a given date. The user inputs a date in the `YYYY-MM-DD` format, and the program outputs the full name of the weekday (e.g., "Monday").

### 4. `3_7_4_display_number_of_days_in_month`

#### Days in Month Finder

This program calculates the number of days in a specified month of a given year. The user inputs the year and the serial number of the month (e.g., "2" for February), and the program outputs the number of days in that month.

### 5. `3_7_5_display_number_of_days_in_month`

#### Days in Month Finder by Month Name

This program calculates the number of days in a specified month of a given year. The user inputs the year and the full name of the month (e.g., "January"), and the program outputs the number of days in that month.

### 6. `3_7_6_get_days_in_month`

#### Get Days in Month

This program generates a sorted list of all dates in a specific month of a given year. The user inputs the year and the full name of the month, and the program returns a sorted list of dates in that month.

### 7. `3_7_7_get_all_mondays`

#### Get All Mondays in a Year

This program generates a sorted list of all Mondays in a given year. The user inputs a year, and the program outputs a list of all Mondays in that year.

### 8. `3_7_8_get_all_third_thursdays`

#### Get Third Thursday of Each Month

This program calculates and displays the third Thursday of each month for a given year. This is useful for tasks like planning visits to museums that offer free entry on the third Thursday of every month.

## Conclusion 🚀

By completing this lesson, I gained a comprehensive understanding of the `calendar` module and its functions.
I learned how to use the module to check leap years, display calendars, and calculate specific dates, such as all Mondays or the third Thursdays of the year.
These techniques are essential for working with date and time-related tasks in Python.
