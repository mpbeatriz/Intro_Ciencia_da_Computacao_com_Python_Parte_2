'''Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista
e devolve o índice correspondente à posição do elemento encontrado.
Utilize o algoritmo de busca sequencial. Nos casos em que o elemento buscado
não existir na lista, a função deve devolver o booleano False.'''

def busca(lista: list, elemento: int | float | str) -> int | bool:
        if elemento not in lista:
                return False
        else:
            for e in range(len(lista)):
                   if lista[e] == elemento:
                          return e
