import numpy as np

def deletaLinha(matriz, linha):
    return np.delete(matriz, linha, axis=0)

def deletaColuna(matriz, coluna):
    return np.delete(matriz, coluna, axis=1)
