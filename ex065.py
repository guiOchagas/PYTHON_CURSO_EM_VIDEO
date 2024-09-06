go = False
soma = cont = media = 0
while go != True:
    num = int(input('Digite um número: '))
    print()
    go = str(input('Deseja continuar? [S/N] ')).upper()
    print()
    soma += num
    cont += 1
    media = soma / cont
    if go == 'N':
        go = True

print()
print(f'Você digitou {cont} valores, a soma entre eles é {soma} e média é {media:.2f}.')
print()
print('Até a próxima...')
