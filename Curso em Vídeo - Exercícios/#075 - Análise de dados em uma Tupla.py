tupa = (int(input('Digite um numero:')), int(input('Digite segundo numero:')), int(input('Digite terceiro numero:')),
        int(input('Digite quarto numero:')), int(input('Digite quinto numero:')))


print(f'O numero nove apareceu: {tupa.count(9)} vezes')

if 3 in tupa:
    print(f'O valor 3 foi digitado na posição: {tupa.index(3) + 1}')
else:
    print('O número 3 não foi indetificado.')

for c in tupa:
    if c % 2 == 0:
        print(f'{c} par ')

