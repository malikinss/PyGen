# Store Closing Time Calculator 🕒

## Description 📝

This program takes the current date and time as input and calculates how many minutes remain until the store closes.
If the store is closed, it will display a message indicating that.

## Purpose 🎯

The purpose of this program is to provide the number of minutes left until the store's closing time based on the current time, considering the store's operating hours.
If the store is closed, it will notify the user.

## How It Works 🔍

1. The user enters the current date and time in the format `DD.MM.YYYY HH:MM`.
2. The program checks the store's operating hours for that specific day of the week.
3. If the store is open, it calculates how many minutes remain until the closing time.
4. If the store is closed (either outside operating hours or on a day the store is closed), it prints "The store is closed".

### Example:

```python
# Running the program will ask for input:
datetime_string = input()
display_minutes_until_closing(datetime_string)
```

## Output 📜

-   If the store is open: It will print the number of minutes until closing.
-   If the store is closed: It will print "The store is closed".

### Example output:

```
45
```

or:

```
The store is closed
```

## Usage 📦

1. The user inputs the current date and time in the format `DD.MM.YYYY HH:MM`.
2. The program then calculates and prints the number of minutes left until the store closes.
3. If the store is closed, a message "The store is closed" will be printed instead.

## Conclusion 🚀

This program helps determine how much time is left before the store closes, providing real-time information for the user based on current time and the store's operating hours.
