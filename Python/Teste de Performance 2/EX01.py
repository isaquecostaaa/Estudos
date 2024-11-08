idades = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16}

def maiores_de_idade(idades):
    return {nome: idade for nome, idade in idades.items() if idade >= 18}

print(maiores_de_idade(idades))
