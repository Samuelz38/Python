D = float(input('Dias alugados:'))
R = float(input('KM rodados:'))
td = D * 60
tr = R * 0.15
print('O total a se pagar é {}'.format(td+tr))
