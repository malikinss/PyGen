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
The provided code implements the `USADate` and `ItalianDate` classes to represent dates in American (MM-DD-YYYY) and Italian (DD/MM/YYYY) formats, respectively.
Both classes inherit from an abstract base class `AnyDate`, which centralizes shared logic for date storage and ISO formatting.
Each class accepts `year`, `month`, and `day` during instantiation and provides two methods: `format()` for the specific format and `iso_format()` for the ISO standard (YYYY-MM-DD).
Intended for applications requiring date representation in localized formats, such as internationalization, user interfaces, or data processing.
It’s also suitable for educational examples of inheritance, abstract base classes, and date handling in Python.
```

2. 7_7_2_Stat

```
# MinStat, MaxStat, and AverageStat Class Implementation
The provided code implements the `MinStat`, `MaxStat`, and `AverageStat` classes to compute the minimum, maximum, and average of a set of numbers, respectively.
All classes inherit from an abstract base class `Stat`, which centralizes shared logic for storing numbers and implementing common methods (`add`, `clear`, and a generic `result`).
Each class accepts an optional iterable of numbers during instantiation and provides methods to add numbers, compute the statistic, and clear the set.
Intended for applications requiring simple statistical computations on dynamic sets of numbers, such as data analysis, real-time monitoring, or educational examples of inheritance and abstract base classes in Python.
```

3. 7_7_3_Paragraph

```
# LeftParagraph and RightParagraph Class Implementation
The provided code implements the `LeftParagraph` and `RightParagraph` classes to format paragraphs aligned to the left and right, respectively.
Both classes inherit from an abstract base class `Paragraph`, which centralizes shared logic for managing lines, adding words, and handling line length constraints.
Each class accepts a `length` parameter during instantiation and provides `add` to append words and `end` to print and clear the paragraph.
Intended for text formatting applications, such as document processing, typesetting, or console-based text alignment.
It’s also suitable for educational examples of inheritance, abstract base classes, and text manipulation in Python.
```
