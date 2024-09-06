''' Escreva uma função menor_nome(nomes) que recebe uma lista de strings com nome de pessoas
como parâmetro e devolve o nome mais curto presente na lista.
A função deve ignorar espaços antes e depois do nome e deve devolver o menor nome presente na lista. 
Este nome deve ser devolvido com a primeira letra maiúscula e seus demais caracteres minúsculos,
independente de como tenha sido apresentado na lista passada para a função.
Quando houver mais de um nome com o menor comprimento dentre os nomes na lista,
a função deve devolver o primeiro nome com o menor comprimento presente na lista.'''

def menor_nome(lista_de_nomes):
    menor = lista_de_nomes[0].strip().capitalize()
    for nome in lista_de_nomes:
        nome = nome.strip().capitalize()
        if len(nome) < len(menor):
            menor = nome
    return menor

