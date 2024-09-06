''' Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro parâmetro uma string
contendo uma frase e como segundo parâmetro uma outra string. Este segundo parâmetro deve ser opcional.
Quando o segundo parâmetro for definido como "vogais", a função deve devolver o numero de vogais presentes na frase.
Quando ele for definido como "consoantes", a função deve devolver o número de consoantes presentes na frase.
Se este parâmetro não for passado para a função, deve-se assumir o valor "vogais" para o parâmetro.'''

def conta_letras(frase: str, condicao:str = "vogais") -> int:
    contador_vogal = 0
    contador_conso = 0
    vogais = 'aeiouAEIOU'
    frase = frase.split()
    f = ''.join(frase)
    if condicao == "vogais":
        for i in f:
            if i in vogais:
                contador_vogal += 1
        return contador_vogal
    if condicao == "consoantes":
        for i in f:
            if i not in vogais:
                contador_conso += 1
        return contador_conso
