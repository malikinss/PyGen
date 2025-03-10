'''
TODO:
    You have access to a named tuple Person, which contains data about
    a person.

    The first element of the named tuple is the person's first and last name,
    the second is their nationality, the third is their gender, the fourth is
    their year of birth, and the fifth is their year of death.

    If the person is alive, the year of death is assumed to be 0.

    A list of persons containing these tuples is also available.

    Expand the code below using generator pipelines to print the first and
    last name of the youngest living male from Sweden.

NOTE:
    Example output:
    Goran Aslin

    It is guaranteed that there is only one person.
'''
from collections import namedtuple
from operator import attrgetter

Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

persons = [
    Person('E. M. Ashe', 'American', 'male', 1867, 1941),
    Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
    Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
    Person('Genevieve Asse', 'French', 'female', 1949, 0),
    Person('Irene Adler', 'Swedish', 'female', 2005, 0),
    Person('Sergio Asti', 'Italian', 'male', 1926, 0),
    Person('Olof Backman', 'Swedish', 'male', 1999, 0),
    Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
    Person('Dana Atchley', 'American', 'female', 1941, 2000),
    Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
    Person('Shura_Stone', 'Russian', 'male', 2000, 0),
    Person('Jon Bale', 'Swedish', 'male', 2000, 0)
]


def youngest_living_swedish_man(persons_list: list[Person]) -> str:
    """
    Find the youngest living male from Sweden using a generator pipeline.

    Args:
        persons_list (list[Person]): A list of Person named tuples.

    Returns:
        str: The full name of the youngest living Swedish male.
    """
    def is_living_swedish_man(person: Person) -> bool:
        """
        Check if a person is a living Swedish male.
        """
        is_swedish = person.nationality == 'Swedish'
        is_man = person.sex == 'male'
        is_alive = person.death == 0

        return all([is_swedish, is_man, is_alive])

    def filter_swedish_males(persons):
        return (p for p in persons if is_living_swedish_man(p))

    def find_youngest(persons):
        return max(persons, key=attrgetter('birth'))

    return find_youngest(filter_swedish_males(persons_list)).name


print(youngest_living_swedish_man(persons))
