'''
TODO:
    Artificial intelligence Anton, created by Guilfoyle, hacked a network
    of smart refrigerators.

    Now he uses them as servers for the Piebald Piper.

    Help the owner of the company find all the infected refrigerators.

    For each refrigerator there is a data line consisting of lowercase letters
    and numbers, and if the word “anton” is present in it (not necessarily
    adjacent letters, the main thing is the presence of a sequence of
    letters), then the refrigerator is infected and you need to display
    the refrigerator number, numbering starts from one.

NOTE:
    If there are no Tails, then you need to output the number 0.
'''


def find_infected_refrigerators(n: int, data: list) -> None:
    """
    Find refrigerators whose data contains the sequence "anton" as
    a subsequence.

    Parameters:
    - n (int): Number of refrigerators.
    - data (list): List of data lines for each refrigerator.

    Outputs:
    - None: It prints the refrigerator numbers that are infected.
    """
    target_word = "anton"

    # Process each refrigerator's data
    for i in range(n):
        s = data[i]
        target_index = 0  # Index for the letters in "anton"

        # Try to find each letter of "anton" in order
        for char in s:
            if char == target_word[target_index]:
                target_index += 1
                if target_index == len(target_word):
                    break

        # If all letters of "anton" are found in order
        if target_index == len(target_word):
            print(i + 1, end=" ")


# Example usage
n = int(input())  # Number of refrigerators
data = [input() for _ in range(n)]  # List of refrigerator data strings

find_infected_refrigerators(n, data)
