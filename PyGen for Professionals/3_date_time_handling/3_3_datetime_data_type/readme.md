# Lesson 3.3: Datetime Data Type 📆⏳

## Description 📝

This lesson explores the `datetime` data type from Python’s `datetime` module.
You will learn how to create, manipulate, format, and convert date-time values.
The lesson also covers timestamp conversions and practical applications for managing date-time data efficiently.

## Purpose 🎯

The goal of this lesson is to gain a solid understanding of how to work with the `datetime` module.
By the end of this lesson, you will be able to:

-   Convert strings to `datetime` objects.
-   Work with timestamps and elapsed seconds.
-   Analyze purchase activity based on time.
-   Combine and sort date-time values.
-   Determine the fastest student in a given task.
-   Sort records based on their timestamps.
-   Check room availability based on booking dates.

## How It Works 🔍

### Topics Covered:

-   `datetime` data type
-   Methods: `combine()`, `date()`, `time()`
-   Methods: `now()`, `utcnow()`, `today()`
-   Method: `timestamp()`
-   Formatting `datetime` objects
-   Converting strings to `datetime`

### Tasks Overview:

1. **Date and Time Extractor Program** 📅
    - Extracts a date and time from a string and converts it into a `datetime` object.
2. **Seconds and Datetime Converter Program** ⏲

    - Converts between seconds elapsed since the epoch and `datetime` objects.

3. **Purchase Activity Analyzer** 🛍

    - Determines whether more purchases were made before or after noon.

4. **Date and Time Merger and Sorter** 🔄

    - Combines and sorts `datetime` objects based on their second values.

5. **Fastest Student Finder** 🏆

    - Identifies the student who completed their homework the fastest.

6. **Astronaut’s Diary Sorter** 🚀

    - Reads an astronaut's diary and sorts entries chronologically.

7. **Hotel Room Availability Checker** 🏨
    - Checks if a hotel room is available for booking based on previous reservations.

## Output 📜

Each program processes date-time data and returns results in a structured format, such as:

-   Formatted `datetime` objects
-   Sorted lists of timestamps
-   Comparisons of time-based activities
-   Availability status for booking

## Usage 📦

1️⃣ Extract a date and time from a string:

```python
print(datetime_object)
```

2️⃣ Convert seconds to a `datetime` object:

```python
print(converted_datetime)
```

3️⃣ Analyze purchase times:

```python
print("Before Noon" if morning_purchases > afternoon_purchases else "Afternoon")
```

4️⃣ Sort `datetime` values:

```python
print(sorted_datetimes)
```

5️⃣ Identify the fastest student:

```python
print(f"Fastest student: {name}")
```

6️⃣ Sort and display an astronaut’s journal:

```python
print(sorted_journal)
```

7️⃣ Check hotel room availability:

```python
print(is_available_date(date_to_check))
```

## Conclusion 🚀

This lesson provides practical experience with Python's `datetime` module, covering everything from parsing dates to analyzing time-based data.
These skills are essential for working with timestamps, managing event schedules, and handling real-world time-related operations.
