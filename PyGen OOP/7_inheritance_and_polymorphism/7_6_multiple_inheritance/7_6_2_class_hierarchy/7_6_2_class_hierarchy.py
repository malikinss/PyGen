'''
TODO:
    Using inheritance and the diagram below, build a hierarchy of empty
    classes:
        |-- D -|
        |      |- B
        |-- E -|  |
    H --|         |- A
        |-- F -|  |
        |      |- C
        |-- G -|
'''


class H:
    """Base class in the hierarchy."""
    pass


class D(H):
    """Class inheriting from H, parent to B."""
    pass


class E(H):
    """Class inheriting from H, parent to B."""
    pass


class F(H):
    """Class inheriting from H, parent to C."""
    pass


class G(H):
    """Class inheriting from H, parent to C."""
    pass


class B(D, E):
    """Class inheriting from D and E, parent to A."""
    pass


class C(F, G):
    """Class inheriting from F and G, parent to A."""
    pass


class A(B, C):
    """Class inheriting from B and C."""
    pass
