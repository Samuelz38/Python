import random
numero_Pensado = random.randint(0,5)
numero_Escolha = int(input('Em qual número pensei? '))
if numero_Pensado == numero_Escolha:
    print(f'Você acertou!\nEu pensei no número {numero_Pensado}')
else:
    print(f'Você errou!\nEu pensei no número: {numero_Pensado} e você disse o número: {numero_Escolha}')