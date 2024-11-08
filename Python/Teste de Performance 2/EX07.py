"""Crie um programa que permita ao usuário registrar as notas de uma turma de estudantes.
O usuário deve inserir os nomes dos alunos e suas respectivas notas.
O programa deve continuar solicitando entradas até que o usuário digite "fim".
Após o término, o programa deve exibir os nomes dos alunos junto com suas notas."""

notas = {}

def exibir_notas(notas):
    print("Alunos registrados:")
    for nome, nota in notas.items():
        print(f"Nome: {nome} Nota: {nota}")



def registrar_aluno(notas):
    while True:

        nome = input("Digite o nome do aluno ou fim para terminar: ")

        if nome.lower() == "fim":
            break

        if nome in notas:
            print("Este aluno já possui uma nota, mudando nota...")

        try:
            nota = float(input("Digite a nota do aluno: "))
            notas[nome] = nota

        except ValueError:
            print("Nota inválida.")

    exibir_notas(notas)

registrar_aluno(notas)