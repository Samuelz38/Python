peso = float(input('Qual é seu Peso (Kg):'))
altura = float(input('Qual é sua altura (m):'))
IMC = peso / altura ** 2
if IMC < 18.5:
    print('ABAIXO DO PESO')
elif IMC < 25:
    print('PESO IDEAL')
elif IMC < 30:
    print('SOBREPESO')
elif IMC <= 40:
    print('OBESIDDE')
else:
    print('OBESIDAE MORNIDO')