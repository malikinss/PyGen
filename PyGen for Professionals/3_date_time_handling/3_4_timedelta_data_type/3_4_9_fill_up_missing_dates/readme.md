# Missing Date Filler 📅

## Description 📝

This program takes a list of dates in the "DD.MM.YYYY" format, sorts them, and fills in any missing dates between them.
The program returns a list containing all the dates in ascending order, including the dates that were missing in between.

## Purpose 🎯

The purpose of this program is to identify gaps between dates and return a complete list of all dates in the range, including the missing ones.
It handles unordered input and ensures that the dates are returned in the correct sequence.

## How It Works 🔍

1. The user provides a list of dates in the "DD.MM.YYYY" format.
2. The program sorts the list of dates in ascending order.
3. It identifies the range of dates between the earliest and latest dates in the list.
4. It fills in any missing dates within that range.
5. The program returns the complete list of dates in the correct order.

### Example:

```python
dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
filled_dates = fill_up_missing_dates(dates)
print(filled_dates)
```

## Output 📜

The program will output a list of dates, including the missing ones, sorted in ascending order.

### Example output:

```
['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021', '08.11.2021', '09.11.2021', '10.11.2021', '11.11.2021', '12.11.2021', '13.11.2021', '14.11.2021', '15.11.2021']
```

## Usage 📦

1. Input a list of dates in the "DD.MM.YYYY" format.
2. The program will display a list of all dates in the range, including any missing ones.

## Conclusion 🚀

This program ensures that any gaps between dates in a sequence are filled, providing a complete list of dates in the specified range.
