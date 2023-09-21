cont = 0
soma = 0
menor = 0
maior = 0
sn = 'S'
while sn == 'S':
    n = int(input('Digite um numero:'))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    sn = input('Quer continuar?[S/N]').upper()[0]

print(f'Você digitou {cont} numeros e a media entre eles é {soma/cont}')
print(f'O maior numero {maior}')
print(f'O menor  numero {menor}')