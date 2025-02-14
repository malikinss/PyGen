# Days Between Dates 📅

## Description 📝

This function calculates the absolute number of days between two `date` objects.

## Purpose 🎯

The purpose of this function is to determine the difference in days between two given dates, regardless of which date is earlier.

## How It Works 🔍

1. The function takes two `date` objects as arguments: the start date and the end date.
2. It calculates the absolute difference in days using subtraction (`start_date - end_date`).
3. The result is returned as an integer representing the number of days.

### Example:

```python
from datetime import date

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)
print(days_between_dates(today, birthday))  # Output: 336
```

## Output 📜

The function returns the absolute number of days between the two dates as an integer.

## Usage 📦

1. Create two `date` objects, one for the start date and one for the end date.
2. Call the function with these two dates as arguments.
3. The function will return the number of days between the two dates.

## Conclusion 🚀

This function is useful for calculating the number of days between two dates, such as determining how many days are left until a special event or birthday.
