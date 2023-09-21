n1 = int(input('Digite um numero:'))
vez = 0
for c in range(1, n1+1):
    if n1 % c == 0:
        print('\033[34m', end='')
        vez += 1
    else:
        print('\033[33m', end='')
    print('{}'.format(c), end=' ')
print('\nO numero {} foi dividido {} vezes'.format(n1, vez))
if vez == 2:
    print('Primo')
else:
    print('Não é primo')
