''' Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj. '''

# RESPOSTA 1

def dimensoes(matriz): 
    i = len(matriz) - 1
    linha = len(matriz)
    while i >= 0:
        coluna = len(matriz[i])
        i = i-1
    return print('{}X{}'.format(linha,coluna))

# RESPOSTA 2

def dimensoes(matriz): 
    linha = len(matriz)
    for i in matriz:
        coluna = len(i)
    return f'{linha}x{coluna}'
