def get_avg_lists_intersection(lst1, lst2):
    intersection = set(lst1).intersection(lst2)
    numbers = []
    for el in lst1 + lst2:
        if el in intersection:
            numbers.append(el)
    if not numbers:
        return 0
    return round(sum(numbers) / len(numbers), 1)


lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
print(get_avg_lists_intersection(lst1, lst2))

# for _ in range(10):
#     lst1 = [random.randint(1, 20) for i in range(random.randint(20, 50))]
#     lst2 = [random.randint(1, 20) for i in range(random.randint(20, 50))]
#     print(*lst1)
#     print(*lst2)
#     print(get_avg_lists_intersection(lst1, lst2))
#     print('-----------')