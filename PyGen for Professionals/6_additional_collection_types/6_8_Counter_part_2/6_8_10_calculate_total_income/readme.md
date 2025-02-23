# Vegetable Sales Income Calculation

## Description 📝

This Python program calculates the total income Timur earned for the year by selling vegetables.
0he program reads sales data from multiple CSV files (one for each quarter) and prices from a JSON file, then computes the total income based on product sales and their respective prices.

## Purpose 🎯

The program processes quarterly sales data, calculates the total kilograms sold for each vegetable, and multiplies the amount by its price to determine the total income.

## How It Works 🔍

1. **Reading CSV Files**: The program reads the sales data for each quarter from CSV files (quarter1.csv, quarter2.csv, quarter3.csv, and quarter4.csv). Each file contains the product name and the amount sold per month.
2. **Reading Prices**: The prices.json file contains a dictionary mapping each product to its price per kilogram.
3. **Processing Data**:
    - The program sums up the sales of each product from the monthly data in each quarter.
    - It then multiplies the total kilograms sold by the price from the `prices.json` file to calculate the total income for the year.
4. **Output**: The program prints the total income earned from selling the vegetables.

## Output 📜

The program outputs a single integer, which is the total income earned for the year.

### Example:

```python
./tests/quarter1.csv:
product,January,February,March
Potatoes,39,61,3
Daikon,51,96,83
...

./tests/prices.json:
{
  "Potatoes": 53,
  "Daikon": 55,
  ...
}
```

#### Output:

```
123456
```

## Usage 📦

1. Place the CSV files (`quarter1.csv`, `quarter2.csv`, `quarter3.csv`, `quarter4.csv`) and the `prices.json` file in a folder, e.g., `./tests/`.
2. Run the Python script:
    ```bash
    python vegetable_sales_income.py
    ```
3. The script will read the data and print the total income for the year.

## Conclusion 🚀

This program allows Timur to track his income from selling vegetables over the course of the year.
It aggregates sales data from each quarter, calculates the total income, and provides a quick and automated way to track his earnings.
