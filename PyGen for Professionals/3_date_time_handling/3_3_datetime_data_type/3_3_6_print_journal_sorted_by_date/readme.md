# Astronaut's Diary Sorter 🚀

## Description 📝

This program reads an astronaut's diary from a text file (`diary.txt`), where daily reports are written with timestamps in various positions.
It then organizes the records in chronological order and displays them.

## Purpose 🎯

The goal of this program is to structure and present the astronaut's journal entries in a readable and time-ordered format.

## How It Works 🔍

1. The program reads the file `diary.txt`, where entries are separated by blank lines.
2. Each entry starts with a timestamp in the format:
    ```plaintext
    DD.MM.YYYY; HH:MM
    ```
3. It validates and converts each timestamp into a `datetime` object.
4. The program organizes all entries by their corresponding timestamps.
5. It prints the entries in chronological order.

## Output 📜

The program outputs the sorted journal entries in the following format:

```plaintext
01.11.2021; 08:45
Woke up and checked the oxygen levels.
Conducted a brief systems check.

01.11.2021; 12:30
Completed the scheduled maintenance for the solar panels.
Communicated with mission control about the progress.

02.11.2021; 06:15
Observed an unidentified flying object in the distance.
...
```

## Usage 📦

1. Ensure that `diary.txt` contains properly formatted entries.
2. Run the script to process and sort the diary records.
3. The sorted journal entries will be displayed in the console.

## Conclusion 🚀

This program helps structure scattered log entries into a readable and time-ordered format, making it easier to analyze and review the astronaut's activities.
