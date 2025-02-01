# Primary Cities with Population Over 10 Million

## Description

This program processes a list of cities, each represented by a record containing the city name, population, and type. The program filters cities based on two criteria:

1. The city type must be "primary".
2. The population must be greater than 10 million.

It then outputs an alphabetical list of primary cities that meet these criteria, formatted as a single string where each city name is separated by a comma.

## Purpose

The purpose of this program is to demonstrate how built-in functions such as `filter()`, `map()`, `sorted()`, and `reduce()` can be applied to:

-   Filter cities based on specific conditions.
-   Map the necessary data from the filtered list.
-   Sort the cities alphabetically.
-   Reduce the list into a formatted string for output.

## How It Works

1. **Filtering**: The program uses the `filter()` function to keep only cities that are "primary" and have a population greater than 10 million.
2. **Mapping**: The `map()` function extracts the names of the filtered cities.
3. **Sorting**: The `sorted()` function orders the city names alphabetically.
4. **Reducing**: The `reduce()` function combines the sorted city names into a single string, separated by commas.

## Output

The program outputs a list of primary cities with populations greater than 10 million, formatted as a single string:

```
Cities: Beijing, Buenos Aires, Cairo, Dhaka, Manila
```

## Usage

To use the program, the following steps are performed:

1. Prepare a list of city records, where each record contains the city name, population, and type.
2. Call the `process_cities` function with this list.
3. The function will return a formatted string containing the names of the primary cities with populations over 10 million.

## Conclusion

This program efficiently filters, maps, sorts, and reduces the list of cities to produce the desired output. It is a great example of applying Python's built-in functional programming tools to real-world data processing tasks.
