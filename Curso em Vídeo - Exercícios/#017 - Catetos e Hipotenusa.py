'''from math import sqrt
op = float(input('Digite o valor do cateto oposto:'))
ad = float(input('Digite o valor do cateto adjascente:'))
c = op**2 + ad**2
print('Sua hipotenusa é {:.2f}'.format(sqrt(c)))'''

op = float(input('Coloque o comprimento do cateto oposto:'))
ad = float(input('Coloque o comprimento do cateto adjaceste:'))
c = (op**2 + ad**2)**(1/2)
print('Sua hipotenusa mede {:.2f}'.format(c))


