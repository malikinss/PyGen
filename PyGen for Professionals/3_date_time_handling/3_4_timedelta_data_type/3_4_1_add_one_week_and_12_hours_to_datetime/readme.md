# Add Time to Datetime ⏳

## Description 📝

This function adds a specified number of weeks and hours to a given `datetime` object and returns the updated result as a formatted string.

## Purpose 🎯

The purpose of this function is to easily modify a `datetime` object by adding a set number of weeks and hours, then format the result for display.

## How It Works 🔍

1. The function takes a `datetime` object and two optional arguments: the number of weeks and hours to add.
2. It uses the `timedelta` class to perform the addition of weeks and hours.
3. The updated `datetime` is then formatted into the string format `DD.MM.YYYY HH:MM:SS`.
4. The formatted string is returned.

### Example:

```python
from datetime import datetime

dt = datetime(2021, 11, 4, 13, 6)
print(add_time_to_datetime(dt))  # Output: '11.11.2021 01:06:00'
```

## Output 📜

The function returns the updated `datetime` object in the format:

-   `'DD.MM.YYYY HH:MM:SS'`

## Usage 📦

1. Create a `datetime` object with the desired date and time.
2. Optionally, specify the number of weeks and hours to add (defaults are 1 week and 12 hours).
3. Call the function and display the result.

## Conclusion 🚀

This function is a convenient way to manipulate `datetime` objects by adding time and returning it in a readable format.
