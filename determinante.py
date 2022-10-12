import numpy as np


def det2(matriz):
    det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    return det


def det3(matriz):
    det = matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[0][1] * matriz[1][2] * matriz[2][0] + \
          matriz[0][2] * matriz[1][0] * matriz[2][1] - (matriz[0][2] * matriz[1][1] * matriz[2][0] + \
          matriz[0][0] * matriz[1][2] * matriz[2][1] + matriz[0][1] *
          matriz[1][0] * matriz[2][2])
    return det


def det4(matriz, linha):
    matriz1 = np.delete(matriz, linha, axis=0)
    matriz1 = del_coluna(matriz1, 0)

    matriz2 = np.delete(matriz, linha, axis=0)
    matriz2 = del_coluna(matriz2, 0)

    matriz3 = del_linha(matriz, 2)
    matriz3 = del_coluna(matriz3, 0)

    matriz4 = del_linha(matriz, 3)
    matriz4 = del_coluna(matriz4, 0)

    det = pow(-1, 2) * matriz[0][0] * det3(matriz1) + pow(-1, 3) * matriz[1][0] * det3(matriz2) \
          + pow(-1, 4) * matriz[2][0] * det3(matriz3) + pow(-1, 5) * matriz[3][0] * det3(matriz4)
    return det


def del_linha(matriz, linha):
    return np.delete(matriz, (linha), axis=0)


def del_coluna(matriz, coluna):
    return np.delete(matriz, (coluna), axis=1)

##if det == 0:
   ##print("A matriz não pode ser invertida")

def inversa2(matriz):
    aux = matriz[0][0]
    ##return [[m[1][1]/determinant, -1*m[0][1]/determinant],
    ## [-1*m[1][0]/determinant, m[0][0]/determinant]]
    ## analisar esse código q eu acabei de encontrar, parece mais clean(https://stackoverflow.com/questions/68304934/python-creating-inverse-matrix-without-numpy)
    matriz[0][0] = matriz[1][1] / "determinante"
    matriz[1][1] = aux / "determinante"
    matriz[0][1] = -(matriz[0][1] / "determinante")
    matriz[1][0] = -(matriz[1][0] / "determinante")
    return matriz


def inversa3(matriz):
    nova_matriz = []
    nova_matriz[0][0] = (det2(matriz[[1][1], [1][2], [2][1], [2][2]]) / det3(matriz))
    nova_matriz[0][1] = -(det2(matriz[[2][1], [2][2], [0][1], [0][2]]) / det3(matriz))
    nova_matriz[0][2] = (det2(matriz[[0][1], [0][2], [1][1], [1][2]]) / det3(matriz))
    nova_matriz[1][0] = -(det2(matriz[[1][2], [0][1], [2][2], [2][0]]) / det3(matriz))
    nova_matriz[1][1] = (det2(matriz[[2][2], [2][0], [0][2], [0][0]]) / det3(matriz))
    nova_matriz[1][2] = -(det2(matriz[[0][2], [0][0], [1][0], [1][2]]) / det3(matriz))
    nova_matriz[2][0] = (det2(matriz[[1][0], [1][1], [2][1], [2][0]]) / det3(matriz))
    nova_matriz[2][1] = -(det2(matriz[[2][0], [2][1], [0][0], [0][1]]) / det3(matriz))
    nova_matriz[2][2] = (det2(matriz[[0][0], [0][1], [1][1], [1][1]]) / det3(matriz))
    ##se essa porra funcionar eu fico em choque
    ##n sei chamar essa matriz de volta
    return nova_matriz
def inversa4(matriz):

## talvez isso seja a resposta para todos os nossos problemas (https://www.codegrepper.com/code-examples/python/matrix+inverse+python+without+numpy)
def m_base2(matriz):
    ##bebeto me ensinou a fzr, mas eu n faço ideia pq envolve resolver sistema de equações