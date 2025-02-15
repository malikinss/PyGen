# Discounted Products Finder Program

## Description 📝

This Python script reads product pricing data from a `CSV` file (`sales.csv`) and displays the names of products whose prices have decreased after a discount.
The program demonstrates how to read and process `CSV` files and compare values.

## Purpose 🎯

The goal of this program is to read the pricing data of various household appliances, check for any price decreases, and display the names of the products whose prices have dropped.
This exercise demonstrates working with `CSV` files, data comparison, and filtering results in Python.

## How It Works 🔍

1. **read_csv_data() Function**: Reads data from the `CSV` file, extracting the product name, old price, and new discounted price.
2. **display_discounted_products() Function**: Iterates through the list of products and prints the name of each product whose new price is lower than the old price.

## Output 📜

When the script is executed, it will output the names of the products whose prices have decreased:

```
Falmec Afrodite 60/600 hood
```

## Usage 📦

1. Save the code to a file named `find_discounted_products.py`.
2. Create a `CSV` file `sales.csv` in the same directory with the following contents:
    ```
    name;old_price;new_price
    Built-in dishwasher De'Longhi DDW 06S;23089;31862
    Falmec Afrodite 60/600 hood;27694;18001
    ```
3. Open a terminal or command prompt.
4. Navigate to the directory where the files are located.
5. Execute the script using the command:
    ```
    python find_discounted_products.py
    ```
6. The program will display the names of the products whose prices have decreased.

## Conclusion 🚀

This program helps to identify discounted products whose prices have actually decreased, allowing for better shopping decisions.
It demonstrates reading `CSV` data, comparing values, and filtering results.
