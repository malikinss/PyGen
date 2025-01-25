'''
TODO:
    An IP address consists of four numbers from 0 to 255 (inclusive) separated
    by a period.

    Write a function generate_ip() that uses the random module to generate
    and return a random valid IP address.

NOTE:
    Example of a valid (incorrect) IP address:
        192.168.5.250 # valid
        199.300.521.255 # invalid

    You don't need to call the generate_ip() function, you just need
    to implement it.
'''
import random


def generate_ip() -> str:
    """
    Generates and returns a random valid IP address consisting of four numbers
    from 0 to 255, each separated by a period.

    Returns:
        str: A randomly generated valid IP address.
    """
    ip_segments = [str(random.randint(0, 255)) for _ in range(4)]
    return '.'.join(ip_segments)
