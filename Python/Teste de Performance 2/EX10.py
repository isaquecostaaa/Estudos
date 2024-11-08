"""Crie uma lista de dicionários (de 4 ou mais elementos), em que cada elemento possui o nome e a nota dos
alunos e ordene a lista de maneira decrescente por nota. OBS: Faça o exercício utilizando apenas estruturas básicas,
sem chamar funções de sort ou algo do tipo."""

lista = [{"nome": "Mateus", "nota": 7.0},
         {"nome": "Lucas", "nota": 9.0},
         {"nome": "Isaque", "nota": 10.0},
         {"nome":"João", "nota": 6.0}]

def organizar_por_nota(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i]["nota"] < lista[j]["nota"]:
                lista[i], lista[j] = lista[j], lista[i]

    exibir_lista(lista)

def exibir_lista(lista):
    for aluno in lista:
        print(f"Nome: {aluno['nome']}, Nota: {aluno['nota']}")

organizar_por_nota(lista)