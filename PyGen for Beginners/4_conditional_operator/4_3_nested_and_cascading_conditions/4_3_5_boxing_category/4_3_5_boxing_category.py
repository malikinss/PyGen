'''
TODO:
    The weight of an amateur boxer is known (an integer).

    It is known that the weight is such that the boxer can be assigned to
    one of three weight categories:
        Lightweight - up to 60 kg (inclusive);
        First welterweight - up to 64 kg (inclusive);
        Welterweight - up to 69 kg (inclusive).

    Write a program that determines in which category the given boxer
    will compete.
'''
x = int(input())

if x < 60:
    print('Lightweight')
elif x < 64:
    print('First welterweight')
else:
    print('Welterweight')
