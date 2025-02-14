# Date Range Filter Program 📅

## Description 📝

This program receives two dates as input, representing the left and right boundaries of a range. The program will then print every third date in the range starting from the first date where the sum of the day and month is odd, provided the date is not a Monday or Thursday.

The output dates are printed in the format `DD.MM.YYYY` and must meet the conditions:

-   The sum of the day and month is odd.
-   The date is not a Monday or Thursday.

## Purpose 🎯

The purpose of this program is to filter a date range based on specific conditions, ensuring that the output only includes dates that:

1. Start from a date where the sum of the day and month is odd.
2. Skip Mondays and Thursdays.
3. Display every third valid date from the range.

## How It Works 🔍

1. The user inputs two dates in the format `DD.MM.YYYY` (the start and end of the range).
2. The program finds the first date where the sum of the day and month is odd.
3. Starting from that date, it checks every third date in the range.
4. It outputs the date if it's neither Monday nor Thursday.

### Example:

```python
# Running the program will ask for input:
start_date = input()  # Enter the start date
end_date = input()    # Enter the end date
display_valid_dates()  # The program displays valid dates
```

## Output 📜

The program will print each valid date on a new line in the format `DD.MM.YYYY`.

### Example output:

```
15.05.2023
18.05.2023
21.05.2023
```

If no dates match the criteria, nothing will be printed.

## Usage 📦

1. The user enters the start and end date in the format `DD.MM.YYYY`.
2. The program calculates every third valid date where the sum of the day and month is odd and the date is not Monday or Thursday.
3. The program outputs the filtered dates or nothing if no valid dates are found.

## Conclusion 🚀

This program helps filter and display dates from a given range based on a specific set of conditions, making it useful for time-related calculations or event scheduling.
