'''
TODO:
    During the summer holidays, Timur and the students of the BEEGEEK online
    school decided to have a rest.

    As a result, n students of the school went to rest at the seaside,
    m students went to the village, and k students went to the mountains.

    It turned out that there were x students in both the village and
    the seaside, and y students in the village and the mountains.

    No one managed to visit both the mountains and the seaside.

    Write a program to determine the number of students in the school if
    no one was able to visit all three places at once, and z students were
    writing the DWI in mathematics for admission to Moscow State University
    and did not go anywhere.

NOTE:
    - n are all the students who went to the seaside
    - m are all the students who went to the village
    - k are all the students who went to the mountains.
'''


def calculate_total_students(sea: int, village: int, mountain: int,
                             village_and_sea: int, village_and_mountain: int,
                             studied: int) -> int:
    """
    Calculates the total number of students in the school, considering
    the number of students who went to the seaside, village, and mountains.

    Args:
    sea (int): Number of students who went to the seaside.
    village (int): Number of students who went to the village.
    mountain (int): Number of students who went to the mountains.
    village_and_sea (int): Number of students who went to both the village
                            and seaside.
    village_and_mountain (int): Number of students who went to both the
                                village and mountains.
    studied (int): Number of students who stayed at home to study.

    Returns:
    int: Total number of students in the school.
    """
    # Calculating students who went only to the seaside, village, and mountain
    only_sea = sea - village_and_sea
    only_village = village - village_and_sea - village_and_mountain
    only_mountain = mountain - village_and_mountain

    # Total number of students is the sum of those who stayed at home,
    # only visited one place, and those who visited two places
    only_total = studied + only_sea + only_village + only_mountain
    total = only_total + village_and_sea + village_and_mountain

    return total


options = [
    'seaside', 'village', 'mountains',
    'village and seaside', 'village and mountains'
]

msg_template = "Enter the number of students who"

# Input values
sea = int(input(f"{msg_template} went to the {options[0]}: "))
village = int(input(f"{msg_template} went to the {options[1]}: "))
mountain = int(input(f"{msg_template} went to the {options[2]}: "))

village_and_sea = int(input(f"{msg_template} went to the {options[3]}: "))
village_and_mountain = int(input(f"{msg_template} went to the {options[4]}: "))

# Students who stayed at home
studied = int(input(f"{msg_template} stayed at home to study: "))

# Calculate total students
total_students = calculate_total_students(
    sea, village, mountain,
    village_and_sea, village_and_mountain, studied
)

# Output the result
print(total_students)
