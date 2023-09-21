lista = dict()

lista['nome'] = input('Nome:')
lista['media'] = float(input('Média:'))

print(f'A média é igual a {lista["media"]}')
if lista['media'] < 7:
    print('Situação: \033[0;31mReprovado\033[m')
else:
    print('Situação: \033[0;32mAprovado\033[m')