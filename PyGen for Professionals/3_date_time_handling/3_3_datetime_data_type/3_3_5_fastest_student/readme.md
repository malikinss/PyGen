# Fastest Student Finder 🏆

## Description 📝

This program determines which student solved their math homework the fastest based on recorded start and end times.

## Purpose 🎯

The goal of the program is to analyze time data and identify the student who completed their homework in the shortest amount of time.

## How It Works 🔍

1. A dictionary of students is provided, where each key is a student's name and the value is a tuple with two timestamps (`start_time` and `end_time`).
2. The program converts the timestamps from the format `'DD.MM.YYYY HH:MM:SS'` into `datetime` objects.
3. It calculates the total time spent solving the homework for each student.
4. The student who spent the least time is identified.
5. The program prints the name of the fastest student.

## Output 📜

The program outputs the name of the student who completed their homework in the shortest amount of time.

### Example Output:

```plaintext
Егор
```

(If `Егор` was the fastest student based on the given data.)

## Usage 📦

1. Prepare a dictionary where:
    - The keys are student names.
    - The values are tuples containing start and end times in the format `'DD.MM.YYYY HH:MM:SS'`.
2. Call `fastest_student(data)`, passing the dictionary as an argument.
3. The function will return the name of the fastest student.

## Conclusion 🚀

This program helps in identifying students who solve problems efficiently.
It can be useful for competitions, time management analysis, or performance tracking.
