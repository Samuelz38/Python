# equilatero - todos lados iguais
# isoceles - dois lados iguais
# escaleno = todos os lados diferentes

prime = int(input('Primeiro segmento:'))
second = int(input('Segundo segmnto:'))
thrd = int(input('Terceiro segmento:'))

#-----------------------------

ab = prime - second
ac = prime - thrd
bc = second - thrd

#------------------------------

ab2 = second + thrd
ac2 = prime + thrd
bc2 = prime + second

#------------------------------

if ab <  thrd < ab2 and ac < second < ac2 and bc < prime < bc2:
    if prime == second == thrd:
        print('EQUILATERO')
    elif prime == second or prime == thrd or second == thrd:
        print('ISOCELES')
    else:
        print('ESCALENO')
else:
    print('NÃO É TRIANGULO')
    print(''' Segundo:
|b – c| < a < b + c
|a – c| < b < a + c
|a – b| < c < a + b''')
