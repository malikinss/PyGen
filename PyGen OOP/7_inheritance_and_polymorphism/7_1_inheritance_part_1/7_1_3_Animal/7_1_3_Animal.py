'''
TODO:
    Using inheritance and the diagram below, build a hierarchy of classes that
    describe animals:

        Animal
        |-- Fish
        |__ Bird
            |__ FlyingBird

    The Animal class must have two instance methods:
        sleep()—empty method
        eat()—empty method

    The Fish class must have one instance method:
        swim()—empty method

    The Bird class must have one instance method:
        lay_eggs()—empty method

    The FlyingBird class must have one instance method:
        fly()—empty method
'''


class Animal:
    """
    Base class for all animals.

    This class serves as the root of the animal hierarchy, defining common
    behaviors such as sleeping and eating.
    """

    def sleep(self) -> None:
        """
        Simulate the animal sleeping.

        This method represents the animal's ability to sleep.
        """
        pass

    def eat(self) -> None:
        """
        Simulate the animal eating.

        This method represents the animal's ability to consume food.
        """
        pass


class Fish(Animal):
    """
    Class representing a fish.

    Inherits from Animal and defines behaviors specific to fish,
    such as swimming.
    """

    def swim(self) -> None:
        """
        Simulate the fish swimming.

        This method represents the fish's ability to move through water.
        """
        pass


class Bird(Animal):
    """
    Class representing a bird.

    Inherits from Animal and defines behaviors specific to birds, such
    as laying eggs.
    """

    def lay_eggs(self) -> None:
        """
        Simulate the bird laying eggs.

        This method represents the bird's reproductive behavior.
        """
        pass


class FlyingBird(Bird):
    """
    Class representing a flying bird.

    Inherits from Bird and defines behaviors specific to birds capable
    of flight, such as flying.
    """

    def fly(self) -> None:
        """
        Simulate the bird flying.

        This method represents the flying bird's ability to move through
        the air.
        """
        pass
