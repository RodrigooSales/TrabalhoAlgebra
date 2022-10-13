import numpy as np
from funcoes import base

def mudancaBase(A, B, n):
    matriz = []
    valida = base(A, B, n)
    if valida == True:
        if n == 2:
            a = [[B[0][0]], B[1][0], [B[0][1], B[1][1]]]
            b = A[0]

            sistema_linear = np.linalg.solve(a, b)
            x1 = sistema_linear[0]
            y1 = sistema_linear[1]

            a = [[B[0][0], B[1][0]], [B[0][1], B[1][1]]]
            b = A[1]

            sistema_linear = np.linalg.solve(a, b)
            x2 = sistema_linear[0]
            y2 = sistema_linear[1]

            matriz = [[x1, x2], [y1, y2]]
            return matriz

        if n == 3:
            a = [[B[0][0], B[1][0], B[2][0]], [B[0][1], B[1][1], B[2][1]], [B[0][2], B[1][2], B[2][2]]]

            for x in range(n):
                b = A[x]
                sistema_linear = list(np.linalg.solve(a, b))
                matriz.append(sistema_linear[:])
                sistema_linear.clear()
            return matriz
        if n == 4:
            a = [[B[0][0], B[1][0], B[2][0], B[3][0]], [B[0][1], B[1][1], B[2][1], B[3][1]],
                 [B[0][2], B[1][2], B[2][2], B[3][2]], [B[0][3], B[1][3], B[2][3], B[3][3]]]

            for x in range(n):
                b = A[x]
                sistema_linear = list(np.linalg.solve(a, b))
                matriz.append(sistema_linear[:])
                sistema_linear.clear()
            return matriz
    else:
        return print("As bases apresentadas não são validas")


# def mudaBase2(A, B):
#     a = [[B[0][0]], B[1][0], [B[0][1], B[1][1]]]
#     b = A[0]
#
#     sistema_linear = np.linalg.solve(a, b)
#     x1 = sistema_linear[0]
#     y1 = sistema_linear[1]
#
#     a = [[B[0][0], B[1][0]], [B[0][1], B[1][1]]]
#     b = A[1]
#
#     sistema_linear = np.linalg.solve(a, b)
#     x2 = sistema_linear[0]
#     y2 = sistema_linear[1]
#
#     matriz = [[x1, x2], [y1, y2]]
#     return matriz
#
#
# def mudaBase3(A, B):
#     matriz = []
#     a = [[B[0][0], B[1][0], B[2][0]], [B[0][1], B[1][1], B[2][1]], [B[0][2], B[1][2], B[2][2]]]
#
#     for x in range(3):
#         b = A[x]
#         sistema_linear = list(np.linalg.solve(a, b))
#         matriz.append(sistema_linear[:])
#         sistema_linear.clear()
#     return matriz
#
#
# def mudaBase4(A, B):
#     matriz = []
#     a = [[B[0][0], B[1][0], B[2][0], B[3][0]], [B[0][1], B[1][1], B[2][1], B[3][1]],
#          [B[0][2], B[1][2], B[2][2], B[3][2]], [B[0][3], B[1][3], B[2][3], B[3][3]]]
#
#     for x in range(4):
#         b = A[x]
#         sistema_linear = list(np.linalg.solve(a, b))
#         matriz.append(sistema_linear[:])
#         sistema_linear.clear()
#     return matriz

