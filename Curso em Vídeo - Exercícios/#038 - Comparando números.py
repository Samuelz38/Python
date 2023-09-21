n1 = int(input('Digite o PRIMEIRO valor:'))
n2 = int(input('Digite o SEGUNDO valor'))
if n1 > n2:
    print('O maior valor é {}'.format(n1))
    print('O menor valor é {}'.format(n2))
elif n1 < n2:
    print('O maior valor é {}'.format(n2))
    print('O menor valor é {}'.format(n1))
else:
    print('Os valores são iguais')
