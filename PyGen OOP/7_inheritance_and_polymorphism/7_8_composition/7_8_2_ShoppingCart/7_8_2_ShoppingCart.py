'''
TODO:
    Implement the Item class that describes a product.

    When instantiated, the class must accept two arguments in the following
    order:
        name — the name of the product
        price — the price of the product in dollars

    An instance of the Item class must have the following informal string
    representation:
        <product name>, <product price>$

    Also implement the ShoppingCart class that describes a shopping cart.

    When instantiated, the class must accept one argument:
        items — an iterable that defines the initial set of products in
                the cart.
                If not passed, the cart is considered empty

    The ShoppingCart class must have three instance methods:
        add() — a method that takes an item as an argument and adds it to
                the cart
        total() — a method that returns the total cost of all items in the cart
        remove() — a method that takes an item name as an argument and removes
                   it from the cart.
                   If there are multiple products with the given name in
                   the shopping cart, they should all be deleted

    A ShoppingCart class instance should have the following informal string
    representation:
        <name of first product in cart>, <price of first product in cart>$
        <name of second product in cart>, <price of second product in cart>$
        ...

NOTE:
    If the shopping cart is empty, its informal string representation should
    be an empty string.

    No additional data validation is required.

    It is guaranteed that the implemented classes are used only with correct
    data.

    There are no restrictions regarding the implementations of the classes,
    they can be arbitrary.
'''
from collections.abc import Iterable


class Item:
    """
    Product with name and price.
    """

    def __init__(self, name: str, price: float) -> None:
        """
        Init product.

        Args:
            name: Product name.
            price: Product price in dollars.
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        Get string representation.

        Returns:
            str: Format <name>, <price>$.
        """
        return f"{self.name}, {self.price}$"


class ShoppingCart:
    """
    Shopping cart for products.
    """

    def __init__(self, items: Iterable[Item] = ()) -> None:
        """
        Init cart with optional items.

        Args:
            items: Initial products, defaults to empty.
        """
        self._cart = list(items)

    def add(self, item: Item) -> None:
        """
        Add item to cart.

        Args:
            item: Product to add.
        """
        self._cart.append(item)

    def total(self) -> float:
        """
        Get total cost.

        Returns:
            float: Sum of item prices.
        """
        return sum(item.price for item in self._cart)

    def remove(self, item_name: str) -> None:
        """
        Remove all items with given name.

        Args:
            item_name: Name of product to remove.
        """
        self._cart[:] = [item for item in self._cart if item.name != item_name]

    def __str__(self) -> str:
        """
        Get string representation.

        Returns:
            str: Items as <name>, <price>$ per line or empty string.
        """
        return "\n".join(str(item) for item in self._cart)
