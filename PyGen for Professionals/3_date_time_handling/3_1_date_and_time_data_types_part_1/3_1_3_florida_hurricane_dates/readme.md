# Count Early Hurricanes in Florida

## Description 📝

The `count_early_hurricanes()` function counts the number of hurricanes that hit Florida before the official start of the Atlantic hurricane season, which begins on June 1st.

## Purpose 🎯

This function is designed to:

-   Track hurricanes that hit Florida before the start of the Atlantic hurricane season, based on a list of hurricane dates.

## How It Works 🔍

1. The function takes a list of hurricane dates as input.
2. It iterates through each date, checking if the month is less than 6 (before June).
3. The counter `early_hurricanes` is incremented each time a hurricane occurred before June.

## Output 📜

Example output when running the function:

```python
hurricane_dates = [
    date(1950, 5, 30),
    date(1955, 6, 10),
    date(1960, 4, 25),
]

early_hurricanes_count = count_early_hurricanes(hurricane_dates)
print(early_hurricanes_count)
# Output: 2
```

## Usage 📦

1. Define a list of hurricane dates in the form of `date` objects.
2. Call the `count_early_hurricanes()` function with the list of dates.
3. The function returns the number of hurricanes that occurred before June.

Example usage:

```python
from datetime import date

def count_early_hurricanes(hurricane_dates: list) -> int:
    early_hurricanes = 0
    for hurricane in hurricane_dates:
        if hurricane.month < 6:
            early_hurricanes += 1
    return early_hurricanes

# Example list of hurricane dates
hurricane_dates = [
    date(1950, 5, 30),
    date(1955, 6, 10),
    date(1960, 4, 25),
]

# Count early hurricanes
early_hurricanes_count = count_early_hurricanes(hurricane_dates)
print(early_hurricanes_count)  # Output: 2
```

## Conclusion 🚀

This function is helpful for analyzing historical hurricane data and identifying trends related to the timing of hurricanes in the Atlantic hurricane season.
