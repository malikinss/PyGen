Lesson 8.2: enumerations, class Enum

Enumerations
Creating enumerations
Enumeration capabilities
Abstract. The lesson is devoted to enumerations in Python.

https://stepik.org/lesson/794703/step/1?unit=797455

This lesson has good theory explonation, has 3 programing practical tasks and 21 theoretical questions presented on the website.

1. 8_2_1_HTTPStatusCodes

```
# HTTPStatusCodes Enum Implementation

## Description 📝

The provided code implements the `HTTPStatusCodes` class as a Python enumeration using `enum.Enum`.
It defines five HTTP status codes (`CONTINUE`, `OK`, `USE_PROXY`, `NOT_FOUND`, `BAD_GATEWAY`) with their respective values (100, 200, 305, 404, 502).
Each enum element supports two methods: `info()` to return the element’s name and value as a tuple, and `code_class()` to return the Russian name of the status code’s group (e.g., информация, успех).

## Purpose 🎯

Intended for applications involving HTTP request handling, such as web servers, APIs, or educational examples of Python enumerations, status code management, and method implementation on enum elements.
```

2. 8_2_2_Seasons

```
# Seasons Enum Implementation

## Description 📝

The provided code implements the `Seasons` class as a Python enumeration using `enum.Enum`.
It defines four seasons (`WINTER`, `SPRING`, `SUMMER`, `FALL`) with values 1, 2, 3, and 4, respectively.
Each enum element supports a `text_value` method that returns the season’s name in English (`en`) or Russian (`ru`), with specific translations for each season.

## Purpose 🎯

Intended for applications requiring localized season names, such as calendars, weather apps, or educational examples of Python enumerations, method implementation on enum elements, and internationalization.
```

3. 8_2_3_NextDate

```
# Weekday and NextDate Class Implementation

## Description 📝

The provided code implements the `Weekday` class as a Python enumeration using `enum.Enum` to represent days of the week, and the `NextDate` class to determine the next date corresponding to a specified weekday relative to a given date.
The `Weekday` enum defines seven days with values 0–6.
The `NextDate` class takes a current date, a target weekday, and a boolean flag to consider the current date, providing methods to return the next matching date and the number of days until it.

## Purpose 🎯

Intended for scheduling applications, such as calendar systems, event planning, or educational examples of Python enumerations, date manipulation, and modular arithmetic for weekday calculations.
```
