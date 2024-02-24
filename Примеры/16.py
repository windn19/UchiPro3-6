def get_avg(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)


assert get_avg([1, 2, 3, 4, 5]) == 3.0
assert get_avg([4, 4, 4]) == 4.0
assert get_avg([]) == 0
