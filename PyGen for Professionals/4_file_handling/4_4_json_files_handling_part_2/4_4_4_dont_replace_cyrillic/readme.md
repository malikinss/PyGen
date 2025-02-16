# JSON Conversion Utility 📝

## Description 📝

This script converts a dictionary containing specifications of a processor into a formatted JSON string.
It ensures proper indentation and preserves Cyrillic characters without replacing them with Unicode escape sequences.

## Purpose 🎯

The primary goal of this script is to demonstrate how to use Python's `json` module to format and output JSON data while maintaining readability and non-ASCII characters.

## How It Works 🔍

1. The `convert_to_json()` function takes a dictionary as input.
2. It uses `json.dumps()` with `indent=3` for structured formatting.
3. The `ensure_ascii=False` parameter ensures Cyrillic characters remain readable.
4. The result is printed in JSON format.

## Output 📜

The expected output of the script is:

```json
{
    "Модель": "AMD Ryzen 5 5600G",
    "Год релиза": 2021,
    "Сокет": "AM4",
    "Техпроцесс": "7 нм",
    "Ядро": "Cezanne",
    "Объем кэша L2": "3 МБ",
    "Объем кэша L3": "16 МБ",
    "Базовая частота": "3900 МГц"
}
```

## Usage 📦

Follow these steps to run the script:

1. Ensure Python is installed on your system.
2. Copy the script into a `.py` file.
3. Run the script using the command:

    ```bash
    python script.py
    ```

## Conclusion 🚀

This script is a simple and effective way to format and print JSON data while preserving non-ASCII characters. It can be useful for working with localized data in Python.
