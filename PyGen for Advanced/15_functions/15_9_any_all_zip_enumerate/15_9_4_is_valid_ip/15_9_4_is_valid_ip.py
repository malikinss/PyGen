'''
TODO:
    An IP address is a unique numeric identifier for a device in a computer
    network that uses the TCP/IP protocol.

    In version 4, an IP address is a 32-bit number.

    The address is written as four decimal numbers (octets) with a value
    from 0 to 255 (inclusive), separated by periods, for example, 192.168.1.2.

    Write a program using the built-in all() function to check the correctness
    of an IP address:
        whether all octets in the IP address are numbers with a value
        from 0 to 255.

NOTE:
    Leading zeros should be ignored.
'''


def is_valid_ip(ip: str) -> bool:
    """
    Checks whether a given string is a valid IPv4 address.

    An IP address is valid if:
    - It consists of exactly four octets separated by dots.
    - Each octet is a numeric value between 0 and 255.
    - Leading zeros are ignored.

    Args:
        ip (str): The IP address as a string.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    return all(
        octet.isdigit() and 0 <= int(octet) <= 255
        for octet in ip.split('.')
    )


# Read input and check validity
ip_address = input().strip()
print(is_valid_ip(ip_address))
