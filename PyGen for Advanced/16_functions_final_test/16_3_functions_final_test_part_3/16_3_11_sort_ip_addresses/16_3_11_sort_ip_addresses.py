'''
TODO:
    An IP address is a unique numeric identifier for a device in a computer
    network that uses the TCP/IP protocol.

    In version 4, an IP address is a 32-bit number.

    The address is written as four decimal numbers (octets) with a value
    from 0 to 255, separated by periods, for example, 192.168.1.2.

    Write a program that reads IP addresses and outputs them in ascending
    order according to decimal representation.

NOTE:
    To convert the IP address 192.168.1.2 to a decimal number, we use
    the formula:
        192 * 256^3 + 168 * 256^2 + 1*256^1 + 2*256^0 = 3232235778

    Use the optional key argument.
'''


def dec(IP: str) -> int:
    """
    Converts an IP address from its dot-decimal notation to a decimal number.

    Parameters:
    - IP (str): The IP address in dot-decimal notation (e.g., "192.168.1.2").

    Returns:
    - int: The decimal representation of the IP address.
    """
    octets = [int(i) for i in IP.split('.')]

    decimal_value = 0
    for i, octet in enumerate(octets):
        decimal_value += octet * (256 ** (3 - i))

    return decimal_value


def sort_ip_addresses(n: int) -> None:
    """
    Sorts a list of IP addresses in ascending order according to their decimal
    representation.

    Parameters:
    - n (int): The number of IP addresses to input.

    Returns:
    - None: This function prints the sorted IP addresses.
    """
    ip_addresses = [input() for _ in range(n)]
    sorted_ips = sorted(ip_addresses, key=dec)
    print(*sorted_ips, sep='\n')


# Example usage
n = int(input())  # Number of IP addresses
sort_ip_addresses(n)
