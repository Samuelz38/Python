km = int(input('Quantos km possui a sua viagem?'))
if km <= 200:
    p = 0.50*km
    print('o TOTAL a se pagar pela viagem é: {} RS'.format(p))
else:
    ty5 = 0.45*km
    print('O valor de sua viagem é {} RS'.format(ty5))
print('Pague o aluguel')