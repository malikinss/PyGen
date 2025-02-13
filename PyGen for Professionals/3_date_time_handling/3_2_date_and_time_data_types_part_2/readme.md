# Lesson 3.2: Date and Time Data Types (Part 2) 🗓️

## Description 📝

This lesson delves into formatting and parsing dates and times using Python.
I worked with various date and time data types, learning how to manipulate and format them in a way that suits different needs.
The lesson contains 9 practical tasks, where I applied formatting, localization, and validation techniques, and 5 theoretical questions presented on the Stepik website.

## Purpose 🎯

The goal of this lesson was to understand how to format and manipulate date and time data effectively.
I explored ways to convert strings into date and time objects, validated dates, and applied different formats for different use cases.

## How It Works 🔍

In this lesson, I focused on the following key concepts:

-   **Formatting Date and Time**: Displaying dates in different formats, including localized formats.
-   **Using Localization**: Handling date and time formatting based on different regional settings.
-   **Converting Strings to Date and Time**: Parsing date strings and converting them into date objects for further manipulation.
-   **Date Validation**: Ensuring the accuracy and correctness of user-provided date inputs.

## Output 📜

The outputs for each task vary depending on the specific function, including:

-   Displaying extracted components of a given date or time object
-   Showing dates in multiple formats
-   Validating and checking the correctness of dates
-   Sorting and filtering dates based on specific criteria

## Usage 📦

1. I cloned this repository to my local machine.
2. I navigated to the folder of the lesson I wanted to work on.
3. I implemented each function described in the tasks and tested them with sample data.
4. I observed the output and ensured that my code worked correctly by checking the results.

## Tasks 🎯

The following practical tasks were part of this lesson:

### 1. `3_2_1_display_alarm_components`

#### Alarm Time Components

This function extracts and prints the hours, minutes, and seconds from a given `time` object in a formatted way.

### 2. `3_2_2_display_birthday_components`

#### Birthday Date Components

This function extracts and prints key components from a given `date` object, such as the full month name, weekday name, year, month number, and day of the month.

### 3. `3_2_3_display_local_dates`

#### First Hurricane Date Formatter

This function extracts the earliest date from a list of Florida hurricane occurrences and prints it in three different formats.

### 4. `3_2_4_display_date_in_different_formats`

#### Hurricane Andrew Date Formatter

This function prints the date of Hurricane Andrew (August 24, 1992) in three different formats.

### 5. `3_2_5_select_min_date`

#### Select Minimum Date

This function takes two dates as input, compares them, and outputs the smaller (earliest) date in a specific format.

### 6. `3_2_6_display_sorted_dates`

#### Sort Dates in Non-Decreasing Order

This program takes a sequence of dates as input, sorts them in non-decreasing order, and outputs the sorted dates in the `DD/MM/YYYY` format.

### 7. `3_2_7_print_good_dates`

#### Find Interesting Dates

This program takes a list of dates and outputs the "interesting" ones in ascending order. A date is considered interesting if its year coincides with the user's year of birth, and the sum of the month number and day number equals the user's age.

### 8. `3_2_8_is_date_correct`

#### Validate Date Function

This function checks whether a given date (day, month, and year) is valid or not. It uses Python's `datetime.date` to validate the input and returns `True` if the date is valid and `False` if it is not.

### 9. `3_2_9_check_correct_dates`

#### Date Validity Checker Program

This program checks the correctness of dates entered by the user. The input dates should be in the format `DD.MM.YYYY`. The program will validate each date, indicating whether it is correct or incorrect, and at the end, it will display the total number of correct dates.

## Conclusion 🚀

This lesson helped me master various techniques for formatting, validating, and parsing dates and times in Python. I gained a deeper understanding of how to manage date and time data, ensuring they are accurate and displayed in a user-friendly way. These skills are essential for working with time-sensitive applications and ensuring date-related operations are handled correctly.
