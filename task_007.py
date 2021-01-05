def fact(n):
    for i in range(1, n + 1):
        global rez
        rez = rez * i
        if i == n:
            break
        yield i


n = int(input())
rez = 1
print(f'{n}! = ', end='')
for el in fact(n):
    print(f'{el}', end=' * ')

print(f'{n} = {rez}')
