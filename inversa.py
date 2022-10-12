from determinante import det2, det3, det4
import numpy as np


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
    print()
