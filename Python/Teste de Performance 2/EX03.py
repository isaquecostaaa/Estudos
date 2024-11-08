"""Crie uma lista que possua números repetidos e conte a frequência de cada elemento nessa utilizando um dicionário
(Ex: lista = [4, 1, 5, 2, 3, 2, 4, 4] deve retornar dicionario = {1: 1, 2: 2, 3: 1, 4: 3, 5: 1})."""

def contar_frequencia(lista):
    frequencia = {}

    for numero in lista:
        if numero in frequencia:
            frequencia[numero] += 1
        else:
            frequencia[numero] = 1

    return dict(sorted(frequencia.items()))

lista = [4, 1, 5, 2, 3, 2, 4, 4]
print(contar_frequencia(lista))

