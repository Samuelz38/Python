tupa = ('Palmeiras', 'Internacinal', 'Fluminense', 'Corintias', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
        'São Paulo', 'Ámerica-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragatino', 'Coritiba', 'Cuiabá', 'Céara SC',
        'Átletico-GO', 'Avaí', 'Juventude')
print(f'Os primeiros cinco coloados são: {tupa[0:5]}')
print(f'Os ultimos quatro colocados são: {tupa[-4:]}')
print(f'Em ordem alfabetica: {sorted(tupa)}')
pos = tupa.index('São Paulo')

print(f'O time São Paulo está na posição: {pos}º')


