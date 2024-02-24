def get_avg(lst):
    """
    Принимает список чисел и возвращает
    среднее арифметическое чисел этого списка
    или 0, если список пуст.
    """
    if not lst:
        return 0
    return sum(lst) / len(lst)
