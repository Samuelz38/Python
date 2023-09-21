from time import sleep
def manual(a):
    help(a)

while True:
    sleep(2)
    print('~'*30)
    print('SISTEMA DE AJUDA')
    print('~'*30)
    sleep(0.7)
    qual = input('Função ou Biblioteca> ').lower()
    sleep(1)
    if qual == 'fim':
        break
    else:
        manual(qual)