from random import choice
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha = choice(lista)
palpites = 0
print('''Sou seu computador...
Tente adivinhar um numero etre 0 e 10.
Que estou pesando.''')
num = int(input('''Será que consegue adivihar?
Digite o numero:'''))

if num != escolha:
    while True:
        if num > escolha:
            num = int(input('Menos... tente outra vez:'))
        elif num < escolha:
            num = int(input('Mais... tente outra vez:'))
        palpites += 1

else:
    print('Acertou!!! Com {} palpites'.format(palpites))