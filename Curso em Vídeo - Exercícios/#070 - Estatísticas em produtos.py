total = cont = quant = menor = 0
barato = ''
nuar = ''
while True:
    nome = input('Qual nome do produto?')
    pre = float(input('Preço do produto:R$'))
    quant += 1
    if quant == 1:
        menor = pre
        barato = nome
    else:
        if pre < menor:
            menor = pre
            barato = nome

    if pre > 1000:
        cont += 1
    total += pre
    nuar = input('Desseja continuar? [S/N]').upper()[0]
    if nuar == 'N':
        break
print(f'Total a pagar: {total}RS')
print(f'Total de produtos que custam mais de 1000: {cont}')
print(f'O produto com menor preço foi {barato} e ele custa {menor}')