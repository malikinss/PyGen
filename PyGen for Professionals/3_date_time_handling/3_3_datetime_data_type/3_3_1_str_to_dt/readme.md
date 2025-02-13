# Date and Time Extractor Program

## Description 📝

This program extracts a date and time from a given text string.
The date is in the format `DD.MM.YYYY`, and the time is in the format `HH:MM`.
It then converts the extracted date and time into a `datetime` object.

## Purpose 🎯

The program is designed to extract date and time from a string and convert it into a `datetime` object that can be used for further processing.
This is useful when working with text data that contains specific date and time information.

## How It Works 🔍

1. The program receives a string that contains a date in the format `DD.MM.YYYY` and a time in the format `HH:MM`.
2. It splits the input text to isolate the date and time part.
3. The program then combines the extracted date and time into one string.
4. Finally, the combined string is converted into a `datetime` object using Python's `strptime()` function.

## Output 📜

The program outputs a `datetime` object representing the extracted date and time.

### Example Usage:

```plaintext
Input:
'Dear patient, the doctor is ready to see you on 15.07.2022 at 08:30'

Output:
2022-07-15 08:30:00
```

## Usage 📦

1. Pass the text string containing the date and time in the specified format to the function `extract_datetime_from_text()`.
2. The function will return a `datetime` object representing the extracted date and time.

## Conclusion 🚀

This program is a simple tool for extracting date and time from a given text string and converting it into a `datetime` object. It is useful for text parsing and handling date/time data in various formats.
