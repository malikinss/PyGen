# Get Third Thursday of Each Month

## Description 📝

This Python program calculates the third Thursday of each month for a given year.
This is specifically useful for identifying free days at museums, such as the Hermitage, which offer free entry on the third Thursday of every month.

## Purpose 🎯

The program helps to find all the third Thursdays in a given year, allowing users to plan visits or events that align with these free entry days.

## How It Works 🔍

1. **Function `filter_dates_by_weekday_in_month(year, month, target_weekday)`**:

    - This function generates all dates in the specified month and filters those that fall on the target weekday (in this case, Thursday).

2. **Function `get_third_thursday_per_month(year, month_name)`**:

    - It calls `filter_dates_by_weekday_in_month()` to get all Thursdays in the given month, and then it returns the third Thursday from the list.

3. **Function `get_all_third_thursdays(year)`**:
    - This function iterates over all months of the year, calling `get_third_thursday_per_month()` to get the third Thursday for each month. The results are formatted in 'DD.MM.YYYY' format.

### Example:

For input:

```python
get_all_third_thursdays(2021)
```

The output will be:

```python
21.01.2021
18.02.2021
18.03.2021
15.04.2021
20.05.2021
17.06.2021
15.07.2021
19.08.2021
16.09.2021
21.10.2021
18.11.2021
16.12.2021
```

## Output 📜

The function returns a list of the third Thursdays of each month in the specified year, formatted as `DD.MM.YYYY`.

Example output:

```python
21.01.2021
18.02.2021
18.03.2021
15.04.2021
20.05.2021
17.06.2021
15.07.2021
19.08.2021
16.09.2021
21.10.2021
18.11.2021
16.12.2021
```

## Usage 📦

1. Save the code in a file named `get_third_thursday.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script or import the `get_all_third_thursdays()` function into another Python script to use.

### Example usage:

```python
from get_third_thursday import get_all_third_thursdays

free_days = get_all_third_thursdays(2024)
for day in free_days:
    print(day)
```

## Conclusion 🚀

This program is a useful tool for determining free museum days that occur on the third Thursday of each month.
It can be particularly beneficial for planning visits to museums like the Hermitage, where entry is free on these days. 🏛️
