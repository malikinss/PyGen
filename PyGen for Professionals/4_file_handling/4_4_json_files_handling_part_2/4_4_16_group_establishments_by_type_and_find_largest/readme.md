# Establishment Types Analysis 📝

## Description 📝

This program analyzes the food services data from a `JSON` file, identifying the largest establishment for each type based on the number of seats.

## Purpose 🎯

The purpose of this program is to determine the largest establishment for each type (e.g., cafe, restaurant) and display the results in lexicographic order.
It will show the name of the largest establishment and the number of seats it has for each type of establishment.

## How It Works 🔍

1. **Reading the Data**: The program reads the data from the `food_services.json` file using the `read_json_data()` function.
2. **Grouping by Type and Finding the Largest**: The `group_establishments_by_type_and_find_largest()` function processes the data, grouping the establishments by type and keeping track of the largest establishment (based on seat count) for each type.
3. **Output**: The `print_establishments_results()` function prints the results in lexicographic order, showing the type of establishment, its largest establishment's name, and the seat count.

## Output 📜

### Example:

Given the data, the program might output:

```
bar: Bar association PROFSOYUZ, 800
buffet: DINING - KANTINACITY, 320
snack bar: Burger FARSH, 74
...
```

## Usage 📦

1. Place the `food_services.json` file in the same directory as the script or specify the full path to the file.
2. Run the script. It will automatically analyze the data and print the results, displaying each establishment type along with the name and seat count of its largest establishment.

## Conclusion 🚀

This program efficiently categorizes establishments by type and identifies the largest establishment in each category.
The results are displayed in an organized and easily readable format, helping with analysis of food service trends based on establishment size.
