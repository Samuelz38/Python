l = float(input('Diga a largura:'))
a = float(input('Agora a altura:'))
a2 = l*a
print('Sua parede tem uma dimensão de {}x{} e sua área é de {}m², será necessario {:.2f} litros de tinta para pinta-lá'.format(l, a, a2, a2/2))
