# Saturdays Between Two Dates

## Description 📝

The `saturdays_between_two_dates()` function calculates the number of Saturdays that fall between two given dates, inclusive.
The dates can be provided in any order, and the function will correctly count the Saturdays regardless.

## Purpose 🎯

This function is useful for determining the number of Saturdays within a specific date range.
It could be applied in various scenarios, such as scheduling events on Saturdays or counting weekend days for planning purposes.

## How It Works 🔍

1. The function first converts the start and end dates into their respective ordinal values, ensuring the range is processed from the earlier date to the later date.
2. The function iterates through all dates within the specified range.
3. For each date, it checks whether the date is a Saturday.
4. It increments the count each time a Saturday is encountered.

## Output 📜

Example output when running the function:

```python
2  # January 4, 2020 and January 11, 2020
```

## Usage 📦

1. Provide two `date` objects representing the start and end dates.
2. Call the `saturdays_between_two_dates()` function with the provided dates.
3. The function returns an integer representing the count of Saturdays between the start and end dates, inclusive.

## Conclusion 🚀

The `saturdays_between_two_dates()` function provides a simple way to count how many Saturdays occur within a specified range of dates.
This can be useful for various scheduling and planning tasks.
