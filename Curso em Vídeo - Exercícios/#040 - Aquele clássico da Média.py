prime = float(input(('Primeira Nota:')))
second = float(input('Segunda Nota:'))
media = (prime + second) / 2
print('Tirando {} e {} sua média é {}'.format(prime, second, media))
if media < 5:
    print('O aluno foi REPROVADO.')
elif media <= 6.9:
    print('O aluno está de RECUPERAÇÃO.')
else:
    print('O aluno foi APROVADO.')