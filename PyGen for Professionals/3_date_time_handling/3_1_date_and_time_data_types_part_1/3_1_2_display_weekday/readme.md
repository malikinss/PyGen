# Day of the Week for Hurricane Andrew's Landfall

## Description 📝

The `get_day_of_week_for_hurricane()` function calculates the day of the week on which Hurricane Andrew made landfall.
It returns the weekday as an integer, where 0 represents Monday, and 6 represents Sunday.

## Purpose 🎯

This function is designed to:

-   Determine the exact day of the week for significant historical events, such as Hurricane Andrew's landfall.

## How It Works 🔍

1. The function takes the date of an event (year, month, day) as input.
2. It uses Python's `datetime.date()` method to create a `date` object representing the hurricane's landfall.
3. The `weekday()` method is called on the `date` object to get the day of the week, which is returned as an integer.

## Output 📜

Example output when running the function:

```python
hurricane_andrew_landfall = get_day_of_week_for_hurricane(1992, 8, 24)
print(hurricane_andrew_landfall)
# Output: 0
```

## Usage 📦

1. Call the `get_day_of_week_for_hurricane()` function with the date of an event.
2. The function returns the corresponding weekday as an integer (0 = Monday, 6 = Sunday).

Example usage:

```python
from datetime import date

def get_day_of_week_for_hurricane(year: int, month: int, day: int) -> int:
    hurricane_date = date(year, month, day)
    return hurricane_date.weekday()

hurricane_andrew_landfall = get_day_of_week_for_hurricane(1992, 8, 24)
print(hurricane_andrew_landfall)
```

## Conclusion 🚀

This function is a simple but useful tool for determining the weekday of historical events, which can be helpful for data analysis or for general historical knowledge.
