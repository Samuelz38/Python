import time
def contador(i, f , p):
    if i < f:
        if p == 0:
                p = 1
        for c in range(i, f+1, p):
            print(c)
            time.sleep(1.3)
            print(end='')
    
    if i > f:
        if p == 0:
                p = 1
        if p < 0:
            p = p * (-1)
        for r in range(i , f-1 , -p):
            print(r)
            time.sleep(1.3)
            print(end='')

time.sleep(1.3)
contador(1 , 10, 1)
print('-=' * 25)
time.sleep(1.3)
contador(10, 0 , 2)
print('-=' * 25)
time.sleep(1.3)
print('Agora sua vez de personalizar a contagem!')
time.sleep(1)

n1 = int(input('Início: '))
n2 = int(input('Fim:    '))
n3 = int(input('Passos: '))

print('-=' * 25)
print(f'Contagem de {n1} a {n2} de {n3} em {n3}')
print('-=' * 25)

contador(n1, n2, n3)