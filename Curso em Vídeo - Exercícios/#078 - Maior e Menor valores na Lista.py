lista = []
for n in range(1,6):
    lista.append(int(input(f'Digite um valor para posição {n-1}:')))
pos1 = max(lista)
pos2 = min(lista)
print(f'Valores da lista: {lista}')
print(f'O Maior valor: {pos1} e sua posição é {lista.index(max(lista))}')
print(f'O Menor valor: {pos2} e sua posiçâo é {lista.index((min(lista)))}')
