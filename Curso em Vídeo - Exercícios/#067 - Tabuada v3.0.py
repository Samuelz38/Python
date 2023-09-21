cont = num = 0
while True:
    print('-' * 45)
    num = int(input('Digite o numero para multiplicar:'))
    if num <= 0:
        break
    for c in range(1, 11):
        cont += 1
        mult = num * cont
        print(f'{num} x {cont} = {mult}')
    cont -= 10
print('Fim')