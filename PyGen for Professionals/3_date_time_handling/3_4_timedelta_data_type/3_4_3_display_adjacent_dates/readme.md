# Get Adjacent Dates 📅

## Description 📝

This program takes a date as input and returns the previous and next dates in the format "DD.MM.YYYY".

## Purpose 🎯

The goal of this program is to calculate and display the previous and next dates for a given date, helping to easily find neighboring dates.

## How It Works 🔍

1. The user provides a date string in the format "DD.MM.YYYY".
2. The program converts the input date string into a `datetime` object.
3. It then calculates the previous and next dates using the `timedelta` class.
4. Finally, the program outputs the previous and next dates in the same "DD.MM.YYYY" format.

### Example:

```python
Please input date in format DD.MM.YYYY: 04.11.2021
03.11.2021
05.11.2021
```

## Output 📜

The program outputs two lines:

-   The first line shows the previous date.
-   The second line shows the next date.

## Usage 📦

1. Run the program.
2. Enter a date in the format "DD.MM.YYYY".
3. The program will display the previous and next dates for the entered date.

## Conclusion 🚀

This program is useful for quickly finding adjacent dates and is flexible enough to handle any valid date input.
