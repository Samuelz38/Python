lista = list()
while True:
    n = int(input('Digiete um valor:'))
    lista.append(n)

    prox = input('Deseja continuar:[S/N]?').upper()[0]
    if prox == 'N':
        break
    while True:
        if prox != 'S':
            print('Erro')
            prox = input('Deseja continuar:[S/N]?').upper()[0]
        else:
            break


print(f'Total de numeros digitados: {len(lista)}')
print(f'Em ordem decrescente: {lista[::-1]}')
if 5 in lista:
    print('O numero 5 foi digitado na lista')
else:
    print('O numero 5 não foi digitado na lista')

