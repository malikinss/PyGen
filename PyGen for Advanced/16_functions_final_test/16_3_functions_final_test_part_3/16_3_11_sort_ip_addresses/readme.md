# IP Address Sorting 🎯

## Description 📝

The program reads a list of IP addresses and sorts them in ascending order based on their decimal representation. The sorting is performed by converting each IP address into a decimal number using a mathematical formula, and the addresses are printed in sorted order.

## Purpose 🎯

This function takes a list of IP addresses, converts them from dot-decimal notation to decimal format, and sorts them accordingly. This is useful for tasks like network analysis or IP address management where sorting by numerical value is necessary.

## How It Works 🔍

1. **Decimal Conversion**:  
   The `dec()` function converts an IP address (in dot-decimal format) to its decimal representation by processing each octet and applying the formula:

    ```
    decimal = octet1 * 256^3 + octet2 * 256^2 + octet3 * 256^1 + octet4 * 256^0
    ```

    where `octet1`, `octet2`, `octet3`, and `octet4` are the four octets in the IP address.

2. **Sorting IPs**:  
   The `sort_ip_addresses()` function reads the input IP addresses, converts each to its decimal value using `dec()`, and then sorts the addresses based on their decimal values.

3. **Output**:  
   After sorting, the program prints the IP addresses in ascending order based on their decimal representation.

## Example Usage:

```python
>>> n = 3
>>> sort_ip_addresses(n)
192.168.0.1
192.168.1.2
192.168.1.10
```

## Conclusion 🚀

The `sort_ip_addresses()` function is useful for sorting IP addresses in a numerical order, which is often needed in network configurations or when managing IP address ranges. By converting the addresses into decimal form, the program can easily perform sorting, ensuring that the addresses are presented in the correct order.
