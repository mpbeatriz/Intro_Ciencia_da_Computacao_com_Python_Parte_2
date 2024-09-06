''' Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro
e devolve o booleano True se a lista estiver ordenada e False se a lista não estiver ordenada. '''

def ordenada(lista: list) -> bool:
    lista2 = sorted(lista)
    if lista2 == lista:
        return True
    else:
        return False
