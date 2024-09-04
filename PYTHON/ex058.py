from random import randint
computador = randint(0, 10)
erros = 1
print('='*40)
print('{: ^40}'.format( ' JOGO DA ADVINHAÇÃO '))
print('='*40)
print('TENTE ADVINHAR QUE NÚMERO O COMPUTADOR ESCOLHEU')
print()
jogador = int(input('Seu palpite: '))
while jogador != computador:
    jogador = int(input('Tente novamente: '))
    if jogador != computador:
        erros = erros + 1
print()
print('Acertouuu!\n\nO computador escolheu {} e você tentou {} vezes até acertar'.format(computador, erros))
