'''
TODO:
    Implement the OrderStatus class, which describes a flag with the states of
    online orders.

    The flag must have three elements:
        ORDER_PLACED
        PAYMENT_RECEIVED
        SHIPPING_COMPLETE

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the OrderStatus
    class, it can be arbitrary.
'''
from enum import Flag, auto


class OrderStatus(Flag):
    """Flag for online order states."""
    ORDER_PLACED = auto()
    PAYMENT_RECEIVED = auto()
    SHIPPING_COMPLETE = auto()
