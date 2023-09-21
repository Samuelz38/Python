'''from random import shuffle
E = input('DIGITE O NOME:')
V = input('DIGITE O NOME:')
Q = input('DIGITE O NOME:')
P = input('DIGITE O NOME:')
lista = [E, V, Q, P]
shuffle(lista)
print('A ordem de apresentação escolhida foi:')
print(lista)'''

import random
E = input('DIGITE O NOME:')
V = input('DIGITE O NOME:')
Q = input('DIGITE O NOME:')
P = input('DIGITE O NOME:')
lista = [E, V, Q, P]
random.shuffle(lista)
print('A ordem de apresentação escolhida foi:')
print(lista)
