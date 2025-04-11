# DateFormatter Class Regional Converter

## Description 📝

The `DateFormatter` class creates callable instances that format `date` objects into strings based on a country-specific format, determined by a `country_code` provided during instantiation.
It supports formats for countries like `ru` (DD.MM.YYYY), `us` (MM-DD-YYYY), and others from a predefined table.

## Purpose 🎯

This class is designed for date localization, suitable for internationalization, educational examples of callable objects, or applications needing region-specific date displays.

## How It Works 🔍

-   **Initialization**: Stores the `country_code` and selects the corresponding format string from `_FORMATS` (e.g., `%d.%m.%Y` for `ru`).
-   **`__call__`()**: Makes instances callable, formatting the input `date` object using `strftime` with the stored format.

## Usage 📦

1. Save the class in a Python file, e.g., `date_formatter.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from date_formatter import DateFormatter
from datetime import date
ru_format = DateFormatter('ru')
us_format = DateFormatter('us')
d = date(2023, 12, 25)
print(ru_format(d))  # 25.12.2023
print(us_format(d))  # 12-25-2023
ca_format = DateFormatter('ca')
print(ca_format(d))  # 2023-12-25
```

## Conclusion 🚀

The `DateFormatter` class offers a clean and reusable way to format dates in Python according to various country standards, leveraging `strftime` for accuracy.
Its design is straightforward and can be extended with more country codes or custom formats for broader localization needs.
