n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:',))
# -------------------------------------------

soma = n1 + n2
multiplicar = n1 * n2
maior = 0
menor = 0
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
#----------------------------------------------

print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos valores
[ 5 ] sair''')
op = int(input('>>>>>> Qual a opção:'))
while op != 5:
    if op == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
        print('O maior é {} e o menor é {} '.format(maior, menor))
        print('[ 1 ] somar')
        print('[ 2 ] multiplicar')
        print('[ 3 ] maior')
        print('[ 4 ] novos valores')
        print('[ 5 ] sair')
        op = int(input('>>>>>> Qual a opção:'))
    elif op == 2:
        print('A multiplcação entre {} e {} é {}'.format(n1, n2, multiplicar))
        print('O maior é {} e o menor é {} '.format(maior, menor))
        print('[ 1 ] somar')
        print('[ 2 ] multiplicar')
        print('[ 3 ] maior')
        print('[ 4 ] novos valores')
        print('[ 5 ] sair')
        op = int(input('>>>>>> Qual a opção:'))
    elif op == 3:
        print('O maior é {} e o menor é {} '.format(maior, menor))
        print('[ 1 ] somar')
        print('[ 2 ] multiplicar')
        print('[ 3 ] maior')
        print('[ 4 ] novos valores')
        print('[ 5 ] sair')
        op = int(input('>>>>>> Qual a opção:'))
    elif op == 4:
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor:'))
        # -------------------------------------------
        soma = n1 + n2
        multiplicar = n1 * n2
        maior = 0
        menor = 0
        if n1 > n2:
            maior = n1
            menor = n2
        else:
            maior = n2
            menor = n1
        print('O maior é {} e o menor é {} '.format(maior, menor))
        print('[ 1 ] somar')
        print('[ 2 ] multiplicar')
        print('[ 3 ] maior')
        print('[ 4 ] novos valores')
        print('[ 5 ] sair')
        op = int(input('>>>>>> Qual a opção:'))