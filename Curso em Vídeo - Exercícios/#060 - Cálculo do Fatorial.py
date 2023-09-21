n1 = int(input('Digite um numero para\n calcular a fatorial:'))
c = n1
s = 1
while c > 0:
    s *= c
    print('Calculando {}! = {} x {} >>> {} '.format(n1, c, n1, s))
    c -= 1
