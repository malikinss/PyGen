Lesson 7.7: polymorphism

The concept of polymorphism
Polymorphism of operators
Polymorphism of functions
Polymorphism in class methods
Abstract. The lesson is devoted to polymorphism in Python.

https://stepik.org/lesson/872533/step/1?unit=876917

This lesson has good theory explonation, has 3 programing practical tasks and 9 theoretical questions presented on the website.

1. 7_7_1_AnyDate

```
# USADate and ItalianDate Class Implementation

## Description 📝

The provided code implements the `USADate` and `ItalianDate` classes to represent dates in American (MM-DD-YYYY) and Italian (DD/MM/YYYY) formats, respectively.
Both classes inherit from an abstract base class `AnyDate`, which centralizes shared logic for date storage and ISO formatting.
Each class accepts `year`, `month`, and `day` during instantiation and provides two methods: `format()` for the specific format and `iso_format()` for the ISO standard (YYYY-MM-DD).

## Purpose 🎯

Intended for applications requiring date representation in localized formats, such as internationalization, user interfaces, or data processing.
It’s also suitable for educational examples of inheritance, abstract base classes, and date handling in Python.
```

2. 7_7_2_Stat

```
# MinStat, MaxStat, and AverageStat Class Implementation

## Description 📝

The provided code implements the `MinStat`, `MaxStat`, and `AverageStat` classes to compute the minimum, maximum, and average of a set of numbers, respectively.
All classes inherit from an abstract base class `Stat`, which centralizes shared logic for storing numbers and implementing common methods (`add`, `clear`, and a generic `result`).
Each class accepts an optional iterable of numbers during instantiation and provides methods to add numbers, compute the statistic, and clear the set.

## Purpose 🎯

Intended for applications requiring simple statistical computations on dynamic sets of numbers, such as data analysis, real-time monitoring, or educational examples of inheritance and abstract base classes in Python.
```

3.

```

```
