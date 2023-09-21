
valor_casa = int(input('Qual o valor da casa que deseja comprar?'))
valor_salario = int(input('Qual o seu sálario?'))
tempo_anos_pagar = int(input('Em quantos anos pretende pagar?'))
prestacao_mensal = valor_salario / (tempo_anos_pagar * 12)
if prestacao_mensal >= valor_salario * 0.3:
    print('Negado')
    print('Prestaçao exede 30% ou mais do seu salario')
else:
    print('Aprovado')
