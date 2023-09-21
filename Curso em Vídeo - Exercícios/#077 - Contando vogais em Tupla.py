tuppa = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR'
         'MERCADO', 'PROGRAMADOR', 'FUTURO')
for n in tuppa:
    print(f'\nNa plavra {n} temos :', end='')
    for letra in n:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
