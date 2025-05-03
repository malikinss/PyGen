'''
TODO:
    Implement a Vector class whose instance represents a vector of arbitrary
    dimension.

    An instance of the Vector class must be created based on its own
    coordinates:
        a = Vector(1, 2, 3)
        b = Vector(3, 4, 5)
        c = Vector(5, 6, 7, 8)

    As an informal string representation, a vector must have its own
    coordinates enclosed in parentheses:
        print(a) # (1, 2, 3)
        print(b) # (3, 4, 5)
        print(c) # (5, 6, 7, 8)

    Vectors must support addition, subtraction, product, and normalization
    operations among themselves:
        print(a + b) # (4, 6, 8)
        print(a - b) # (-2, -2, -2)
        print(a * b) # 1*3 + 2*4 + 3*5 = 26
        print(c.norm())
        # sqrt(5**2 + 6**2 + 7**2 + 8**2) = sqrt(174) = 13.19090595827292

    as well as equality and inequality comparison operations:
        print(a == Vector(1, 2, 3)) # True
        print(a == Vector(4, 5, 6)) # False

    When attempting to perform any operation with vectors of different
    dimensions, a ValueError exception should be raised with the text:
        Vectors must have equal length
'''
