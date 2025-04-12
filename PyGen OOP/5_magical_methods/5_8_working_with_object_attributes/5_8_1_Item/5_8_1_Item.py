'''
TODO:
    It was necessary to implement the Item class, which describes an item.

    When creating an instance, the class had to accept three arguments in
    the following order:
        name — item name
        price — item price in rubles
        quantity — item quantity

    It was assumed that when accessing the name attribute of an instance of
    the Item class, its name would be returned with a capital letter, and when
    accessing the total attribute, the product of the item's price and its
    quantity would be returned.

    The programmer was in a hurry and solved the problem incorrectly.

    Complete the code below and implement the correct Item class.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Item class,
    it can be arbitrary.
'''
from typing import Union, Any


class Item:
    """
    A class representing an item with name, price, and quantity.
    """

    def __init__(
        self, name: str, price: Union[int, float], quantity: int
    ) -> None:
        """
        Initialize Item with name, price, and quantity.

        Args:
            name (str): The name of the item.
            price (int | float): The price of the item in rubles.
            quantity (int): The quantity of the item.
        """
        self._name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, attr: str) -> Any:
        """
        Handle attribute access, customizing name and total.

        Args:
            attr (str): The name of the attribute.

        Returns:
            Any: The attribute value, capitalized for 'name',
                 price * quantity for 'total'.
        """
        if attr == 'name':
            name = object.__getattribute__(self, '_name')
            return name.title()
        elif attr == 'total':
            price = object.__getattribute__(self, 'price')
            quantity = object.__getattribute__(self, 'quantity')
            return price * quantity
        return object.__getattribute__(self, attr)
