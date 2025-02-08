# Country Information 🌍

## Description 📝

This program outputs information about different countries, including their capitals and populations, using parallel iteration over three lists: `countries`, `capitals`, and `populations`.

## Purpose 🎯

The goal is to efficiently format and display country-related information in a structured way, using `zip()` for simultaneous iteration over multiple lists.

## How It Works 🔍

1. The function `print_country_info()` accepts three lists:
    - `countries`: List of country names.
    - `capitals`: List of capital cities.
    - `populations`: List of population numbers.
2. The function iterates over these lists in parallel using `zip()`.
3. For each country, it constructs a formatted string:
    ```
    <capital> is the capital of <country>, population equal <population> people.
    ```
4. It prints this formatted information for each country.

## Output 📜

### Example Output:

```
Moscow is the capital of Russia, population equal 145934462 people.
Washington is the capital of USA, population equal 331002651 people.
London is the capital of UK, population equal 80345321 people.
Berlin is the capital of Germany, population equal 67886011 people.
Paris is the capital of France, population equal 65273511 people.
Delhi is the capital of India, population equal 1380004385 people.
```

## Usage 📦

1. Define three lists: `countries`, `capitals`, and `populations`.
2. Call `print_country_info(countries, capitals, populations)`.
3. The program will print formatted country information for each entry in the lists.

## Conclusion 🚀

This implementation efficiently processes country data, leveraging `zip()` for parallel iteration and string formatting for clear, structured output.
