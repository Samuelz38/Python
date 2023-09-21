contatos = list()
maior = 0
menor = 0

while True:
    
    lista02 = list()
    nome = input('Nome: ')
    peso = int(input('Peso: '))
    lista02.append(nome)
    lista02.append(peso)
    contatos.append(lista02)    
     
    
    lista02.clear
    
    cont = input('Quer continaur?[S/N]').upper()
    if cont == 'N':
        break
    while True:
        if cont != 'S':
            print('Erro')
            cont = input('Quer continaur?[S/N]').upper()
        else:
            break

for c in contatos:
     if c[1] > maior:
         maior = c[1]
         if menor == 0:
            menor = c[1]   
     if c[1] < menor:
        menor = c[1]


print(f'Ao todo, você cadastrou {len(contatos)} pessoas.')
print(f'O maior peso foi de {maior}. Peso de', end=' ')

for p in contatos:
   if maior == p[1]:
      print(p[0])
print()
print(f'O menor peso foi: {menor}. Peso', end=' ')
for t in contatos:
    if menor == t[1]:
       print(t[0])
print()