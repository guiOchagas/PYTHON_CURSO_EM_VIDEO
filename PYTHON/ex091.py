from random import randint
from time import sleep

jogo = {'jogador_1': randint(1,6), 'jogador_2': randint(1,6), 'jogador_3': randint(1,6), 'jogador_4': randint(1,6)}
print('='*10)
print(f'   JOGO')
print('='*10)
for k, v in jogo.items():
    print(f'O {k} tirou [{v}]')
    sleep(1)

print()
print('='*10)
print(f' RESULTADO')
print('='*10)
print()
