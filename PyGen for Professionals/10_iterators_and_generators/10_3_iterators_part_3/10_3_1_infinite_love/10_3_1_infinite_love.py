'''
TODO:
    Complete the code below so that the infinite_love variable contains an
    iterator that infinitely generates a single value, the string:
        "i love beegeek!"
'''

# Infinite iterator that generates "i love beegeek!" infinitely
infinite_love = iter(lambda: 'i love beegeek!')

# Example usage
for _ in range(5):
    print(next(infinite_love))
