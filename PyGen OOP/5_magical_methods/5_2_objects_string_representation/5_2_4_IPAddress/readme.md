# IPAddress Class Network Identifier

## Description 📝

The `IPAddress` class represents an IP address, accepting it as either a string (e.g., '192.158.1.38') or a list/tuple of four integers (e.g., [192, 158, 1, 38]) during instantiation.
It uses single dispatch to handle input types, storing the address as a string and providing formal (`__repr__`) and informal (`__str__`) string representations.

## Purpose 🎯

This class is designed for managing IP address data, suitable for network programming, educational examples of type handling, or applications needing IP address representation.

## How It Works 🔍

-   **Initialization**: Uses `@singledispatchmethod` with `__init__` to process input:
    -   **\_from_str()**: Sets `ipaddress` directly from a dotted string.
    -   **\_from_list_or_tuple()**: Converts a list/tuple to a dotted string using `join`.
    -   Base `__init__`: Raises `TypeError` for unsupported types (though not triggered with correct data per note).
-   ****repr**() Method**: Returns `IPAddress('<ipaddress>')` for formal representation.
-   ****str**() Method**: Returns the IP address as a plain dotted string for informal output.

## Usage 📦

1. Save the class in a Python file, e.g., `ip_address.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from ip_address import IPAddress
ip1 = IPAddress("192.158.1.38")
ip2 = IPAddress([10, 0, 0, 1])
print(ip1)
print(repr(ip2))
```

## Conclusion 🚀

The `IPAddress` class provides a flexible and straightforward way to handle IP addresses in Python, supporting multiple input formats with clear string outputs.
Its use of single dispatch makes it extensible, and it can be enhanced with validation or network-related methods for more advanced use cases.
