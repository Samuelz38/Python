def fatorial(n, show=False):
    """
    --> Calcula o fatorial de um numero.
        n: O numero a ser calculado
        show: Opcional, a opcão False vem pre-definida (false - para ocultar) , (True - para mostrar) mostra a conta feita 
        return: o fatorial de um numero
    """
    print('-'*30)
    c = 1
    for b in range(n, 0, -1):
        c *= b
    if show == False:
        return c
    elif show == True:
        for d in range (n, 0, -1):
            print(f'{d}',end=' ')
            print('x 'if d > 1 else '= ', end='')
        return c

print(help(fatorial))   
