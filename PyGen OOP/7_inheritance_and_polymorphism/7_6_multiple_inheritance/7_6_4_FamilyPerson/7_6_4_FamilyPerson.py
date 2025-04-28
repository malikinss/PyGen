'''
TODO:
    Use multiple inheritance to create a hierarchy of the following four
    classes.

    Try to keep code duplication to a minimum when solving this problem.

    Implement a Father class that describes a father.

    When instantiated, the class must accept one argument:
        mood — mood, defaults to the string neutral

    An instance of the Father class must have one attribute:
        mood — mood

    The Father class must have two instance methods:
        greet() — method that returns the string Hello!
        be_strict() — method that changes the value of the mood attribute to
                      the string strict

    Also implement a Mother class that describes a mother

    When instantiated, the class must accept one argument:
        mood — mood, defaults to the string neutral

    An instance of the Mother class must have one attribute:
        mood — mood

    The Mother class must have two instance methods:
        greet() — method that returns the string Hi, honey!
        be_kind() — a method that changes the value of the mood attribute to
                    the string kind

    In addition, implement the Daughter class that describes the daughter.

    When instantiating the class, it must accept one argument:
        mood — mood, by default equals to the string neutral

    An instance of the Daughter class must have one attribute:
        mood — mood

    The Daughter class must have three instance methods:
        greet() — a method that returns the string Hi, honey!
        be_kind() — a method that changes the value of the mood attribute to
                    the string kind
        be_strict() — a method that changes the value of the mood attribute to
                      the string strict

    Finally, implement the Son class that describes the son.

    When instantiating the class, it must accept one argument:
        mood — mood, by default equals to the string neutral

    An instance of the Son class must have one attribute:
        mood — mood

    The Son class must have three instance methods:
        greet() — a method that returns the string Hello!
        be_kind() — method that changes the value of the mood attribute to
                    the string kind
        be_strict() — method that changes the value of the mood attribute to
                      the string strict

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented classes are used only with correct
    data.

    There are no restrictions regarding class implementations, they can be
    arbitrary.
'''
from abc import ABC, abstractmethod


class FamilyPerson(ABC):
    """
    Abstract base class for family members with mood and behaviors.
    """

    def __init__(self, mood: str = "neutral") -> None:
        """
        Initialize with a mood.

        Args:
            mood: Initial mood, defaults to 'neutral'.
        """
        self.mood = mood

    @abstractmethod
    def greet(self) -> str:
        """
        Return a greeting.

        Returns:
            str: Greeting specific to the family member.
        """
        pass

    def be_strict(self) -> None:
        """
        Set mood to strict.
        """
        self.mood = "strict"

    def be_kind(self) -> None:
        """
        Set mood to kind.
        """
        self.mood = "kind"


class Father(FamilyPerson):
    """
    Father class inheriting from FamilyPerson.
    """

    def greet(self) -> str:
        """Return a greeting.

        Returns:
            str: Greeting 'Hello!'.
        """
        return "Hello!"


class Mother(FamilyPerson):
    """
    Mother class inheriting from FamilyPerson.
    """

    def greet(self) -> str:
        """Return a kind greeting.

        Returns:
            str: Greeting 'Hi, honey!'.
        """
        return "Hi, honey!"


class Daughter(Mother, Father):
    """
    Daughter class inheriting from Mother and Father.
    """
    pass


class Son(Father, Mother):
    """
    Son class inheriting from Father and Mother.
    """
    pass
