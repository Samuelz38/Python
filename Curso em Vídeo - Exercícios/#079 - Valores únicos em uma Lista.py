lista = []

while True:
    m = int(input('Digite o Valor:'))
    if m not in lista:
        lista.append(m)
    else:
        print('Valor duplicado')

    continar = input('Deseja cotinuar?[S/N]').upper()[0]

    if continar == 'N':
        break

    while True:
        if continar != 'S':
            print('Erro')
            continar = input('Deseja cotinuar?[S/N]').upper()[0]

        else:
            break

print(sorted(lista))


