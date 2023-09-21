from datetime import date
cart = dict()
ano_atual = date.today().year
cart['Nome'] = input('Nome:')
cart['Ano_de_Nascimento'] = int(input('Ano de Nascimento:'))
cart['Carteira_de_Traba'] = int(input('Carteira de Trabalho(0 não possoí):'))
if cart['Carteira_de_Traba'] == 0:
    print('PROCESSO FINALIZADO')


else:
    cart['Ano_de_Contratação'] = int(input('Ano de Contratação:'))
    cart['Sálario'] = int(input('Sálario:'))
    if cart['Sálario'] == 0:
        while True:
            print('ERRO')
            cart['Sálario'] = int(input('Digite o valor correto'))
            if cart['Sálario'] != 0:
                break
print('-=' * 30)

print(f' - nome tem o valor: {cart["Nome"]}')
print(f' - idade tem o valor: {ano_atual - cart["Ano_de_Nascimento"]}')
print(f' - ctps tem o valor: {cart["Carteira_de_Traba"]}')
if cart['Carteira_de_Traba'] > 0:
    print(f' - contratação tem o valor {cart["Ano_de_Contratação"]}')
    print(f' - salário tem o valor {cart["Sálario"]}')
    aposentadoria = (cart["Ano_de_Nascimento"] - ano_atual) + ((cart["Ano_de_Contratação"] + 35) - ano_atual)
    print(f' - aposentadoria tem o valor {aposentadoria}')
