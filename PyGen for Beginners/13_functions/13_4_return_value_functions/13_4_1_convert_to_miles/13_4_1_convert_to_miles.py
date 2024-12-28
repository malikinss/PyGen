'''
TODO:
    Write a function convert_to_miles(km) that takes a distance in kilometers
    as an argument and returns the distance in miles.

NOTE:
    The conversion formula is:
        miles = kilometers * 0.6214.
'''


def convert_to_miles(km: int) -> float:
    """
    Converts a distance from kilometers to miles.

    The function takes a distance in kilometers and converts it to miles using
    the conversion formula: miles = kilometers * 0.6214.

    Args:
    km (int): The distance in kilometers.

    Returns:
    float: The distance in miles.
    """
    return km * 0.6214


# Example usage
num = int(input())  # Read input
print(convert_to_miles(num))  # Call the function and print the result
