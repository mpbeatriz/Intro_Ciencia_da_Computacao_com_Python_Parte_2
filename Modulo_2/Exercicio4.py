''' Escreva a função primeiro_lex(lista) que recebe uma lista de strings como parâmetro e devolve
o primeiro string na ordem lexicográfica. Neste exercício, considere letras maiúsculas e minúsculas. '''


def primeiro_lex(lista: list) -> str:
    menor = lista[0]
    for l in lista:
        if l < menor:
            menor = l
    return menor
