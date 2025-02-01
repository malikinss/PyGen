# print_products() Function

## Description

The `print_products()` function prints a numbered list of valid product names provided as arguments. It only considers non-empty strings as products and ignores other types of data.

## Purpose

This function helps in printing a list of product names, where each product is assigned a unique number. If no valid products are provided, it prints a default message.

## How It Works

-   The function accepts an arbitrary number of arguments.
-   It iterates through the arguments and checks if each one is a non-empty string.
-   For valid products (non-empty strings), it prints them with a numbered prefix.
-   If no valid products are found, it prints "No products".

## Usage

Example calls:

```python
print_products('Laptop', 'Phone', 'Tablet')  # Output:
# 1) Laptop
# 2) Phone
# 3) Tablet

print_products('Shoes', 123, 'T-shirt')     # Output:
# 1) Shoes
# 2) T-shirt

print_products(1, 2, 3)                    # Output: "No products"
```

## Conclusion

The `print_products()` function is a simple way to print a list of products while ignoring invalid entries, ensuring that only valid product names (non-empty strings) are shown.
