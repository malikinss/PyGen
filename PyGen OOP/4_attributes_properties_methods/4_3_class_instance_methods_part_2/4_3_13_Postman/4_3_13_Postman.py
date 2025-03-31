'''
TODO:
    Implement a Postman class that describes a postman.

    The class should not take any arguments when instantiated.

    An instance of the Postman class must have one attribute:
        - delivery_data — an initially empty list of addresses to which
        letters should be delivered

    An instance of the Postman class must have three instance methods:
        - add_delivery() — a method that takes a street, house, and apartment
        as arguments and adds this data to the list of addresses as a tuple:
            (<street>, <house>, <apartment>)
        - get_houses_for_street() — a method that takes a street as an
        argument and returns a list of all houses on that street to which
        letters should be delivered
        - get_flats_for_house() — a method that takes a street and house as
        arguments and returns a list of all apartments in that house to which
        letters should be delivered

NOTE:
    The houses and apartments in the lists returned by get_houses_for_street()
    and get_flats_for_house() must be in the order in which they were added.

    If a house or apartment located in the same house appears in
    the delivery_data address list several times, then those that were added
    earlier should be specified.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from typing import List, Tuple


class Postman:
    """A class representing a postman with a delivery list.

    This class maintains a list of delivery addresses as tuples of street,
    house, and apartment, and provides methods to add addresses and retrieve
    houses or apartments based on specific criteria.

    Attributes:
        delivery_data (list[tuple[str, int, int]]): A list of delivery
        addresses.

    Methods:
        add_delivery(street, house, apartment): Adds an address to
        the delivery list.
        get_houses_for_street(street): Returns a list of houses on the given
        street.
        get_flats_for_house(street, house): Returns a list of apartments in
        the given house.
    """

    def __init__(self) -> None:
        """Initialize a Postman instance with an empty delivery list.

        Sets up the delivery list as an empty list of addresses.

        Returns:
            None
        """
        self.delivery_data: List[Tuple[str, int, int]] = []

    def add_delivery(self, street: str, house: int, apartment: int) -> None:
        """
        Add a delivery address to the list.

        Appends a tuple of street, house, and apartment to the delivery list.

        Args:
            street (str): The street name of the address.
            house (int): The house number of the address.
            apartment (int): The apartment number of the address.

        Returns:
            None
        """
        self.delivery_data.append((street, house, apartment))

    def get_houses_for_street(self, street: str) -> List[int]:
        """
        Return a list of houses on the given street.

        Retrieves all unique house numbers for the specified street in the
        order they were added, preserving the first occurrence of duplicates.

        Args:
            street (str): The street name to filter by.

        Returns:
            list[int]: A list of house numbers.
        """
        seen = set()
        matching_addresses = [
            address for address in self.delivery_data if address[0] == street
        ]
        unique_houses = [
            address[1] for address in matching_addresses
            if not (address[1] in seen or seen.add(address[1]))
        ]
        return unique_houses

    def get_flats_for_house(self, street: str, house: int) -> List[int]:
        """
        Return a list of apartments in the given house on the street.

        Retrieves all unique apartment numbers for the specified street and
        house in the order they were added, preserving the first occurrence of
        duplicates.

        Args:
            street (str): The street name to filter by.
            house (int): The house number to filter by.

        Returns:
            list[int]: A list of apartment numbers.
        """
        seen = set()
        matching_addresses = [
            address for address in self.delivery_data
            if address[0] == street and address[1] == house
        ]
        unique_flats = [
            address[2] for address in matching_addresses
            if not (address[2] in seen or seen.add(address[2]))
        ]
        return unique_flats
