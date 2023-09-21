import random
'''quant = maior = menor = 0
x = random.randint(1, 51)
x2 = random.randint(1, 51)
x3 = random.randint(1, 51)
x4 = random.randint(1, 51)
x5 = random.randint(1, 51)
tupa = (x, x2, x3, x4, x5)

print(tupa)
print(f'Em ordem: {sorted(tupa)}')
while True:
    quant += 1
    if quant == 1:
        maior = x
        menor = x
    else:
        if x2 > maior:
            maior = x2
        if x3 > maior:
            maior = x3
        if x4 > maior:
            maior = x4
        if x5 > maior:
            maior = x5
        if x2 < menor:
            menor = x2
        if x3 < menor:
            menor = x3
        if x4 < menor:
            menor = x4
        if x5 < menor:
            menor = x5
        break
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')'''

tupa = (random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
        random.randint(1, 50))
print('Os numeros gerados foram:', end='')
for n in tupa:
    print(f'{n}', end=' ')
print(f'\nMaior valor: {max(tupa)} ')
print(f'Menor valor: {min(tupa)}')
