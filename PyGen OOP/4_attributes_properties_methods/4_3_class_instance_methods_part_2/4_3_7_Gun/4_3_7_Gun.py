'''
TODO:
    Implement a Gun class that describes a gun.

    The class should not take any arguments when instantiated.

    The Gun class should have three instance methods:
        - shoot() — a method that prints the string:
            pif on the first call,
            paf on the second,
            pif on the third,
            paf on the fourth,
            and so on
        - shots_count() — a method that returns the current number of calls to
        the shoot() method
        - shots_reset() — a method that resets the number of calls to the
        shoot() method to zero
'''


class Gun:
    """
    A class representing a firearm with alternating shot sound simulation.

    This class models a simple gun that produces distinct sounds ('pif'
    and 'paf') on consecutive shots.

    It maintains an internal counter to track the number
    of shots fired and alternates the output based on whether the shot count
    is odd or even.

    The class is designed to be instantiated without any arguments.

    Attributes:
        counter (int): An internal counter tracking the number of shots fired,
                       starting from 0.

    Methods:
        shoot(): Prints 'pif' for odd-numbered shots and 'paf' for
        even-numbered shots, then increments the counter.
        shots_count(): Returns the current number of shots fired.
        shots_reset(): Resets the shot counter to its initial state.
    """
    PIF = 'pif'
    PAF = 'paf'

    def __init__(self) -> None:
        """
        Initialize a Gun instance with a shot counter.

        Sets up the gun with an initial shot counter value of 0, preparing it
        for alternating sound output.

        Returns:
            None
        """
        self.counter: int = 0

    def shoot(self) -> None:
        """
        Prints 'pif' or 'paf' depending on the shot count.

        Prints 'pif' on odd calls and 'paf' on even calls, incrementing the
        counter each time.

        Returns:
            None
        """
        self.counter += 1
        # Check if the shot count is even to alternate between 'pif' and 'paf'
        if self.counter % 2 == 0:
            print(self.PAF)
        else:
            print(self.PIF)

    def shots_count(self) -> int:
        """
        Returns the current number of shots fired.

        Retrieves the value of the internal counter representing the total
        number of calls to the shoot() method.

        Returns:
            int: The number of shots fired.
        """
        return self.counter

    def shots_reset(self) -> None:
        """
        Resets the shot counter to its initial state.

        Sets the internal counter back to 0 to restart the shooting sequence.

        Returns:
            None
        """
        self.counter = 0
