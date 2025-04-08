'''
TODO:
    Implement a FoodInfo class that describes the nutritional value of foods.

    When instantiating, the class must accept three arguments in the following
    order:
        - proteins — the amount of protein in grams
        - fats — the amount of fat in grams
        - carbohydrates — the amount of carbohydrates in grams

    An instance of the FoodInfo class must have three attributes:
        - proteins — the amount of protein in grams
        - fats — the amount of fat in grams
        - carbohydrates — the amount of carbohydrates in grams

    And the following formal string representation:
        FoodInfo(
            <amount of protein>, <amount of fat>, <amount of carbohydrates>
        )

    Also, instances of the FoodInfo class must support the addition operation
    between themselves using the + operator, the result of which must be a new
    instance of the FoodInfo class with the total amount of proteins, fats,
    and carbohydrates of the original instances.

    Finally, an instance of the FoodInfo class must support the operations of
    multiplication, division, and integer division by n using the *, /,
    and // operators, respectively:
        - the result of multiplication must be a new instance of the FoodInfo
          class, the number of proteins, fats, and carbohydrates of which is
          multiplied by n
        - the result of division must be a new instance of the FoodInfo class,
          the number of proteins, fats, and carbohydrates of which is divided
          by n
        - the result of integer division must be a new instance of
          the FoodInfo class, the number of proteins, fats, and carbohydrates
          of which is divided by n

NOTE:
    We will consider instances of the int and float classes as numbers.

    We will also guarantee that an instance of the FoodInfo class is always
    divisible by a non-zero number.

    If the object with which the arithmetic operation is performed is
    incorrect, the method implementing this operation must return
    the NotImplemented constant.

    There are no restrictions regarding the implementation of the FoodInfo
    class, it can be arbitrary.
'''
from typing import Union


class FoodInfo:
    """
    A class representing the nutritional value of food.
    """

    def __init__(
        self, proteins: float, fats: float, carbohydrates: float
    ) -> None:
        """
        Initialize FoodInfo with nutritional values.

        Args:
            proteins (float): Amount of protein in grams.
            fats (float): Amount of fat in grams.
            carbohydrates (float): Amount of carbohydrates in grams.
        """
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self) -> str:
        """
        Formal string representation of the FoodInfo.

        Returns:
            str: Representation like 'FoodInfo(10, 20, 30)'.
        """
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"

    def __add__(
        self, other: 'FoodInfo'
    ) -> 'Union[FoodInfo, NotImplemented]':  # type: ignore
        """
        Add two FoodInfo instances.

        Args:
            other (FoodInfo): Another FoodInfo instance to add.

        Returns:
            FoodInfo: New instance with summed nutritional values.
            NotImplemented: If other is not a FoodInfo instance.
        """
        if isinstance(other, FoodInfo):
            proteins = self.proteins + other.proteins
            fats = self.fats + other.fats
            carbohydrates = self.carbohydrates + other.carbohydrates
            return FoodInfo(proteins, fats, carbohydrates)
        return NotImplemented

    def __mul__(
        self, n: Union[int, float]
    ) -> 'Union[FoodInfo, NotImplemented]':  # type: ignore
        """
        Multiply FoodInfo by a scalar.

        Args:
            n (int | float): Scalar to multiply by.

        Returns:
            FoodInfo: New instance with scaled nutritional values.
            NotImplemented: If n is not a number.
        """
        if isinstance(n, (int, float)):
            proteins = self.proteins * n
            fats = self.fats * n
            carbohydrates = self.carbohydrates * n
            return FoodInfo(proteins, fats, carbohydrates)
        return NotImplemented

    def __rmul__(
        self, n: Union[int, float]
    ) -> 'Union[FoodInfo, NotImplemented]':  # type: ignore
        """
        Right multiply FoodInfo by a scalar (n * FoodInfo).

        Args:
            n (int | float): Scalar to multiply by.

        Returns:
            FoodInfo: New instance with scaled nutritional values.
            NotImplemented: If n is not a number.
        """
        return self.__mul__(n)

    def __truediv__(
        self, n: Union[int, float]
    ) -> 'Union[FoodInfo, NotImplemented]':  # type: ignore
        """
        Divide FoodInfo by a scalar.

        Args:
            n (int | float): Scalar to divide by.

        Returns:
            FoodInfo: New instance with divided nutritional values.
            NotImplemented: If n is not a number.
        """
        if isinstance(n, (int, float)):
            proteins = self.proteins / n
            fats = self.fats / n
            carbohydrates = self.carbohydrates / n
            return FoodInfo(proteins, fats, carbohydrates)
        return NotImplemented

    def __floordiv__(
        self, n: Union[int, float]
    ) -> 'Union[FoodInfo, NotImplemented]':  # type: ignore
        """
        Integer divide FoodInfo by a scalar.

        Args:
            n (int | float): Scalar to integer divide by.

        Returns:
            FoodInfo: New instance with integer-divided nutritional values.
            NotImplemented: If n is not a number.
        """
        if isinstance(n, (int, float)):
            proteins = self.proteins // n
            fats = self.fats // n
            carbohydrates = self.carbohydrates // n
            return FoodInfo(proteins, fats, carbohydrates)
        return NotImplemented
