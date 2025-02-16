# Food Services Analysis 📝

## Description 📝

This program analyzes the food services data from a `JSON` file, identifying:

1. The district with the highest number of establishments.
2. The chain with the most establishments.

## Purpose 🎯

The purpose of this program is to provide insights into the food services landscape in Moscow, identifying the areas and chains with the most establishments based on the provided data.

## How It Works 🔍

1. **Reading the Data**: The program reads the `JSON` data from the `food_services.json` file using `read_json_file()`.
2. **Counting Districts**: It counts how many establishments are located in each district using the `count_items()` function, which uses a key extractor to pull out the district name from each record.
3. **Counting Chains**: It counts the number of establishments for each chain, filtering only those establishments marked as "yes" in the `IsNetObject` field (indicating a chain).
4. **Output**: It uses the `print_most_frequent()` function to print the most frequent district and chain along with their counts.

## Output 📜

### Example:

Given the data, the program might output:

```
district Metrogorodok: 456
French bakery SeDelice: 144
```

## Usage 📦

1. Place the `food_services.json` file in the same directory as the script or specify the full path to the file.
2. Run the script. It will automatically analyze the data and print the results.
3. The program will output the district with the most establishments and the chain with the largest number of locations.

## Conclusion 🚀

This program is useful for analyzing food service establishments in a specific region, providing quick insights into the district and chain dominance in Moscow.
