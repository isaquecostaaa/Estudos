"""Defina uma função chamada calcular_total que receba dois parâmetros: preço e quantidade, onde a quantidade tem o
valor padrão de 1. A função deve calcular e retornar o total, multiplicando o preço pela quantidade."""

def calcular_total(preco, quantidade = 1):
    return preco * quantidade

print("O total é:",calcular_total(15,4))
print("O total é:",calcular_total(15))