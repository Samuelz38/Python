cont = ''
maior = 0
masculino = 0
feminino = 0
while True:
    idade = int(input('Digite sua idade:'))
    if idade >= 18:
        maior += 1
    sexo = input('Sexo[M/F]:').upper()[0]
    if sexo == 'M':
        masculino += 1
    if sexo == 'F' and idade < 20:
        feminino += 1

    cont = input('Deseja continuar?[S/N]').upper()
    if cont == 'N':
        break
print(f'Total de Pessoas de Maior {maior}')
print(f'Total de homens cadastrados {masculino}')
print(f'Total de mulheres abaixo dos 20: {feminino}')
