# Date Formatter Function

## Description 📝

This Python function `date_formatter` is a higher-order function that returns a function for formatting a given date according to the specified country code.
The `date_formatter` function accepts a country code (e.g., 'ru', 'us', 'ca') and generates a formatter function that formats a `date` object into a string following the country's date format.

## Purpose 🎯

The purpose of this function is to format dates in different formats based on the country code, making it useful for international applications that need to present dates in country-specific formats.

## How It Works 🔍

1. **Country Code Mapping**:  
   The `date_formatter` function defines a dictionary that maps country codes to their respective date formats.

2. **Return a Formatting Function**:  
   After determining the correct format for the provided country code, the function returns another function (`format_date`) that takes a `date` object and converts it to the correct format using Python's `datetime.strftime()`.

3. **Example Usage**:

    - Calling `date_formatter('ru')` will return a function that formats the date as "DD.MM.YYYY".
    - This returned function is then called with a `date` object to get the formatted date.

4. **Valid Country Codes**:  
   The valid country codes are:

    - 'ru' => "DD.MM.YYYY"
    - 'us' => "MM-DD-YYYY"
    - 'ca' => "YYYY-MM-DD"
    - 'br' => "DD/MM/YYYY"
    - 'fr' => "DD.MM.YYYY"
    - 'pt' => "DD-MM-YYYY"

5. **Error Handling**:  
   If an unsupported country code is passed, a `ValueError` is raised.

## Output 📜

Example usage and outputs:

```python
# Create a function to format dates for Russia (ru)
date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))  # Output: "25.01.2022"

# Create a function to format dates for the United States (us)
date_us = date_formatter('us')
print(date_us(today))  # Output: "01-25-2022"
```

## Usage 📦

1. Save the code to a file named `date_formatter.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using Python:

    ```python
    from date_formatter import date_formatter
    from datetime import date

    date_ru = date_formatter('ru')
    today = date(2022, 1, 25)
    print(date_ru(today))  # "25.01.2022"

    date_us = date_formatter('us')
    print(date_us(today))  # "01-25-2022"
    ```

## Conclusion 🚀

The `date_formatter` function provides an efficient way to handle date formatting across multiple countries with different formats.
This is particularly helpful in applications that require date display customization based on the user's location or preferences.
