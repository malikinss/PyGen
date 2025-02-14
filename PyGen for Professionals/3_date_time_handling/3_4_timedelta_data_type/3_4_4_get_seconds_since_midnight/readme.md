# Get Seconds Since Midnight ⏰

## Description 📝

This program takes a time as input and calculates the number of seconds that have passed since midnight (00:00:00).

## Purpose 🎯

The goal of this program is to convert a given time (in "HH:MM:SS" format) into the total number of seconds that have passed since the beginning of the day.

## How It Works 🔍

1. The user provides a time string in the format "HH:MM:SS".
2. The program parses the input string into a `datetime` object.
3. It then calculates the total number of seconds by multiplying the number of hours by 3600 (seconds in an hour), minutes by 60, and adding the number of seconds.
4. The program then outputs the total number of seconds since midnight.

### Example:

```python
Please input the time in the format HH:MM:SS: 12:30:45
45045
```

## Output 📜

The program outputs a single integer representing the number of seconds since midnight (00:00:00).

## Usage 📦

1. Run the program.
2. Enter a time in the format "HH:MM:SS".
3. The program will display the number of seconds that have passed since midnight for the entered time.

## Conclusion 🚀

This program is useful for converting time into a measurable unit (seconds), allowing for easy calculations or time-related analysis.
