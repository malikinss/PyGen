'''
TODO:
    You have access to the variable article, which contains some multi-line
    text.

    Complete the code below so that it determines:
    - the number of lines that begin with the word Stepik (in any case);
    - the number of lines that end with three dots ... or an exclamation mark !

    and outputs two corresponding numbers, each on a separate line.

NOTE:
    A line can simultaneously satisfy both conditions.
'''
import re


def count_starts_with(text: str, pattern: str) -> int:
    """
    Counts the number of lines that start with the given value
    (case-insensitive).

    Args:
        text (str): Multi-line text.
        pattern (str): The word to check at the beginning of lines.

    Returns:
        int: Number of lines that start with the given word.
    """
    regex = rf'^{pattern}\b'
    return len(re.findall(regex, text, re.I | re.M))


def count_ends_with(text: str, pattern: str) -> int:
    """
    Counts the number of lines that end with the given pattern.

    Args:
        text (str): Multi-line text.
        pattern (str): The pattern to check at the end of lines.

    Returns:
        int: Number of lines that match the pattern.
    """
    regex = rf'{pattern}$'
    return len(re.findall(regex, text, re.M))


article = '''Stepik (до августа 2016 года Stepic) — это образовательная
платформа и конструктор онлайн-курсов!

Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android.
В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном
режиме для iOS и Android...

На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
Stepik позволяет любому зарегистрированному пользователю создавать
интерактивные обучающие уроки и онлайн-курсы, используя видео, тексты и
разнообразные задачи с автоматической проверкой и моментальной обратной связью.

Проект сотрудничает как с образовательными учреждениями, так и c
индивидуальными преподавателями и авторами.
Stepik сегодня предлагает онлайн-курсы от образовательных организаций,
а также индивидуальных авторов!

Система автоматизированной проверки задач Stepik была использована в ряде
курсов на платформе Coursera, включая курсы по биоинформатике от
Калифорнийского университета в Сан-Диего и курс по анализу данных от НИУ
«Высшая школа экономики»...

Stepik также может функционировать как площадка для проведения конкурсов и
олимпиад, среди проведённых мероприятий — отборочный этап Олимпиады НТИ
(2016—2020) (всероссийской инженерной олимпиады школьников, в рамках программы
Национальная технологическая инициатива), онлайн-этап акции Тотальный диктант
в 2017 году, соревнования по информационной безопасности StepCTF-2015...'''


print(count_starts_with(article, r'Stepik'))
print(count_ends_with(article, r'(?:\.\.\.|!)'))
