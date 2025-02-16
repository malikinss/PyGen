# Religion Grouping Program 📝

## Description 📝

This program processes a JSON file (`countries.json`) that contains a list of countries and the religions practiced in them.
It groups the countries by religion and creates a new JSON object where each religion is a key, and its value is a list of countries where that religion is practiced.
The result is then saved to a file (`religion.json`).

## Purpose 🎯

The purpose of this program is to transform a list of countries and religions into a grouped structure, where each religion is associated with all countries practicing it.
This makes it easy to analyze and organize countries based on their religious affiliations.

## How It Works 🔍

1. The program reads data from `countries.json`, which contains a list of dictionaries. Each dictionary has a `country` and a `religion` key.
2. It processes this data, grouping countries by religion. For each religion, a list of countries where that religion is practiced is created.
3. The result is a new JSON object, where each religion is a key and its corresponding value is the list of countries practicing that religion.
4. The resulting data is written to `religion.json`.

### Key Details:

-   Input: A list of dictionaries with `country` and `religion` attributes.
-   Output: A dictionary with religion names as keys and lists of countries as values.

## Output 📜

### Example:

#### Input (`countries.json`):

```json
[
    {
        "country": "Afghanistan",
        "religion": "Islam"
    },
    {
        "country": "Albania",
        "religion": "Islam"
    },
    {
        "country": "India",
        "religion": "Hinduism"
    },
    {
        "country": "Nepal",
        "religion": "Hinduism"
    }
]
```

#### Output (`religion.json`):

```json
{
    "Islam": ["Afghanistan", "Albania"],
    "Hinduism": ["India", "Nepal"]
}
```

(Note: The order of countries within each religion is preserved.)

## Usage 📦

1. Ensure that the `countries.json` file contains the country-religion data.
2. Run the program, which will process the data and group the countries by religion.
3. The program will output the grouped data into the `religion.json` file.

## Conclusion 🚀

This program helps organize country-religion data into a more accessible format, where each religion is directly associated with the countries where it is practiced.
This can be useful for various applications such as analysis, reporting, or data management tasks.
