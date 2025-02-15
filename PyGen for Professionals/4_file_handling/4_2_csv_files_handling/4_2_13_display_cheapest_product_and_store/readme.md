# Cheapest Product Finder 💸

## Description 📝

This program reads a `CSV` file containing prices of various products in multiple stores and identifies the cheapest product and the store where it's sold.
It outputs the product name and the corresponding store name in a specified format.
If there are multiple products with the same minimum price, it displays the product whose name is lexicographically smaller.
Similarly, if there are multiple stores selling the product at the same price, the store with the lexicographically smaller name is chosen.

## Purpose 🎯

The purpose of this program is to help users quickly identify the cheapest product across multiple stores by analyzing a `CSV` file with product prices.

## How It Works 🔍

1. The program reads a `CSV` file that contains store names and product prices.
2. It determines the minimum price of each product in each store.
3. It finds the overall cheapest product and the store that offers it.
4. If there are multiple products or stores with the same price, it selects the lexicographically smallest one.

## Output 📜

The program outputs the cheapest product and the store where it's sold in the following format:

```
<Product name>: <Store name>
```

### Example Output:

```
Strawberry yogurt: VkusVill
```

## Usage 📦

1. Prepare a `CSV` file (`prices.csv`) containing product prices across various stores. The file should be structured as follows:

    - The first column should contain store names.
    - The following columns should contain product prices with product names as headers.

2. Run the program by executing the script.

3. The program will print the cheapest product and the store where it’s sold.

## Conclusion 🚀

This program is a simple yet powerful tool to help you find the cheapest product from a set of stores quickly.
It’s efficient, and handles cases where multiple products or stores have the same price by considering lexicographical order.
