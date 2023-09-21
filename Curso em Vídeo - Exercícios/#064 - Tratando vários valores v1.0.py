n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número:'))
    soma += n
    cont += 1

print(f'Voce digitou {cont - 1} numeros e a soma entre eles é {soma - 999}')
