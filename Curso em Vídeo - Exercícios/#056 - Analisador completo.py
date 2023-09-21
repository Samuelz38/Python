
tot = 0
media = 0
idade_homen_velho = 0
nome_homem_maisvelho = ''
nome_mulher = 0
for c in range(1, 5):
    print('-'*15, '{}ª PESSOA'.format(c), '-'*15)
    nome = input('NOME:')
    idade = int(input('IDADE:'))
    sexo = input('SEXO [M / F]:').strip().upper()
    if c == 1 and sexo == 'M':
        idade_homen_velho = idade
        nome_homem_maisvelho = nome
    if sexo in 'M' and idade > idade_homen_velho:
        idade_homen_velho = idade
        nome_homem_maisvelho = nome

    elif sexo == 'F' and idade < 20:
        nome_mulher += 1

    media += idade
    tot += 1

print('A média da idade do grupo é {} anos'.format(media/tot))
print('O homen mais velho é {} com {} anos'.format(nome_homem_maisvelho, idade_homen_velho))
print('Mulheres com menos de 20 anos: {}'.format(nome_mulher))
