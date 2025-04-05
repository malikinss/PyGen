# BirthInfo Class Age Calculator

## Description 📝

The `BirthInfo` class encapsulates a birth date, accepting it as a `date` object, ISO string, or list/tuple of integers, and stores it as a `date` object.
It provides a read-only `age` property to compute the current age in years, raising a `TypeError` for unsupported input types or invalid dates.

## Purpose 🎯

This class is designed for managing birth date data and calculating age, ideal for personal record systems, educational examples of type dispatching, or applications needing precise age computation.

## How It Works 🔍

-   **Initialization**: Uses `@singledispatchmethod` with `__init__` to handle different input types:
    -   **\_from_date()**: Sets `birth_date` directly from a `date` object.
    -   **\_from_iso()**: Parses an ISO string (e.g., '2023-02-26') into `birth_date`, raising `TypeError` if invalid.
    -   **\_from_list_or_tuple()**: Converts a 3-element sequence (year, month, day) into `birth_date`, raising `TypeError` if invalid.
    -   Base `__init__`: Raises `TypeError` for unsupported types.
-   **age Property**: Calculates full years between `birth_date` and today using `relativedelta` from `dateutil`.
-   **Error Handling**: Centralized `ERR_MSG` ensures consistent error messaging.

## Usage 📦

1. Save the class in a Python file, e.g., `birth_info.py`.
2. Install `python-dateutil` if needed (`pip install python-dateutil`).
3. Open a terminal and navigate to the directory where the file is saved.
4. Run Python and test the class:

```python
from birth_info import BirthInfo
from datetime import date
birth1 = BirthInfo(date(2023, 2, 26))
birth2 = BirthInfo("2020-05-15")
birth3 = BirthInfo([1990, 12, 31])
print(f"Age 1: {birth1.age}")
print(f"Age 2: {birth2.age}")
print(f"Age 3: {birth3.age}")
```

## Conclusion 🚀

The `BirthInfo` class provides a robust and flexible way to handle birth dates and calculate ages in Python, leveraging single dispatch for type versatility.
Its precise age computation and error handling make it a reliable tool, easily extensible with features like date formatting or additional age-related metrics.
