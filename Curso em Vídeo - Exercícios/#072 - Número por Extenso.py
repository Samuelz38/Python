tupa = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'quatoze', 'quinze', 'dezesseis', 'dezesete',
        'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20:'))
    if 0 <= num <= 20:
        print(f'O numero lido foi {tupa[num]}')
    if num > 20:
        print('Tente novamente', end='.')
    if num < 0:
        break

