'''
TODO:
    The input to the program is a text string containing 4 positive integers
    separated by a dot.

    Write a program that determines if an input string of text
    is a valid ip address.
'''


def is_valid_ip(ip: str) -> None:
    """
    This function checks if the input string is a valid IPv4 address.
    A valid IPv4 address consists of 4 numbers between 0 and 255,
    separated by dots.

    Args:
        ip (str): The input string representing the IP address.

    Returns:
        None: Prints 'YES' if the IP address is valid, otherwise prints 'NO'.
    """
    # Split the input string by dot and check each part
    parts = ip.split(".")

    # Check if there are exactly 4 parts and each part is within
    # the valid range
    for part in parts:
        if not (part.isdigit() and 0 <= int(part) <= 255):
            print("NO")
            return

    # If all checks passed
    print("YES")


# Input string containing the IP address
ip_address = input()

# Call the function to validate the IP address
is_valid_ip(ip_address)
