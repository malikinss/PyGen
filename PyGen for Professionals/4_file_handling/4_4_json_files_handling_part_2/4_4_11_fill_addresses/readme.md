# Playground Address Grouping Program 📝

## Description 📝

This program processes a `CSV` file (`playgrounds.csv`) containing information about sports grounds in Moscow.
It groups the playgrounds based on their administrative district and district name, then creates a `JSON` object where each administrative district contains a dictionary of districts, with each district holding a list of playground addresses.
The result is saved into a file (`addresses.json`).

## Purpose 🎯

The goal of this program is to transform raw `CSV` data about playgrounds into a structured format that groups playgrounds by their administrative district and district name.
This structured data can be used for further analysis, reporting, or displaying information related to the locations of playgrounds in Moscow.

## How It Works 🔍

1. The program reads data from the `playgrounds.csv` file, which contains columns: `ObjectName`, `AdmArea`, `District`, and `Address`.
2. The program processes the data, grouping the playgrounds by administrative district and district name.
3. The resulting structure is a `JSON` object where each key is an administrative district, and the corresponding value is a dictionary with districts as keys and lists of addresses as values.
4. Finally, the program writes this grouped data to the `addresses.json` file.

### Key Details:

-   Input: A CSV file with columns `ObjectName`, `AdmArea`, `District`, and `Address`, where the delimiter is a semicolon (`;`).
-   Output: A JSON object where the structure is as follows:
    -   The key is an administrative district (`AdmArea`).
    -   The value is another dictionary where the key is a district (`District`) and the value is a list of addresses.

## Output 📜

### Example:

#### Input (`playgrounds.csv`):

```csv
ObjectName;AdmArea;District;Address
Park, green urban area "Lianozovsky Park of Culture and Leisure";North-Eastern Administrative District;Lianozovo District;Uglichskaya Street, Building 13
Park, green urban area "Lianozovsky Park of Culture and Leisure";North-Eastern Administrative District;Lianozovo District;Altufevskoe Shosse, Building 147A
Park "Otradnoe";North-Eastern Administrative District;Otradnoe District;Altufevskoe Shosse, Building 20A
Park "Otradnoe";North-Eastern Administrative District;Otradnoe District;Yurlovsky Proezd, Building 8, Building 1
```

#### Output (`addresses.json`):

```json
{
    "North-Eastern Administrative District": {
        "Lianozovo District": [
            "Uglichskaya Street, Building 13",
            "Altufevskoe Shosse, Building 147A"
        ],
        "Otradnoe District": [
            "Altufevskoe Shosse, Building 20A",
            "Yurlovsky Proezd, Building 8, Building 1"
        ]
    }
}
```

(Note: The order of addresses within each district is preserved.)

## Usage 📦

1. Ensure that the `playgrounds.csv` file contains the playground data with correct semicolon delimiters.
2. Run the program, which will read the `CSV` file, process the data, and group playgrounds by district and administrative area.
3. The program will output the resulting grouped data into the `addresses.json` file.

## Conclusion 🚀

This program helps organize playground location data by administrative district and district name, making it more accessible for analysis and reporting.
By transforming `CSV` data into a structured `JSON` format, the program makes it easier to work with large datasets and extract meaningful insights.
