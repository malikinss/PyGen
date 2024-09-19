'''
TODO:
    Write a program that, given the user's age, tells what age group
    he belongs to:
        up to 13 (inclusive) - childhood;
        from 14 to 24 (inclusive) - youth;
        from 25 to 59 (inclusive) - maturity;
        from 60 (inclusive) - old age.
'''
user_age = int(input())

if user_age <= 13:
    print('childhood')
else:
    if user_age <= 24:
        print('youth')
    else:
        if user_age <= 59:
            print('maturity')
        else:
            print('old age')
