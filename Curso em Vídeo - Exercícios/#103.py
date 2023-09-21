def ficha(nome, gols):  
    if nome == '':
        nome = '<desconehcido>'
    if gols == '':
        gols = 0
    print('-'*25)
    print(f'O jogador(a) {nome} fez {gols} gol(s).')

nome = input('Jogador: ')
gols = input('Gols: ')

print(ficha(nome, gols))

