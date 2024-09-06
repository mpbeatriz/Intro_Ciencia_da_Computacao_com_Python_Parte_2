'''Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que represente
sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.'''

def dimensoes(matriz):
    i = len(matriz) - 1
    linha = len(matriz)
    while i >= 0:
        coluna = len(matriz[i])
        i = i-1
    return (linha,'x',coluna)

def soma_matrizes(A, B): 
    if dimensoes(A) != dimensoes(B):
        return False
    else:
        C = []
        linha = 0
        for e in range(len(A)):
            linha = [0] * len(A[0])
            C.append(linha)
            for j in range(len(A[0])):
                C[e][j] = A[e][j] + B[e][j] 
        return C
