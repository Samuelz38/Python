'''frase = input('Qual seu nome completo?').strip()
print('Seu nome em minusculo: {}'.format(frase.lower()))
print('Seu nome em maiusculo: {}'.format(frase.upper()))
dividido = frase.split()
n1 = (len(frase.replace(' ', '')))
n2 = (len(dividido[0]))
print('Ao todo seu nome possui {} letras e seu primeiro nome possui {} letras.'.format(n1, n2))'''''

frase = input('Qual seu nome completo?').strip()
print('Seu nome em minusculo: {}'.format(frase.lower()))
print('Seu nome em maiusculo: {}'.format(frase.upper()))
print('Ao todo seu nome possui {}'.format(len(frase) - frase.count(' ')))
print('Ao todo seu primeiro nome possui: {}'.format(frase.find(' ')))
