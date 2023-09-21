import random
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vito = 0
while True:
    num = int(input('Digite um numero:'))
    es = input('Escolha Impar ou Par?[I/P]').upper()[0]
    escolha = random.choice(lista)
    soma = num + escolha
    print(escolha, soma)
    if soma % 2 == 0 and es == 'P':
        print(f'{num} + {escolha} = {soma}')
        print('Par venceu')
        vito += 1


    elif soma % 2 == 1 and es == 'I':
        print(f'{num} + {escolha} = {soma}')
        print('Impar Venceu')
        vito += 1

    elif soma % 2 == 0 and es == 'I':
        print(f'{num} + {escolha} = {soma}')
        print('Par Venceu')
        print('PC VENCEU')
        break

    elif soma % 2 == 1 and es == 'P':
        print(f'{num} + {escolha} = {soma}')
        print('Impar Venceu')
        print('PC VENCEU')
        break
print(f'Voce ganhou {vito} vezes concecutivas')