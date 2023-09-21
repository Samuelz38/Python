def notas(*num , sit=False):
    """ -> Descrição da funçãod notas
    :num - recebem varios parametros int para estabelecer as notas
    :sit (opcional) - mostra situação de classe ; True - para ligado e False - para desligado
    :return - retorna um dicionario com as notas classificadas 
    """
    
    num2 = list(num)
    tot = len(num) 
    num2.sort()
    maior = num2[-1]
    menor = num2[0]
    media = sum(num2) / tot
    dic = dict()
    status = ''
    
    
    if media >= 7:
        status = 'Boa'
    else:
        status = 'Ruim'
    
    
    
    if sit == False:
        dic = {'Total':tot,'Maior':maior,'Menor':menor,'Média':media}
        return dic
    elif sit == True:
        dic = {'Total':tot,'Maior':maior,'Menor':menor,'Média':media, 'Situação':status}
        return dic
    



respot = notas(5.6, 7.7, 9.6, sit=True)
print(respot)
