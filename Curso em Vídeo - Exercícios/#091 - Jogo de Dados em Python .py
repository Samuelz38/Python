from time import sleep
from random import randint
from operator import itemgetter
print('\033[0;35mEstá na hora de girar os dados!!!!!!\033[m')
sleep(1)
ranking = list()
jogo = {'\033[0;31mjogador1\033[m': randint(1, 6),
        '\033[0;34mjogador2\033[m': randint(1, 6),
        '\033[0;33mjogador3\033[m': randint(1, 6),
        '\033[1;37mjogador4\033[m': randint(1, 6)}
for k, v in jogo.items():
    print(f'O {k} tirou o valor {v}')
    sleep(1)
print('-=' * 45)
print('==RANKING DOS JOGADORES==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)
print('\033[0;35mPor hoje é so pessoal.\033[m')