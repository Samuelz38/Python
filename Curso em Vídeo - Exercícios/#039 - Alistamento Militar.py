from datetime import date
ano_nascimeto = int(input('Ano de Nascimento:'))
atual = date.today().year
idade = atual - ano_nascimeto
print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimeto, idade, atual))
alistar = ano_nascimeto + 18
tempo = idade - 18

if idade > 18:
    print('Você ja deveria ter se alistado há {} anos.'.format(tempo))
    print('Seu alistamento foi em {}.'.format(alistar))
elif idade == 18:
    print('Seu alistamento é neste ano ')
else:
    print('Ainda falta {} anos para se alistar'.format(18 - idade))
    print('Seu alistamen será em {}'.format(alistar))
