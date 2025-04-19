'''
TODO:
    Implement the User class that describes a user of some Internet resource.

    When creating an instance, the class must accept one argument:
        name — user name

    The User class must have one instance method:
        skip_ads() — a method that always returns False

    Also implement the PremiumUser class, a descendant of the User class,
    that describes a user of some Internet resource with a premium
    subscription.

    The process of creating an instance of the PremiumUser class must coincide
    with the process of creating an instance of the User class.

    The PremiumUser class must have one instance method:
        skip_ads() — a method that always returns True

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of classes, it can
    be arbitrary.
'''


class User:
    """
    Class representing a user of an internet resource.

    This class defines a basic user with a name and the ability to skip ads,
    which is disabled by default.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a User instance.

        Args:
            name: The name of the user.
        """
        self.name = name

    def skip_ads(self) -> bool:
        """
        Check if the user can skip ads.

        Returns:
            bool: Always False, indicating that the user cannot skip ads.
        """
        return False


class PremiumUser(User):
    """
    Class representing a premium user of an internet resource.

    Inherits from User and defines a user with a premium subscription,
    enabling the ability to skip ads.
    """

    def skip_ads(self) -> bool:
        """
        Check if the premium user can skip ads.

        Returns:
            bool: Always True, indicating that the premium user can skip ads.
        """
        return True
