from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior valor é o {max(num)}')
print(f'O menor valor é o {min(num)}')
