'''
TODO:
    Implement the BasicPlan class, which describes a basic subscription to
    some online service.

    The class should not take any arguments when instantiated.

    The BasicPlan class should have seven attributes:
        can_stream — attribute with the value True
        can_download — attribute with the value True
        has_SD — attribute with the value True
        has_HD — attribute with the value False
        has_UHD — attribute with the value False
        num_of_devices — attribute with the value 1
        price — attribute with the value $8.99

    Also implement the SilverPlan class, a descendant of the BasicPlan class,
    which describes a mid-level subscription to some online service.

    The process of instantiating the SilverPlan class should be the same as
    the process of instantiating the BasicPlan class.

    The SilverPlan class must have seven attributes:
        can_stream — attribute with value True
        can_download — attribute with value True
        has_SD — attribute with value True
        has_HD — attribute with value True
        has_UHD — attribute with value False
        num_of_devices — attribute with value 2
        price — attribute with value $12.99

    Finally, implement the GoldPlan class, a subclass of the BasicPlan class
    that describes a high-level subscription to some online service.

    The process of creating an instance of the GoldPlan class must be the same
    as the process of creating an instance of the BasicPlan class.

    The GoldPlan class must have seven attributes:
        can_stream — attribute with value True
        can_download — attribute with value True
        has_SD — attribute with value True
        has_HD — attribute with value True
        has_UHD — attribute with value True
        num_of_devices — attribute with value 4
        price — attribute with value $15.99

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of classes, it can
    be arbitrary.
'''


class BasicPlan:
    """
    Class representing a basic subscription to an online service.

    This class defines the features and pricing for a basic plan, including
    streaming, downloading, and standard definition support.
    """

    can_stream: bool = True
    can_download: bool = True
    has_SD: bool = True
    has_HD: bool = False
    has_UHD: bool = False
    num_of_devices: int = 1
    price: str = '8.99$'


class SilverPlan(BasicPlan):
    """
    Class representing a mid-level subscription to an online service.

    Inherits from BasicPlan and adds high-definition support and support
    for more devices.
    """

    has_HD: bool = True
    num_of_devices: int = 2
    price: str = '12.99$'


class GoldPlan(BasicPlan):
    """
    Class representing a high-level subscription to an online service.

    Inherits from BasicPlan and adds high-definition and ultra-high-definition
    support, as well as support for more devices.
    """

    has_HD: bool = True
    has_UHD: bool = True
    num_of_devices: int = 4
    price: str = '15.99$'
