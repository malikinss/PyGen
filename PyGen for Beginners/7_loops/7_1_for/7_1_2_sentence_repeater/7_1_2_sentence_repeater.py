'''
TODO:
    Given a sentence and the number of times it must be repeated.
    Write a program that repeats the given sentence as many times as needed.
'''

given_sentence = input()

how_many_times = int(input())

for _ in range(how_many_times):
    print(given_sentence)
