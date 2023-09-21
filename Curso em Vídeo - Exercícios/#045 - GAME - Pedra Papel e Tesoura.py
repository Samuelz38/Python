from time import sleep
from random import choice
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
num = int(input('Qual a sua jogada?'))
PEDRA = 0
PAPEL = 1
TESOURA = 2
lista = [PEDRA, PAPEL, TESOURA]
sleep(1.0)
print('JO')
sleep(1.0)
print('KEN')
sleep(1.0)
print('PO')
sleep(1.0)
print('-=' * 25)
#----------------------- VITORIAS
escolha = choice(lista)
if num > escolha and escolha == PEDRA:
    print('Computador jogou pedra')
    print('jogador jogou papel')
    print('-='*25)
    print('JOGADOR VENCEU')
elif num > escolha and escolha == PAPEL:
    print('Computador jogou papel')
    print('jogador jogou tesoura')
    print('-=' * 25)
    print('JOGADOR VENCEU')
elif num < escolha and escolha == TESOURA:
    print('Computador jogou tesoura')
    print('jogador jogou pedra')
    print('-=' * 25)
    print('JOGADOR VENCEU')
# -------------------------- DERROTAS
elif num < escolha and escolha == PAPEL:
    print('Computador jogou papel')
    print('jogador jogou pedra')
    print('-=' * 25)
    print('COMPUTADOR VENCEU')

elif num < escolha and escolha == TESOURA:
    print('Computador jogou tesoura')
    print('jogador jogou papel')
    print('-=' * 25)
    print('COMPUTADOR VENCEU')

elif num > escolha and escolha == PEDRA:
    print('Computador jogou pedra')
    print('jogador jogou tesoura')
    print('-=' * 25)
    print('COMPUTADOR VENCEU')

elif num == escolha and escolha == PEDRA:
    print('Computador jogou pedra')
    print('jogador jogou pedra')
    print('-=' * 25)
    print('EMPATE')

elif num == escolha and escolha == PAPEL:
    print('Computador jogou papel')
    print('jogador jogou papel')
    print('-=' * 25)
    print('EMPATE')

elif num == escolha and escolha == TESOURA:
    print('Computador jogou tesoura')
    print('jogador jogou tesoura')
    print('-=' * 25)
    print('EMPATE')



elif num == 3 or num == 4 or num == 5 or num == 6 or num == 7 or num == 8 or num == 9:
    print('ERRO')
    print('DIGITE O NUMERO CORRETO')
    print('REINICIE O PROGRAMA')

