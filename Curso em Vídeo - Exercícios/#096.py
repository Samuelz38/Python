def areaR(L , C):
    A = L * C
    print(f'Largura = {L} '' \n' f'Comprinto = {C}' '\n' f'A área de um terreno {L}x{C} é {A:.2f}m².')


print('-' * 25)
print('CONTROLE DE TERRENO')
print('-' * 25)

compr = float(input('Comprimento(m): '))
larg  = float(input('Largura(m): '))

areaR(larg, compr)
