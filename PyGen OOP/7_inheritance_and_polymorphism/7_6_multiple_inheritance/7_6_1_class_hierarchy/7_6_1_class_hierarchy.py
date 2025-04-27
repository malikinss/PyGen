'''
TODO:
    Using inheritance and the diagram below, build a hierarchy of empty
    classes:
        |-- c
        |-- B
    A --|   |- E
        |-- D
'''


class A:
    """Base class in the hierarchy."""
    pass


class C(A):
    """Class inheriting from A."""
    pass


class B(A):
    """Class inheriting from A, parent to E."""
    pass


class D(A):
    """Class inheriting from A, parent to E."""
    pass


class E(B, D):
    """Class inheriting from B and D."""
    pass
