# Program to Filter Countries Based on Population and Name Starting with 'G' 🌍

## Description 📝

This program reads a file **"population.txt"** containing the names of countries and their populations, separated by a tab character. It filters out the countries whose names begin with the letter 'G' and whose populations are greater than 500,000 people. The filtered countries are printed in the same order as in the file.

## Purpose 🎯

To list all countries whose names start with the letter 'G' and have a population greater than 500,000.

## How It Works 🔍

1. **Reading Data (`get_data_from_file`)**:

    - The program reads all the lines from **"population.txt"**, each line containing a country and its population, separated by a tab character. The content is stored as a list of strings, one for each line.

2. **Splitting Data (`get_correct_data`)**:

    - Each line is split by the tab character (`\t`), resulting in a list of two elements: the country name and its population. This list is then returned as a list of lists.

3. **Filtering Countries (`filter_countries`)**:

    - The program filters the countries based on two conditions:
        - The country name starts with the letter 'G' (using the `startswith('G')` method).
        - The population is greater than 500,000 (by converting the population string to an integer and checking if it exceeds 500,000).
    - Only the countries meeting these conditions are included in the resulting list.

4. **Output**:
    - The program prints the filtered countries, each on a separate line.

## Example Usage:

**File (`population.txt`):**

```
Germany	83019200
Greece	10423000
Guatemala	17915568
Gabon	2112275
Greenland	56000
Gambia	2416668
```

**Program Output:**

```python
Germany
Greece
Guatemala
```

## Conclusion 🚀

This program efficiently filters countries based on their name and population size and can be adapted for various use cases that require similar filtering of country data!
