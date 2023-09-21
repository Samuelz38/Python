num = int(input('Digite o numero que deseja converter:'))
print('''Escolha uma das bases para conversão:'
[ 1 ] Conveter para BINARIO'
[ 2 ] Conveter para OCTAL '
[ 3 ] Conveter para HEXADECIMAL''')
escolha = int(input('Escolha:'))

if escolha == 1:
    print('Convertido BINARIO: {}'.format(bin(num)))
elif escolha == 2:
    print('Convertido OCTAL {}'.format(oct(num)))
elif escolha == 3:
    print('Convertido HEXADECIMAL'.format(hex(num)))
else:
    print('Escolha os numeros corretos!')
