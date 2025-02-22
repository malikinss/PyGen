# Timur's Meeting Scheduler 📝

## Description 📝

This program processes a CSV file containing Timur's meeting details with his friends, which includes their surnames, first names, meeting dates, and meeting times.
The program reads the CSV data, sorts the meetings by date and time from the earliest to the latest, and then prints the full names of his friends (surname and first name) in sorted order.

## Purpose 🎯

The program performs the following tasks:

-   Reads meeting data from a CSV file.
-   Converts the meeting date and time into a `datetime` object for sorting.
-   Sorts the meetings by date and time from earliest to latest.
-   Displays the full names of the friends in sorted order.

### Example Input (meetings.csv)

```csv
surname,name,meeting_date,meeting_time
Kharisov,Artur,15.07.2022,05:00 PM
Geor,Gagiev,14.12.2022,06:00 PM
Gudtsev,Taimuraz,12.05.2023,08:00 AM
Baziyev,German,20.07.2023,04:00 PM
```

### Example Output

```
Gudtsev Taimuraz
Kharisov Artur
Baziyev German
Geor Gagiev
```

## Output 📜

The program prints the full names of Timur's friends sorted by the meeting date and time, in the format:

-   `<surname> <name>`

Each full name is printed on a new line.

## Usage 📦

To use the program:

1. Ensure that you have a valid CSV file named `meetings.csv` with the correct format.
2. Run the script, which will read and process the data from the CSV file, then display the sorted meeting information.

### Example:

```bash
$ python timur_meeting_scheduler.py
```

### Expected Output (based on the example input)

```
Gudtsev Taimuraz
Kharisov Artur
Baziyev German
Geor Gagiev
```

## Conclusion 🚀

This program efficiently handles the task of sorting and displaying meeting details from a CSV file, ensuring that Timur's meetings are organized by date and time.
