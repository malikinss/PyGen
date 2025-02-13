# Seconds and Datetime Converter Program

## Description 📝

This program converts between seconds (elapsed since the epoch) and `datetime` objects.
It provides two functions:

-   Convert seconds (elapsed since January 1, 1970) to a `datetime` object.
-   Convert a `datetime` object to the number of seconds elapsed since the epoch.

## Purpose 🎯

The program is useful for performing conversions between time represented in seconds and more human-readable `datetime` objects.
It helps in handling timestamps and time calculations in software applications that need to work with different time representations.

## How It Works 🔍

1. The `convert_seconds_to_datetime()` function takes a number of seconds as input and converts it into a `datetime` object using `fromtimestamp()`.
2. The `convert_datetime_to_seconds()` function converts a given `datetime` object to the number of seconds that have elapsed since the Unix epoch using `timestamp()`.

## Output 📜

The program outputs:

-   The corresponding `datetime` object when converting seconds to `datetime`.
-   The number of seconds since the epoch when converting a `datetime` object to seconds.

### Example Usage:

```plaintext
Input:
Seconds: 2483228800
Datetime: 2011-11-04 00:00:00

Output:
Converted datetime: 2011-11-04 00:00:00
Converted seconds: 2483228800
```

## Usage 📦

1. To convert seconds to a `datetime` object, call the function `convert_seconds_to_datetime(seconds)`.
2. To convert a `datetime` object to seconds, call the function `convert_datetime_to_seconds(dt)`.

## Conclusion 🚀

This program is a simple tool for converting between time in seconds and `datetime` objects, which is useful when dealing with timestamps, time-related data manipulation, and applications that need to convert between different time representations.
