import numpy as np
from determinante import det2, det3, det4
from inversa import inversa2, inversa3, inversa4
from mudaBase import mudaBase2, mudaBase3, mudaBase4


matriz = []
dimensao = int(input('Qual a dimensão dessa matriz? '))

if dimensao == 1:
    matriz = [12]
elif dimensao == 2:
    matriz = [[1, 2], [2, 3]]
    det = det2(matriz)
    print(matriz)
    print(det)
elif dimensao == 3:
    print('oi')
elif dimensao == 4:
    matriz = [[1, 2, 3, 4], [0, 0, 0, 0], [3, 0, -4, 2], [5, 4, 3, 2]]
    det = det4(matriz)
    print(matriz)
    print(det)
