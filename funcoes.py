import numpy as np
import determinante


def deletaLinha(matriz, linha):
    return np.delete(matriz, linha, axis=0)


def deletaColuna(matriz, coluna):
    return np.delete(matriz, coluna, axis=1)


def transposta(m):
    transposta = []
    x = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    for linha in x:
        transposta.append(linha)
    return transposta
    #def transposta(m):
        #transposta = list(map(lambda *i: [j for j in i], *m))
        #return transposta


def base(A, B, n):
    if n == 2:
        if determinante.det2(A) == 0 or determinante.det2(B) == 0:
            return False
        else:
            return True
    elif n == 3:
        if determinante.det3(A) == 0 or determinante.det2(B) == 0:
            return False
        else:
            return True
    elif n == 4:
        if determinante.det4(B) == 0 or determinante.det4(A):
            return False
        else:
            return True