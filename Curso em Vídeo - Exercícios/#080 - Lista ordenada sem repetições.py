lista = list()
for n in range(1, 6):
    m = int(input('Digite um valor:'))
    if n == 0 or m > lista[-1]:
        lista.append(m)
        print('Adicionado no começo da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if pos <= lista[-1]:
                lista.insert(pos, n)
                print(f'Foi adicionado {pos} da lista...')
                break
            pos += 1

print(lista)
