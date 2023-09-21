cont = num = soma = todos = 0
while True:
    num = int(input('Digite um numero(999 para parar):'))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'O total de numeros é {cont} e a soma entre ele é {soma}')