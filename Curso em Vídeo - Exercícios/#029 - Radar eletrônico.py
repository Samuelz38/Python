velocidade = float(input('Qual a velocidade atual do seu carro? '))
if velocidade >= 81:
    multa = (velocidade - 80.0) * 7.0  
    print('Multado!!!')
    print(f'Valor a pagar: {multa:.2f}R$')
else:
    print('Tenha um bom dia')
120