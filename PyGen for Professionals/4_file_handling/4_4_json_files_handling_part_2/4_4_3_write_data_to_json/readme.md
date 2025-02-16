# Writing Football Club Data to JSON

## Description 📝

This script gathers information about three football clubs and writes it to a JSON file with a specific indentation.

## Purpose 🎯

The script ensures:

-   The data structure follows the required format.
-   The order of dictionaries remains unchanged.
-   The JSON file is indented with three spaces.

## How It Works 🔍

1. **write_data_to_json() Function**:

    - Takes data and an indentation level as arguments.
    - Writes the data to `data.json` with UTF-8 encoding.

2. **Club Data**:

    - Three dictionaries store football club details.
    - These dictionaries are combined into a list in the correct order.

3. **Writing to JSON**:
    - The `json.dump()` function is used with an indentation of three spaces.

## Output 📜

The `data.json` file will contain:

```json
[
    {
        "name": "FC Byern Munchen",
        "country": "Germany",
        "founded": 1900,
        "trainer": "Julian Nagelsmann",
        "goalkeeper": "M. Neuer",
        "league_position": 1
    },
    {
        "name": "FC Barcelona",
        "country": "Spain",
        "founded": 1899,
        "trainer": "Xavier Creus",
        "goalkeeper": "M. Ter Stegen",
        "league_position": 7
    },
    {
        "name": "FC Manchester United",
        "country": "England",
        "founded": 1878,
        "trainer": "Michael Carrick",
        "goalkeeper": "D. De Gea",
        "league_position": 8
    }
]
```

## Usage 📦

1. Save the script as `write_clubs.py`.
2. Run the script:
    ```
    python write_clubs.py
    ```
3. Open `data.json` to verify the structured data.

## Conclusion 🚀

This script provides a simple yet structured way to store football club information in JSON format while maintaining data order and readability.
