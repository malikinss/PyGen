'''
TODO:
    Using inheritance and the diagram below, build a hierarchy of empty
    classes that describe geometric shapes:

        Shape
        |-- Circle
        |__ Polygon
            |-- Quadrilateral
            |   |__ Parallelogram
            |       |__ Rectangle
            |           |__ Square
            |__ Triangle
                |-- IsoscelesTriangle
                |__ EquilateralTriangle
'''


class Shape:
    """
    Base class for all geometric shapes.

    This class serves as the root of the shape hierarchy, encompassing all
    types of geometric shapes including circles and polygons.
    """
    pass


class Circle(Shape):
    """
    Class representing a circle.

    Inherits from Shape and represents a round geometric shape defined by
    a radius.
    """
    pass


class Polygon(Shape):
    """
    Base class for polygons.

    Inherits from Shape and serves as the parent class for polygonal shapes
    such as quadrilaterals and triangles.
    """
    pass


class Quadrilateral(Polygon):
    """
    Base class for quadrilaterals.

    Inherits from Polygon and serves as the parent class for four-sided
    polygons such as parallelograms.
    """
    pass


class Triangle(Polygon):
    """
    Base class for triangles.

    Inherits from Polygon and serves as the parent class for three-sided
    polygons such as isosceles and equilateral triangles.
    """
    pass


class Parallelogram(Quadrilateral):
    """
    Class representing a parallelogram.

    Inherits from Quadrilateral and represents a four-sided polygon with
    opposite sides equal and parallel.
    """
    pass


class Rectangle(Parallelogram):
    """
    Class representing a rectangle.

    Inherits from Parallelogram and represents a four-sided polygon with
    opposite sides equal and all angles right angles.
    """
    pass


class Square(Rectangle):
    """
    Class representing a square.

    Inherits from Rectangle and represents a four-sided polygon with all sides
    equal and all angles right angles.
    """
    pass


class IsoscelesTriangle(Triangle):
    """
    Class representing an isosceles triangle.

    Inherits from Triangle and represents a three-sided polygon with at least
    two sides of equal length.
    """
    pass


class EquilateralTriangle(Triangle):
    """
    Class representing an equilateral triangle.

    Inherits from Triangle and represents a three-sided polygon with all sides
    and angles equal.
    """
    pass
