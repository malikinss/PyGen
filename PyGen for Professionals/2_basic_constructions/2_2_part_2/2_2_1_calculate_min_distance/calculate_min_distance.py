'''
TODO:
    Today Timur is waiting for his friend Arthur to visit him to plan work
    on the new course "OOP in Python".

    To prepare for the meeting, Timur needs to visit two shops located near
    his house.

    There is a d1 meter long path leading from the house to the first store,
    and a d2 meter long path leads to the second store.

    There is also a path connecting the two shops to each other, d3 meters
    long.

    Write a program that calculates the minimum distance Timur will need
    to walk to visit both stores and return home.

    Timur always starts from home.

    He must visit both stores, moving only along the available three paths,
    and return home.

    At the same time, it will not bother him at all if he has to visit the
    same store or walk along the same path more than once.

    His only task is to minimize the total distance traveled.

NOTE:
    The program is supplied with 3 natural numbers — the lengths of the tracks,
    each on a separate line:
        - d1 is the length of the track connecting Timur's house and
        the first store
        - d2 is the length of the track connecting Timur's house and
        the second store
        - d3 is the length of the track connecting the shops
'''


def calculate_min_distance(d1: int, d2: int, d3: int) -> int:
    """
    Calculates the minimum distance Timur needs to walk to visit both stores
    and return home.

    Args:
        d1 (int): Length of the track connecting Timur's house and the
                  first store
        d2 (int): Length of the track connecting Timur's house and the
                  second store
        d3 (int): Length of the track connecting the shops

    Returns:
        int: Minimum distance Timur needs to walk
    """
    # Determine the shortest path to the first store from home
    home_to_first_shop = min(d1, d2)

    # Determine the shortest path between the two stores
    first_shop_to_second_shop = min(d3, d1 + d2)

    # Determine the shortest path from the second store back home
    second_shop_to_home = min(max(d2, d1), d3 + min(d1, d2))

    # Calculate the total minimum distance
    total_min_distance = (
        home_to_first_shop + first_shop_to_second_shop + second_shop_to_home
    )

    return total_min_distance
