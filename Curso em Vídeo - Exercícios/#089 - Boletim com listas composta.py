lista = list()
dados = list()
contador = 0
while True:
    dados.append(input('Nome:'))
    dados.append(float(input('NOTA 1:')))
    dados.append(float(input('NOTA 2:')))
    lista.append(dados[:])
    dados.clear()
    escolha = input('Deseja continuar [S/N]?')[0].upper()
    contador += 1
    if escolha == 'N':
        break
    if escolha != 'S':
        while True:
            print('\033[0;31mERRO!!!')
            print('Só é possível selecionar s ou n.\033[m')
            escolha = input('Deseja continuar [S/N]?')[0].upper()
            if escolha == 'S':
                break

print('-=' * 35)

print('NO.  NOME       MÉDIA')
print('-' * 70)
for p, l in enumerate(lista):
    print(f'{p}    {lista[p][0]}      {(lista[p][1] + lista[p][2]) / 2} ')

while True:
    n = int(input('\033[1;37mMostrar notas de qual aluno? (999 interrompe):\033[m'))
    if n == 999:
        print('\033[0;33mPROCESSO FINALIZADO...\033[m')
        break
    elif n <= len(lista) - 1:
        print(f' As notas de {lista[n][0]} são {lista[n][1]} e {lista[n][2]}')