# Shipping Cost Calculator 📦

## Description 📝

This Python script calculates the total shipping cost for an order from an online store.
The store offers express delivery at a base rate of 1000 rubles for the first product and an additional 120 rubles for each subsequent product.

## Purpose 🎯

The `get_shipping_cost` function allows users to easily compute the shipping cost based on the number of products in the order.
This can be useful for online shopping platforms, helping to automate delivery cost calculations.

## How It Works 🔍

1. **Function `get_shipping_cost(quantity)`**:

    - If the quantity is less than or equal to 0, a `ValueError` is raised.
    - The first product costs **1000 rubles**.
    - Each additional product adds **120 rubles** to the total.
    - The formula used is:
      \[
      \text{Total Cost} = 1000 + (quantity - 1) \times 120
      \]

2. **Example**:

    ```
    Enter the number of products in the order: 3
    Output: 1240
    ```

    - 1st product: 1000 rubles
    - 2nd product: +120 rubles
    - 3rd product: +120 rubles  
      **Total: 1240 rubles**

3. **Edge Case**:
    - If the quantity is `0` or negative, the function raises an error:
        ```
        ValueError: Quantity must be a positive integer.
        ```

## Usage 📦

1. Copy the code into a Python file, e.g., `shipping_calculator.py`.
2. Run the script in the terminal:
    ```bash
    python shipping_calculator.py
    ```
3. Enter the desired number of products when prompted.
4. The total shipping cost will be displayed.

## Conclusion 🚀

This simple script efficiently calculates shipping costs and includes error handling for invalid inputs.
It can be integrated into e-commerce platforms to automate delivery price calculations, ensuring accurate cost estimations for customers.
