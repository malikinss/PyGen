'''
TODO:
    Write a function number_to_words_ru(num), which takes a natural number num
    as an argument and returns its verbal description in Russian.
NOTE:
    Consider that the number 1 ≤ num ≤ 99.
'''


def number_to_words_ru(num: int) -> str:
    """
    Converts a natural number between 1 and 99 to its verbal description
    in Russian.

    Args:
        num (int): A natural number between 1 and 99.

    Returns:
        str: The verbal description of the number in Russian.
    """
    # Words for single digits
    ed = [
        'ноль', 'один', 'два', 'три', 'четыре',
        'пять', 'шесть', 'семь', 'восемь', 'девять'
    ]

    # Words for numbers 11-19
    od = [
        'одиннадцать', 'двенадцать', 'тринадцать',
        'четырнадцать', 'пятнадцать', 'шестнадцать',
        'семьнадцать', 'восемнадцать', 'девятнадцать'
    ]

    # Words for tens (10, 20, 30, etc.)
    ds = [
        'десять', 'двадцать', 'тридцать',
        'сорок', 'пятьдесят', 'шестьдесят',
        'семьдесят', 'восемьдесят', 'девяносто'
    ]

    # Numbers like 10, 20, 30, etc.
    dss = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    # Logic to convert number to words
    if num < 10:
        d = ed[num]
    elif 10 < num < 20:
        z = int(num % 10 - 1)
        d = od[z]
    elif num in dss:
        x = int(num // 10 - 1)
        d = ds[x]
    elif num > 19:
        a = int(num // 10 - 1)
        b = int(num % 10)
        d = ds[a] + ' ' + ed[b]

    return d


n = int(input("Enter a number between 1 and 99: "))
print(number_to_words_ru(n))
