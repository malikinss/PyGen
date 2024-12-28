'''
TODO:
    The online store provides express delivery for its products at a price
    of 1000 rubles for the first product and 120 rubles for each
    subsequent product.

    Write a function get_shipping_cost(quantity), which takes as an argument
    the natural number quantity - the number of goods in the order
    - and returns the shipping cost.
'''


def get_shipping_cost(quantity: int) -> int:
    """
    Calculate the shipping cost for an order based on the quantity of products.

    The first product costs 1000 rubles for express delivery,
    and each subsequent product costs an additional 120 rubles.

    Args:
        quantity (int): The number of products in the order.

    Returns:
        int: The total shipping cost for the order.
    """
    if quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")

    return 1000 + (quantity - 1) * 120


n = int(input("Enter the number of products in the order: "))
print(get_shipping_cost(n))
