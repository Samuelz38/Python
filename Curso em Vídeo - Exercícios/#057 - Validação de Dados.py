sexo = input('Informe seu sexo:').strip().upper()[0]
if sexo not in 'M' or 'F':
    while sexo != 'M' and 'F':
        sexo = input('Dados Invlidos. Digite o valor correto: ').strip().upper()

print('Dados armazenados')
