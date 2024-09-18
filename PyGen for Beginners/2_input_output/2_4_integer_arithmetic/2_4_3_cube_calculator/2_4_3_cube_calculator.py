'''
TODO:
    Write a program that calculates the volume of a cube and its total surface
    area based on the entered edge length.

NOTE:
    The volume of a cube and its total surface area can be calculated using
    the formulas:
        V=a^3
        S=6a^2

    Please note that at this stage of learning we do not know about
    the exponentiation operator, so we use the definition of a number's
    power - the number is multiplied by itself the specified number of times.

    For example:
        a^4=a⋅a⋅a⋅a
'''
a = int(input())

print('Volume =', a*a*a)
print('Total surface area =', 6*(a*a))
