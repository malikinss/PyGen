'''
TODO:
    Zoom challenged Flash to a fair duel in the form of a race around
    a magnetar.

    If he loses, this neutron star will charge up and destroy the world,
    so Flash decides not to take unnecessary risks and asks his
    friend Cisco Ramon if it makes sense to accept the challenge.

    Cisco received data that Zoom's speed is n, and Flash's speed is k.

    Write a program that should print Cisco's answer to Flash's question.

    If Zoom is faster than Flash, print "NO",
    and if Flash is faster than Zoom, print "YES".

    If their speeds are equal, print "Don't know".
'''
n = int(input())
k = int(input())

if n > k:
    print('NO')
elif k > n:
    print('YES')
else:
    print("Don't know")
