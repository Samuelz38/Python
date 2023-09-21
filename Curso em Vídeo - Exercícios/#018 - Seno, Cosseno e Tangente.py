'''import math
A = int(input('Qual o ângulo:'))
S = math.sin(math.radians(A))
C = math.cos(math.radians(A))
T = math.tan(math.radians(A))
print('O SENO vale{:.2f}\nO COS vale {:.2f}\nE a TANGENTE vale {:.2f}'.format(S, C, T))'''

from math import radians, sin, cos, tan
A = int(input('Qual o ângulo:'))
S = sin(radians(A))
C = cos(radians(A))
T = tan(radians(A))
print('O SENO vale {:.2f} \nO COS vale {:.2f} \nE a TANGENTE vale {:.2f}'.format(S, C, T))
