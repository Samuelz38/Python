somma = 0
for v in range(1,7):
    VALOR = int(input('Digite um numero:'))
    if VALOR % 2 == 0:
        somma = somma + VALOR
print('Soma: {}'.format(somma))

