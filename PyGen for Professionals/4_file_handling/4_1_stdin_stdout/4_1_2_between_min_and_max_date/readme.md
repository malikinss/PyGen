# Calculate Days Between Max and Min Dates

## Description 📝

This Python program reads a sequence of dates in ISO format (YYYY-MM-DD) from the user, finds the earliest (minimum) and latest (maximum) date, and calculates the number of days between them.

## Purpose 🎯

The program helps in finding the time difference between the earliest and latest dates in a sequence of dates provided by the user.
This is useful for analyzing time periods and calculating the difference between two significant dates.

## How It Works 🔍

1. **Function `parse_iso_date(date_string)`**:

    - Converts a string in ISO format (YYYY-MM-DD) to a `datetime.date` object for easy comparison.

2. **Function `get_dates_from_input()`**:

    - Reads the sequence of dates from the user input, strips any extra spaces, and converts them to date objects.

3. **Function `calculate_difference_between_min_and_max_dates(dates)`**:
    - Takes the list of dates and finds the minimum and maximum date using Python's built-in `min()` and `max()` functions.
    - Returns the difference in days between the two dates using the subtraction operation on `datetime.date` objects.

### Example:

For input:

```
2021-01-01
2020-05-05
2022-12-31
```

The program will output:

```
637
```

This is the number of days between `2020-05-05` and `2022-12-31`.

## Output 📜

The program outputs the number of days between the minimum and maximum dates from the provided input.

Example output:

```
637
```

## Usage 📦

1. Save the code in a file named `date_diff.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script.

### Example usage:

```bash
$ python date_diff.py
2021-01-01
2020-05-05
2022-12-31
```

The output will be:

```
637
```

## Conclusion 🚀

This program calculates the number of days between the earliest and latest dates from a sequence provided by the user.
It provides an easy and efficient way to calculate time differences for date-related tasks.
