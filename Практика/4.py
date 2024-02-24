import sys

units = ['байт', 'килобайт', 'мегабайт', 'гигабайт']
total = 0

for line in sys.stdin:
    _, size, unit = line.strip('\n').split()
    total += int(size) * 1024 ** units.index(unit)

index = 0
while total > 1024 and index < 3:
    total /= 1024
    index += 1

print(f'Общий размер всех файлов: {round(total)} {units[index]}')
