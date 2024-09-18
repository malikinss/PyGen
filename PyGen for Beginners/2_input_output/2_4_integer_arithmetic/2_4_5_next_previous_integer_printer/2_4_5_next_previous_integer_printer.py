'''
TODO:
    Write a program that reads an integer and prints the next and previous
    integers for it in the following format:
        The next integer for <current number> is: <next integer>
        For <current number>, the previous integer is: <previous integer>
'''
a = int(input())

print('The next integer for', a, 'is:', a+1)
print('For', a, ',the previous integer is:', a-1)
