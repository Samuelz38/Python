termo = int(input('Digite quantos termos deseja ver:'))
cont = 0
x = 0
x2 = 1
print(f'{x} >> {x2}', end='')

while cont <= termo:
    x3 = x + x2
    print(f' >> {x3}',end='')
    x = x2
    x2 = x3
    cont += 1
