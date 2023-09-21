a = float(input('Digite um segmento: '))
b = float(input('Digite um segundo segmento: '))
c = float(input('Digite um terceiro segmento: '))

if a > (b-c) and a < (b+c):
    if b > (a-c) and b < (a+c): 
        if c > (a-b) and c < (a+b):
            print('É um triânguilo')
        else:
            print('Não é um triângulo')
    else:
        print('Não é um triângulo')
else:
    print('Não é um triângulo')

