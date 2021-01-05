from itertools import count, cycle
i = int(input("выводим целое число: "))
for el in count(i):
    if el > 20:
        break
    else:
        print(el)

с = 0
for j in cycle("ABCDFEGIKLMNOPQRST"):
    if с > 40:
        break
    print(j)
    с += 1