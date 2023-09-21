cont = 0
pos = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        pos = pos + c
        cont = cont + 1

print('Soma dos valores: {}'.format((pos)))
print('Ao todo são: {}'.format((cont)))

