'''
TODO:
    Implement a Gun class that describes a gun.

    The class should not take any arguments when instantiated.

    The Gun class should have one instance method:
        - shoot() — a method that prints the string:
            pif on the first call,
            paf on the second,
            pif on the third,
            paf on the fourth,
            and so on.
'''
PIF = 'pif'
PAF = 'paf'


class Gun:
    """
    A class representing a firearm with alternating shot sound simulation.

    This class models a simple gun that produces distinct sounds ('pif'
    and 'paf') on consecutive shots.

    It maintains an internal counter to track the number of shots fired and
    alternates the output based on whether the shot count is odd or even.

    The class is designed to be instantiated without any arguments.

    Attributes:
        counter (int): An internal counter tracking the number of shots fired,
                       starting from 1.

    Methods:
        shoot(): Prints 'pif' for odd-numbered shots and 'paf' for
        even-numbered shots, then increments the counter.
    """

    def __init__(self) -> None:
        """
        Initialize a Gun instance with a shot counter.

        Sets up the gun with an initial shot counter value of 1, preparing it
        for alternating sound output.

        Returns:
            None
        """
        self.counter: int = 1

    def shoot(self) -> None:
        """
        Prints 'pif' or 'paf' depending on the shot count.

        Prints 'pif' on odd calls and 'paf' on even calls, incrementing the
        counter each time.

        Returns:
            None
        """
        # Check if the shot count is even to alternate between 'pif' and 'paf'
        if self.counter % 2 == 0:
            print('paf')
        else:
            print('pif')

        self.counter += 1
