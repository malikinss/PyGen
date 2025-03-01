'''
TODO:
    You have a list of names, which contains names in Russian.

    Complete the code below so that it prints all names that begin with
    the letters A and M (regardless of case) and have a length greater
    than 4.

    Names must be in lexicographic order, separated by a space, each with
    a capital letter.

NOTE:
    The initial part of the answer looks like this:
        Adelina Eileen Alexander ...

    It is convenient to use the map() and filter() functions in
    the problem.
'''
from typing import List


def filter_names_by_conditions(
    names: List[str], min_length: int, letters: List[str]
) -> List[str]:
    """
    Filter names by length and starting letter.

    Args:
        names (List[str]): List of names to filter.
        min_length (int): Minimum length of names to include.
        letters (List[str]): List of starting letters to include.

    Returns:
        List[str]: List of filtered names, sorted and capitalized.
    """
    # Filter names by length and starting letter, then capitalize and sort
    return sorted([
        name.capitalize()
        for name in names
        if len(name) > min_length and name[0].lower() in letters
    ])


names = [
    'ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья',
    'семён', 'Никита', 'маргарита', 'Василиса', 'Кирилл', 'александр',
    'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём',
    'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк',
    'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин',
    'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр',
    'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей',
    'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор', 'Ника', 'анна',
    'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина',
    'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна',
    'Демид', 'амелия', 'Элина', 'Арсен', 'евгений', 'мадина', 'дарина',
    'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания',
    'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава',
    'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид'
]

result = filter_names_by_conditions(names, 4, ['а', 'м'])
print(*result)
