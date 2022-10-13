import determinante
import inversa
import mudaBase

print("---------Programa iniciado---------")

print("Digite a operação que deseja fazer: ")
print("1- Determinante e Matriz inversa"
      "\n2 - Matriz mudança de base")
choice = int(input("Choice: "))
matriz = []
dimensao = int(input('Qual a dimensão dessa matriz? '))

if choice == 1:
    if dimensao == 2:
        matriz = [[1, 2], [2, 3]]
        det = determinante.det2(matriz)
        inversa = inversa.inversa2(matriz)
        print(f"O valor da determinante é: {det}")
        print("A sua inversa é: ")
        print(inversa)
    elif dimensao == 3:
        matriz = [[1, 2, 3], [4, 3, 5], [6, 8, 9]]
        det = determinante.det3(matriz)
        inversa = inversa.inversa3(matriz)
        print(f"O valor da determinante é: {det}")
        print("A sua inversa é: ")
        print(inversa)
    elif dimensao == 4:
        matriz = [[1, 2, 3, 4], [9, 2, 5, 1], [3, 0, 4, 2], [5, 4, 3, 2]]
        det = determinante.det4(matriz)
        inversa = inversa.inversa3(matriz)
        print(f"O valor da determinante é: {det}")
        print("A sua inversa é: ")
        print(inversa)
elif choice == 2:
    n = int(input("Digite a dimensão das bases: "))
    if n == 2:
        A = [[1, 3], [2, 4]]
        B = [[1, 2], [4, 3]]
        mudaBase = mudaBase.mudancaBase(A, B, n)
        print(mudaBase)
    if n == 3:
        A = [[1, 3, 4], [5, 4, 3], [6, 4, 2]]
        B = [[2, 4, 8], [7, 8, 2], [9, 1, 1]]
        mudaBase = mudaBase.mudancaBase(A, B, n)
        print(mudaBase)
    if n == 4:
        A = [[4, 5, 6, 1], [4, 3, 2, 0], [3, 7, 9, 1], [0, 8, 3, 1]]
        B = [[3, 2, 1, 3], [1, 8, -2, 1], [4, -9, 0, 3], [4, 2, 7, -3]]
        mudaBase = mudaBase.mudancaBase(A, B, n)
        print(mudaBase)