from determinante import det2, det3, det4
from funcoes import transposta, deletaColuna, deletaLinha
import numpy as np


def inversa2(matriz):
    if det2(matriz) == 0:
        return print("Sua matriz não possui inversa!")

    matrizSaida = []
    matrizSaida2 = []
    aux = []

    sub_matriz1 = deletaLinha(matriz, 0)
    sub_matriz1 = deletaColuna(sub_matriz1, 0)

    sub_matriz2 = deletaLinha(matriz, 0)
    sub_matriz2 = deletaColuna(sub_matriz2, 1)

    sub_matriz3 = deletaLinha(matriz, 1)
    sub_matriz3 = deletaColuna(sub_matriz3, 0)

    sub_matriz4 = deletaLinha(matriz, 1)
    sub_matriz4 = deletaColuna(sub_matriz4, 1)

    lista = [sub_matriz1, sub_matriz2, sub_matriz3, sub_matriz4]

    exp1 = 0
    exp2 = 0
    aux2 = []

    for k in lista:
        if exp2 == 2:
            exp2 = 0
            exp1 += 1
        aux2.append(pow(-1, exp1 + exp2 + 2) * k[0][0])
        matrizSaida.append(aux2[:])
        aux2.clear()
        exp2 += 1

    for inversa in matrizSaida:
        aux.append(inversa[0])
    matrizSaida2.append([aux[0], aux[1]])
    matrizSaida2.append([aux[2], aux[3]])
    inversa=np.array(transposta(matrizSaida2)) * float(1/det2(matriz))
    return inversa


def inversa3(matriz):
    if det3(matriz) == 0:
        return print("Sua matriz não possui inversa")

    matrizSaida1 = []
    matrizSaida2 = []
    aux2 = []

    lista = []
    aux1 = []
    count1 = 0
    count2 = 0
    count3 = 0
    for inversa in range(9):
        inversa = deletaLinha(matriz, count1)
        inversa = deletaColuna(inversa, count2)
        count2 += 1
        if count2 == 3:
            count1 += 1
            count2 = 0
        for j in inversa:
            aux1.append(list(j))
            count3 += 1
            if count3 == 2:
                lista.append(aux1[:])
                aux1.clear()
                count3 = 0
    for k, inversa in enumerate(lista):
        lista[k] = det2(inversa)

    exp1 = 0
    exp2 = 0
    aux3 = []
    for j in lista:
        if exp2 == 3:
            exp2 = 0
            exp1 += 1
        aux3.append(pow(-1, exp1 + exp2 + 2) * j)
        matrizSaida1.append(aux3[:])
        aux3.clear()
        exp2 += 1

    for inversa in matrizSaida1:
        aux2.append(inversa[0])

    matrizSaida2.append([aux2[0], aux2[1], aux2[2]])
    matrizSaida2.append([aux2[3], aux2[4], aux2[5]])
    matrizSaida2.append([aux2[6], aux2[7], aux2[8]])

    inversa = np.array(transposta(matrizSaida2)) * float(1/det3(matriz))
    return inversa


def inversa4(matriz):
    matrizSaida1 = []
    matrizSaida2 = []
    aux1 = []
    aux2 = []

    lista = []
    count1 = 0
    count2 = 0
    count3 = 0
    for inversa in range(16):
        m = deletaLinha(matriz, count2)
        m = deletaColuna(m, count1)
        count2 += 1
        if count2 == 4:
            count1 += 1
            count2 = 0
        for j in m:
            aux1.append(list(j))
            count3 += 1
            if count3 == 3:
                lista.append(aux1[:])
                aux1.clear()
                count3 = 0
    for k, inversa in enumerate(lista):
        lista[k] = det3(inversa)

    exp1 = 0
    exp2 = 0
    aux3 = []
    for j in lista:
        if exp2 == 4:
            exp2 = 0
            exp1 += 1
        aux3.append(pow(-1, exp1 + exp2 + 2) * j)
        matrizSaida1.append(aux3[:])
        aux3.clear()
        exp2 += 1

    for inversa in matrizSaida1:
        aux2.append(inversa[0])

    matrizSaida2.append([aux2[0], aux2[1], aux2[2], aux2[3]])
    matrizSaida2.append([aux2[4], aux2[5], aux2[6], aux2[7]])
    matrizSaida2.append([aux2[8], aux2[9], aux2[10], aux2[11]])
    matrizSaida2.append([aux2[12], aux2[13], aux2[14], aux2[15]])

    inversa = np.array(transposta(matrizSaida2)) * float(1 / det4(matriz))
    return inversa
