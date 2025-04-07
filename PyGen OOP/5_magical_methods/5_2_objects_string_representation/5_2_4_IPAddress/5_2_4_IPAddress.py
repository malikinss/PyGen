'''
TODO:
    An IP address is a unique address that identifies a device on the Internet
    or a local network.

    IP addresses are a set of four integers separated by periods.

    For example, 192.158.1.38.

    Each number in the set belongs to the interval from 0 to 255.

    Thus, the full range of IP addresses is addresses:
        from 0.0.0.0 to 255.255.255.255.

    Implement the IPAddress class, which describes an IP address.

    When instantiated, the class must accept one argument:
        - ipaddress — an IP address, represented as one of the following:
            1. a string of four integers separated by dots
            2. a list or tuple of four integers

    An instance of the IPAddress class must have the following formal string
    representation:
        IPAddress('<IP address as four integers separated by dots>')

    And the following informal string representation:
        <IP address as four integers separated by dots>

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the IPAddress
    class, it can be arbitrary.
'''
from functools import singledispatchmethod


class IPAddress:
    """
    A class representing an IP address.
    """

    @singledispatchmethod
    def __init__(self, ipaddress: object) -> None:
        """
        Initialize an IPAddress instance.

        Args:
            ipaddress (object): The IP address as a string or list/tuple.

        Raises:
            TypeError: If the ipaddress type is not supported.
        """
        raise TypeError("Unsupported type for IP address")

    @__init__.register
    def _from_str(self, ipaddress: str) -> None:
        """
        Initialize from a string of four integers separated by dots.

        Args:
            ipaddress (str): The IP address, e.g., '192.158.1.38'.
        """
        self.ipaddress = ipaddress

    @__init__.register
    def _from_list_or_tuple(self, ipaddress: list | tuple) -> None:
        """
        Initialize from a list or tuple of four integers.

        Args:
            ipaddress (list | tuple): The IP address, e.g., [192, 158, 1, 38].
        """
        self.ipaddress = ".".join(map(str, ipaddress))

    def __repr__(self) -> str:
        """
        Return a formal string representation of the IP address.

        Returns:
            str: The IP address in format "IPAddress('<ipaddress>')".
        """
        return f"IPAddress('{self.ipaddress}')"

    def __str__(self) -> str:
        """
        Return an informal string representation of the IP address.

        Returns:
            str: The IP address as four integers separated by dots.
        """
        return f"{self.ipaddress}"
