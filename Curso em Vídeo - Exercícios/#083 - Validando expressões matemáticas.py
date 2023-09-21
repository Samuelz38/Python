conta = input('Digite a expressão:')
expressao = []
for sim in conta:
    if sim == '(':
        expressao.append('(')
    elif sim == ')':
        if len(expressao) > 0:
            expressao.pop(0)
        else:
            expressao.append(')')
            break
    if len(expressao) == 0:
        print('Valido')
    else:
        print('Invalido')
