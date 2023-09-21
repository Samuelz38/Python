def voto(Ano_Nas):
    Resul = 2023 - Ano_Nas
    if Resul < 18:
        return 'NÃO VOTA'
    elif Resul >= 18:
        return 'VOTO OBRIGRATORIO'
    elif Resul >= 100:
        return 'VOTO OPCIONAL'
print('-'*30)    
total = int(input('Em que ano voce nasceu/ '))
print(f'Com {2023 - total} anos: {voto(total)}')
