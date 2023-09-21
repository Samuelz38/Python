frase = input('Digite uma frase: ').strip().lower()
numero_A = frase.count('a')
A1 = frase.find('a')
AF = frase.rfind('a')
print(f'A letra "A" aparece: {numero_A}')
print(f'A primeira letra: {A1 + 1}')
print(f'A ultma letra: {AF + 1}')

 