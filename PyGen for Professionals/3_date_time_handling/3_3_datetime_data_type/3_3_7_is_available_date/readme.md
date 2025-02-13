# Hotel Room Availability Checker 🏨

## Description 📝

This function checks whether a specific date or date range is available for booking in a hotel based on already booked dates.

## Purpose 🎯

The goal of this function is to help hotel staff quickly determine if a room can be booked for a given date or period.

## How It Works 🔍

1. The function accepts:
    - `booked_dates`: A list of booked dates or date ranges (e.g., `['04.11.2021', '05.11.2021-09.11.2021']`).
    - `date_for_booking`: A single date or a date range (e.g., `'01.11.2021'` or `'01.11.2021-04.11.2021'`).
2. It converts all dates to `datetime` objects for comparison.
3. Date ranges are expanded into individual dates.
4. The function checks if any requested date overlaps with already booked dates.
5. If there is an overlap, it returns `False` (not available); otherwise, it returns `True` (available).

## Output 📜

The function returns:

-   `True` if the requested date or range is fully available.
-   `False` if any of the requested dates overlap with booked dates.

### Example:

```python
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '11.11.2021-15.11.2021'

print(is_available_date(dates, some_date))  # Output: True
```

## Usage 📦

1. Prepare a list of booked dates in `DD.MM.YYYY` format.
2. Pass the booked dates and the date for booking to the function.
3. Check the boolean output to determine availability.

## Conclusion 🚀

This function simplifies hotel room availability checks by efficiently handling individual dates and date ranges.
