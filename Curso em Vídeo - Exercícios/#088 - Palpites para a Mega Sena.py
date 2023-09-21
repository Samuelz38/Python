from time import sleep
from random import randint
lista = list()
jogos = list()
print('-' * 30)
print('JOGO DA MEGA SENA')
print('-' * 30)
sleep(1.2)
tot = 1
n = int(input('Quantos jogos voce deseja sortear?'))

while tot <= n:
    cont = 0
    while True:
        sorteio = randint(1, 60)
        if sorteio not in lista:
            lista.append(sorteio)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-' * 25)
print(f'PROCESSANDO OS {n} JOGOS')
print('-' * 25)

for i, l in enumerate(jogos):
    print(f'JOGO {i+1}: {l}')