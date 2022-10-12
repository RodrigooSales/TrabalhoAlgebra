import numpy as np
from funcoes import deletaLinha, deletaColuna

def det2(matriz):
    det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    return det


def det3(matriz):
    det = matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[0][1] * matriz[1][2] * matriz[2][0] + \
          matriz[0][2] * matriz[1][0] * matriz[2][1] - (matriz[0][2] * matriz[1][1] * matriz[2][0] + \
          matriz[0][0] * matriz[1][2] * matriz[2][1] + matriz[0][1] *
          matriz[1][0] * matriz[2][2])
    return det


def det4(matriz):
    matriz1 = deletaLinha(matriz, 0)
    matriz1 = deletaColuna(matriz1, 0)

    matriz2 = deletaLinha(matriz, 1)
    matriz2 = deletaColuna(matriz2, 0)

    matriz3 = deletaLinha(matriz, 2)
    matriz3 = deletaColuna(matriz3, 0)

    matriz4 = deletaLinha(matriz, 3)
    matriz4 = deletaColuna(matriz4, 0)

    det = pow(-1, 2) * matriz[0][0] * det3(matriz1) + pow(-1, 3) * matriz[1][0] * det3(matriz2) + pow(-1, 4) * matriz[2][0] * det3(matriz3) + pow(-1, 5) * matriz[3][0] * det3(matriz4)
    return det


