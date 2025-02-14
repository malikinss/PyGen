# Math Tutor Class Schedule 🗓️

## Description 📝

This program helps a math tutor generate a class schedule for a working day.
Each lesson lasts 45 minutes, followed by a 10-minute break.
The tutor inputs the start and end times of their working day, and the program generates a list of class schedules.
If the working day is too short for a full lesson, it will notify the tutor.

## Purpose 🎯

The purpose of this program is to automate the process of generating a class schedule for a tutor, ensuring that lessons are arranged in a way that includes breaks and respects the workday boundaries.

## How It Works 🔍

1. The user inputs the start and end times of the working day in the "HH:MM" format.
2. The program calculates the number of lessons that can fit in the given timeframe, considering a 45-minute lesson and a 10-minute break after each.
3. The schedule is displayed with the start and end times of each lesson in the "HH:MM - HH:MM" format.
4. If the workday is too short for at least one lesson, a message will be shown instead of the schedule.

### Example:

```python
# Example:
# Start time: 09:00
# End time: 12:00
# Output will show lessons from 09:00 - 09:45, 09:55 - 10:40, and so on
```

## Output 📜

The program will output the class schedule in the format `HH:MM - HH:MM`.

### Example output:

```
Class schedule:
09:00 - 09:45
09:55 - 10:40
10:50 - 11:35
11:45 - 12:30
```

If the workday is too short for even a single lesson:

```
The workday is too short for even a single lesson.
```

## Usage 📦

1. Run the program and input the start and end times of the workday.
2. The program will display a list of lessons, or notify you if there is not enough time for even one lesson.

## Conclusion 🚀

This program provides a simple and effective way for math tutors to plan their lesson schedules, ensuring that lessons are appropriately spaced and fall within the available workday hours.
