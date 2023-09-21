import datetime
data = datetime.date.today().year
cont1 = 0
cont2 = 0
for c in range(1, 8):
    ano = int(input('Em que ano nasceu a {}ª pessoa'.format(c)))
    if data - ano >= 18:
        cont1 = cont1 + 1
    elif data - ano < 18:
        cont2 = cont2 + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont1))
print('Ao todo tivemos {} pessoas menores de idade'.format(cont2))
