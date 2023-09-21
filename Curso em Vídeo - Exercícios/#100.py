import random
numeros = list()
lis2 = list()
def sorteia(lst):
    pos = 0
    while pos < 5:
        num = random.randint(0, 5)
        lst.append(num)
        pos += 1



def somaPar(lst2):
    pos = 0
    while pos < 5:
        if lst2[pos] % 2 == 0:
            lis2.append(lst2[pos])
    
    

sorteia(numeros)
print(numeros)
somaPar(numeros)
print(lis2)
