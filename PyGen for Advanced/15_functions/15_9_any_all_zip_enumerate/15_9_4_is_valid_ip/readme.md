# IP Address Validator 🖥️

## Description 📝

This program validates whether a given IPv4 address is correct according to the standard rules for IP addresses.
The address must consist of four decimal numbers (octets), each ranging from 0 to 255, separated by periods.
Leading zeros in octets are ignored.

## Purpose 🎯

The goal is to check if a string representing an IP address adheres to the structure of an IPv4 address by ensuring each octet is a valid number between 0 and 255.

## How It Works 🔍

1. The function `is_valid_ip(ip)` checks:
    - The IP address is split into four octets by the dot (`.`) separator.
    - Each octet is checked to ensure it is a digit and its integer value falls between 0 and 255.
    - Leading zeros are implicitly handled as `int()` converts the string to an integer, automatically discarding any leading zeros.
2. The function returns `True` if all the octets are valid, otherwise `False`.
3. The `all()` function is used to ensure that all octets meet the criteria.

## Output 📜

-   **True** if the IP address is valid.
-   **False** if the IP address is invalid.

### Example Output:

```
True
```

## Usage 📦

1. Input a string representing the IPv4 address.
2. The program checks if it consists of exactly four octets, each ranging from 0 to 255.
3. The result (`True` or `False`) is printed, indicating whether the IP address is valid.

## Conclusion 🚀

This program efficiently validates the correctness of an IPv4 address using Python's built-in functions for string manipulation, iteration, and logical checking.
