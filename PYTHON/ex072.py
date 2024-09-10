num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:
    r = int(input('Digite um número entre 0 e 10: '))
    if r >= 0 and r <= 10:
        break
    print('Opção inválida. ', end='')
print()
print(f'Você digitou o número {num[r]}')
