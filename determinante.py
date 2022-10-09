import numpy as np

def det2(matriz):
    det = matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0]
    return det
def det3(matriz):
    det = matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[0][1]*matriz[1][2]*matriz[2][0] + \
        matriz[0][2]*matriz[1][0]*matriz[2][1] - (matriz[0][2]*matriz[1][1]*matriz[2][0] +\
        matriz[0][0]*matriz[1][2]*matriz[2][1] + matriz[0][1]*matriz[1][0]*matriz[2][2])
    return det
def det4(matriz, linha):
    matriz1 = np.delete(matriz, linha, axis=0)
    matriz1 = del_coluna(matriz1,0)

    matriz2 = np.delete(matriz, linha, axis=0)
    matriz2 = del_coluna(matriz2,0)

    matriz3 = del_linha(matriz,2)
    matriz3 = del_coluna(matriz3,0)

    matriz4 = del_linha(matriz,3)
    matriz4 = del_coluna(matriz4,0)

    det = pow(-1,2)*matriz[0][0]*det3(matriz1) + pow(-1,3)*matriz[1][0]*det3(matriz2) \
        + pow(-1,4)*matriz[2][0]*det3(matriz3) + pow(-1,5)*matriz[3][0]*det3(matriz4)
    return det

def del_linha(matriz,linha):
    return np.delete(matriz,(linha),axis=0)
def del_coluna(matriz,coluna):
    return np.delete(matriz,(coluna), axis=1)






