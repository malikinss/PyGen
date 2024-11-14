'''
TODO:
    Write a program that reads a sequence of 10 integers and
    determines whether each of them is even or not.

    The program should output the string "YES" if all numbers are even
    and "NO" otherwise.
'''


def check_all_even() -> None:
    """
    Checks if all numbers in a sequence of 10 integers are even.
    Outputs "YES" if all numbers are even, otherwise outputs "NO".
    """
    for _ in range(10):
        num = int(input())

        # If any number is odd, print "NO" and exit
        if num % 2 != 0:
            print("NO")
            return

    # If the loop completes, all numbers are even
    print("YES")


# Call the function to perform the check
check_all_even()
