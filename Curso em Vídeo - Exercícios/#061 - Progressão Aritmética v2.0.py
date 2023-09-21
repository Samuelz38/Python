print('-=-'*20)
print('TERMO DE UM PA')
print('-=-'*20)
cont = 0
a1 = int(input('Qual o primeiro termo?'))
r = int(input('Qual a razão?'))
while (cont < 10):
    print(f'{a1}>>', end='')
    a1 = r + a1
    cont += 1
print('EXIT')