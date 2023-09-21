lista = []
par = list()
impar = list()
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    prox = input('Deseja continuar?[S/N]').upper()[0]
    if prox == 'N':
        break
    while True:
        if prox != 'S':
            print('ERRO')
            prox = input('Deseja continuar?[S/N]').upper()[0]
        else:
            break

print(f'Todos os valores: {lista}')
print(f'Valores par: {par}')
print(f'Valores impar: {impar}')

