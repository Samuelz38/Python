print('-=-'*20)
print('TERMO DE UM PA')
print('-=-'*20)
cont = 0
termo = int(input('Qual o termo da PA?'))
razao = int(input('Qual a razão?'))
total = 0
x = 10
while x != 0:
    total = total + x
    while cont < total:
        print(f'{termo}>>', end='')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    x = int(input('Deseja adicionar quantos termos?'))























while cont < 10:
    print(f'{termo}>>', end='')
    termo = termo + razao
    cont += 1

print('PAUSA')

x = int(input('Deseja adicionar quantos termos?'))
if x != 0:
    while x > 0:
        print(f'{termo}>>', end='')
        termo = termo + razao
        x -= 1