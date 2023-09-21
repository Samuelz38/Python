
print('='*25, 'LOJA KAIROS', '='*25)
pagar = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = float(input('Qual é a opção?'))

if op == 1:
    desconto = pagar * 0.10
    print('VALOR DA COMPRA: {}'.format(pagar))
    print('DESCONTO DE 10%')
    print('TOTAL A PAGAR: {}'.format(pagar - desconto))
elif op == 2:
    desconto = pagar * 0.05
    print('VALOR DA COMPRA: {}'.format(pagar))
    print('DESCONTO DE 10%')
    print('TOTAL A PAGAR: {}'.format(pagar - desconto))
elif op == 3:
    print('VALOR DA COMPRA: {}'.format(pagar))
    print('2X VEZES NO CARTÃO - SEM JUROS')
    print('TOTAL A PAGAR: {}'.format(pagar / 2))
elif op == 4:
    juros = pagar * 0.2
    parcelas = float(input('N° DE PARCELAS'))
    print('VALOR DA COMPRA: {}'.format(pagar))
    print('3X VEZES NO CARTÃO - COM JUROS - 20%')
    print('JUROS: {}'.format(juros))
    print('TOTAL A PAGAR: {}'.format(pagar + juros))
    print('VALOR A PAGAR POR MÊS: {}'.format((pagar + juros) / parcelas))
else:
    print(''' ERRO!
    SELECIONE A OPÇÃO CORRETA''')
