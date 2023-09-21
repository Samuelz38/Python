salario = float(input('Digite seu sálario: '))
if salario > 1250:
    aumento = (salario * 0.10) + salario
    print(f'Salario de: {salario}\nTem aumento para: {aumento}')
else:
    aumento = (salario * 0.15) + salario
    print(f'Salario de: {salario}\nTem aumento para: {aumento}')