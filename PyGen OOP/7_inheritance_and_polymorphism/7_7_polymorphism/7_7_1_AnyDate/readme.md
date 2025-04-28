# USADate and ItalianDate Class Implementation

## Description 📝

The provided code implements the `USADate` and `ItalianDate` classes to represent dates in American (MM-DD-YYYY) and Italian (DD/MM/YYYY) formats, respectively.
Both classes inherit from an abstract base class `AnyDate`, which centralizes shared logic for date storage and ISO formatting.
Each class accepts `year`, `month`, and `day` during instantiation and provides two methods: `format()` for the specific format and `iso_format()` for the ISO standard (YYYY-MM-DD).

## Purpose 🎯

Intended for applications requiring date representation in localized formats, such as internationalization, user interfaces, or data processing.
It’s also suitable for educational examples of inheritance, abstract base classes, and date handling in Python.

## Hierarchy Design 🛠️

-   **Why `AnyDate` as an Abstract Base Class?**:
    -   Centralizes common functionality: storing the date and implementing `iso_format`.
    -   Uses `ABC` to enforce that subclasses implement `format`, ensuring each defines its specific format.
    -   Reduces code duplication by handling date initialization and ISO formatting once.
-   **Inheritance Structure**:
    -   `USADate` inherits from `AnyDate`, implementing `format` for MM-DD-YYYY.
    -   `ItalianDate` inherits from `AnyDate`, implementing `format` for DD/MM/YYYY.
-   **Why Use `datetime.date`?**:
    -   Simplifies date storage and formatting using Python’s standard library.
    -   Provides reliable formatting via `strftime` and `isoformat`.
    -   No validation needed per requirements, but `date` ensures correct date creation.

## How It Works 🔍

-   **AnyDate (Abstract Base Class)**:
    -   Initializes with `year`, `month`, `day`, storing them as a `datetime.date` object (`self.date`).
    -   Defines `iso_format()`: Returns the date in YYYY-MM-DD format using `date.isoformat`.
    -   Declares abstract `format()` to be implemented by subclasses.
-   **USADate**:
    -   Inherits from `AnyDate`.
    -   Defines `DATE_FORMAT = "%m-%d-%Y"` (MM-DD-YYYY).
    -   Implements `format()`: Returns the date formatted with `strftime` using `DATE_FORMAT`.
-   **ItalianDate**:
    -   Inherits from `AnyDate`.
    -   Defines `DATE_FORMAT = "%d/%m/%Y"` (DD/MM/YYYY).
    -   Implements `format()`: Returns the date formatted with `strftime` using `DATE_FORMAT`.
-   **Behavior**:
    -   Both classes store a `date` object and provide:
        -   `format()`: Returns the date in the locale-specific format.
        -   `iso_format()`: Returns the date in YYYY-MM-DD (inherited from `AnyDate`).
    -   No validation is performed, as inputs are guaranteed correct.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   `USADate(2023, 5, 15)` creates a date for May 15, 2023.
    -   `ItalianDate(2023, 5, 15)` creates the same date.
-   **USADate Methods**:
    -   `USADate(2023, 5, 15).format()` → `"05-15-2023"`.
    -   `USADate(2023, 5, 15).iso_format()` → `"2023-05-15"`.
-   **ItalianDate Methods**:
    -   `ItalianDate(2023, 5, 15).format()` → `"15/05/2023"`.
    -   `ItalianDate(2023, 5, 15).iso_format()` → `"2023-05-15"`.
-   **Formatting**:
    -   Handles leading zeros correctly (e.g., `"05"` for month).
    -   Consistent with MM-DD-YYYY for USA and DD/MM/YYYY for Italy.
-   **Inheritance**:
    -   `issubclass(USADate, AnyDate)` → `True`.
    -   `issubclass(ItalianDate, AnyDate)` → `True`.
    -   `iso_format` inherited from `AnyDate`, reducing duplication.
-   **Correctness**:
    -   Uses `datetime.date` for reliable date handling.
    -   No validation needed per requirements.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `AnyDate` centralizes `date` storage and `iso_format`, ensuring consistency.
    -   `strftime` with `%m`, `%d`, `%Y` correctly formats dates with leading zeros.
    -   Abstract `format` ensures each subclass defines its format.
-   **Performance**:
    -   Initialization: O(1) for creating `date` object.
    -   `format`, `iso_format`: O(1) for string formatting.
    -   Highly efficient for date operations.
-   **Design**:
    -   `AnyDate` reduces duplication by sharing `iso_format` and date storage.
    -   Class-level `DATE_FORMAT` constants clarify format specifications.
    -   Type hints (`int`, `str`) enhance clarity.
    -   Simple and focused implementation using `datetime.date`.
-   **Alternatives**:
    -   Without `AnyDate`, `iso_format` and date storage would be duplicated.
    -   Manual string formatting (without `datetime`) is error-prone and unnecessary.
-   **Extensibility**:
    -   Easily extended for other date formats by adding new subclasses.
    -   Could add validation or additional methods if needed.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
usa_date = USADate(2023, 5, 15)
italian_date = ItalianDate(2023, 5, 15)

# Test USADate
print(usa_date.format())      # 05-15-2023
print(usa_date.iso_format())  # 2023-05-15

# Test ItalianDate
print(italian_date.format())      # 15/05/2023
print(italian_date.iso_format())  # 2023-05-15

# Test another date
usa_date2 = USADate(2023, 12, 1)
print(usa_date2.format())      # 12-01-2023
print(usa_date2.iso_format())  # 2023-12-01
```

## Conclusion 🚀

The `AnyDate`, `USADate`, and `ItalianDate` implementation is precise, providing date representations in American and Italian formats with a shared ISO format.
Using `AnyDate` as an abstract base class minimizes duplication, and `datetime.date` ensures reliable date handling.
It’s ideal for localized date formatting or teaching inheritance concepts, fully compliant with the task’s requirements.
