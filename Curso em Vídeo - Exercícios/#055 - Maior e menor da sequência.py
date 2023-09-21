maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa:'.format(c)))
    if c == 1:
        maior = c
        menor = c
    else:
        if peso > maior:
           maior = peso
        if peso < menor:
            menor = peso

