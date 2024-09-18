'''
TODO:
    Mad Titan Thanos has collected all 6 Infinity Stones and intends
    to destroy half the population of the Universe with a snap of his fingers.

    However, if the population of the Universe is an odd number, the Titan
    will show mercy and round the number of survivors up.

    Help the Avengers count the number of survivors.

    The input is an integer n - the population of the Universe.

    The program must output one number - the number of survivors.
'''
# Input: population of the Universe
population: int = int(input("Enter the population of the Universe: "))

# Calculate the number of survivors
survivors: int = (population + 1) // 2

# Output the result
print(survivors)
