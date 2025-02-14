# Lesson 3.4: Timedelta Data Type ⏳

## Description 📝

This lesson is devoted to the `timedelta` data type from Python's `datetime` module.
The timedelta object allows me to represent and manipulate differences between `datetime` or `date` objects.
The lesson covers operations with time intervals, such as adding or subtracting time, comparing time intervals, and calculating differences between dates and times.

The lesson includes 10 practical tasks and 11 theoretical questions, which explore:

-   Adding or subtracting days, seconds, and microseconds
-   Using the `total_seconds()` method
-   Comparing time intervals
-   Operations with `datetime` and `date` objects

## Purpose 🎯

The purpose of this lesson was to introduce me to the `timedelta` data type, its attributes, and its methods.
By the end of the lesson, I learned how to perform arithmetic on `datetime` objects, such as calculating the number of days between dates, finding future dates based on intervals, and working with missing dates.

## How It Works 🔍

The core concepts covered in this lesson include:

-   **Days, Seconds, Microseconds Attributes:** These attributes allow me to specify a time interval and manipulate it.
-   **`total_seconds()` Method:** This method provides the total number of seconds in a `timedelta` object.
-   **Comparison of Time Intervals:** I learned how to compare two `timedelta` objects.
-   **Operations on `timedelta` and `datetime` Objects:** I can add or subtract `timedelta` objects to/from `datetime` or `date` objects.
-   **Operations on `date` Objects:** Operations like calculating the difference in days between two `date` objects.

## Output 📜

The outputs of the tasks vary depending on the specific operation:

-   Formatted strings representing adjusted dates
-   Lists of dates, including missing ones
-   Number of days or seconds between dates
-   Calculated time after a certain period has passed
-   Count of specific days (e.g., Sundays) within a given year

## Usage 📦

1. I cloned this repository to my local machine.
2. I navigated to the directory of the lesson I wanted to work on.
3. I implemented the corresponding function for each task in the provided files.
4. I tested my code using the given inputs and ensured it produced the correct output.

## Tasks 🎯

The following practical tasks were part of this lesson:

### 1. `3_4_1_add_one_week_and_12_hours_to_datetime`

#### Add Time to Datetime ⏳

This function adds a specified number of weeks and hours to a given `datetime` object and returns the updated result as a formatted string.

### 2. `3_4_2_days_until_birthday`

#### Days Between Dates 📅

This function calculates the absolute number of days between two `date` objects.

### 3. `3_4_3_display_adjacent_dates`

#### Get Adjacent Dates 📅

This program takes a date as input and returns the previous and next dates in the format "DD.MM.YYYY".

### 4. `3_4_4_get_seconds_since_midnight`

#### Get Seconds Since Midnight ⏰

This program takes a time as input and calculates the number of seconds that have passed since midnight (00:00:00).

### 5. `3_4_5_time_after_timer`

#### Time After Timer ⏲️

This program takes a time as input and adds a user-defined timer duration (in seconds) to it, then outputs the new time after the specified interval.

### 6. `3_4_6_num_of_sundays`

#### Count the Sundays of the Year 📅

This program calculates the number of Sundays in a given year.

### 7. `3_4_7_calculate_task_preparation_dates`

#### Task Preparation Dates 📅

This program helps Arthur prepare tasks for his "OOP in Python" course by calculating the dates on which he should prepare each task, following a rule: each subsequent task takes one more day than the previous one.

### 8. `3_4_8_calculate_days_difference`

#### Date Difference Calculator 📅

This program calculates the number of days between two adjacent dates in a given sequence.

### 9. `3_4_9_fill_up_missing_dates`

#### Missing Date Filler 📅

This program takes a list of dates in the "DD.MM.YYYY" format, sorts them, and fills in any missing dates between them.

### 10. `3_4_10_display_schedule`

#### Math Tutor Class Schedule 🗓️

This program generates a class schedule for a math tutor, factoring in 45-minute lessons and 10-minute breaks. It helps the tutor organize their working day based on input times.

## Conclusion 🚀

This lesson provided me with a solid understanding of the `timedelta` data type in Python, enabling me to perform various operations with time and dates. I now know how to calculate time differences, add or subtract time intervals, and work with date ranges effectively. The practical tasks reinforced my knowledge, and I feel confident in applying these concepts to solve real-world problems related to date and time calculations.
