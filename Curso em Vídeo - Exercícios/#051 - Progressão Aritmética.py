print('='*25)
print('10 TERMOS DE UMA PA')
print('='*25)

a1 = int(input('Primeiro Termo:'))
r = int(input('Razão:'))
print('{}'.format(a1), end='→→')
for c in range(1, 10):
    a1 = a1 + r
    print('{} →'.format(a1), end='→')
print('Acabou')


