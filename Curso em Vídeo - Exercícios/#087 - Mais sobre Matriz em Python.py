matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spaar = mai = scol = 0
for l in range(0, 3):
    for c in range(0 , 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} , {c} ]:'))
print('-=' * 20)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]} ]', end= '')
        if matriz[l][c] % 2 == 0:
            spaar += matriz[l][c]
    print()
print('-=' * 20)
print(f'A soma dos valores pares é {spaar}')

for l in range(0, 3):
    scol += matriz[l][2]

print(f'A soma da terceira colana é {scol}')

for c in range(0, 3):
    if mai == 0:
        mai = matriz[1][c]
    elif mai < matriz[1][c]:
        mai = matriz[1][c]

print(f'O maior numero da linha 1 é {mai}')
print()