# Validate IP Address 📝

## Description 📝

This Python program checks whether a given string is a valid IPv4 address. A valid IPv4 address consists of four positive integers (between 0 and 255) separated by dots.

## Purpose 🎯

The goal of this program is to verify if a string input represents a valid IPv4 address. It helps ensure that the input conforms to the format required for IP addresses.

## How It Works 🔍

1. The program takes a string representing an IP address as input.
2. It splits the string by the dot (`.`) character into four parts.
3. It checks if each part is a digit and within the valid range (0-255).
4. If all parts are valid, the program prints "YES". Otherwise, it prints "NO".

## Output 📜

```bash
Example Input:
192.168.1.1
Example Output:
YES

Example Input:
256.300.1.1
Example Output:
NO
```

## Usage 📦

1. Save the script as `validate_ip.py`.
2. Run the script in a Python environment.
3. Input a string representing an IP address (e.g., `192.168.1.1`).
4. The program will output whether the IP address is valid or not.

## Conclusion 🚀

This program is a simple and effective way to validate IPv4 addresses, ensuring that they adhere to the proper format.
