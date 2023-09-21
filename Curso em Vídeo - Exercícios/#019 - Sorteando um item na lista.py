'''import random
A = input('Primiro aluno:')
B = input('Segundo aluno:')
C = input('Terciro aluno:')
D = input('Quarto aluno:')
lista = [A, B, C, D]
print('O escolhido foi {}'.format(random.choice(lista)))'''

from random import choice
n1 = input('Nome do primeiro aluno:')
n2 = input('Nome do segundo aluno:')
n3 = input('Nome do terceiro aluno:')
n4 = input('Nome do quarto aluno:')
lista = [n1, n2, n3, n4]
E = choice(lista)
print('O escolhido foi {}.'.format(E))
