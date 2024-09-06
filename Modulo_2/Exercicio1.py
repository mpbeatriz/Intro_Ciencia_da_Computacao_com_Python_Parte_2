''' Escreva a função maiusculas(frase) que recebe uma frase (uma string) como parâmetro e devolve
uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.'''

def maiusculas(frase: str) -> str:
    maiusculas_da_frase = ''
    for i in frase:
        if 65 <= ord(i) <= 90:
            maiusculas_da_frase += i
        maiusculas_da_frase = maiusculas_da_frase.lstrip().rstrip().strip()
    return maiusculas_da_frase
