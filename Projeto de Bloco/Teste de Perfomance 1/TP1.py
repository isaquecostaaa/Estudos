from datetime import datetime

"""Estrutura de cada tarefa: [id_tarefa, descricao, data, status, prazo, urgencia]"""

tarefas = []
SEPARADOR = "-------------------------"


def adicionar_tarefa(descricao, prazo, urgencia):
    """Adiciona uma nova tarefa à lista de tarefas"""
    data_criacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status = "Pendente"
    id_tarefa = len(tarefas) + 1

    tarefa = [id_tarefa,descricao,data_criacao,status,prazo,urgencia]
    tarefas.append(tarefa)
    print(SEPARADOR)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    """Lista todas as tarefas formatadas"""
    if not tarefas:
        print("Nenhuma tarefa adicionada.")
        return
    print("LISTAGEM DE TAREFAS:")
    for tarefa in tarefas:
        print(SEPARADOR)
        print(f"ID:{tarefa[0]}")
        print(f"Descrição: {tarefa[1]}")
        print(f"Data de criação: {tarefa[2]}")
        print(f"Status: {tarefa[3]}")
        print(f"Prazo: {tarefa[4]}")
        print(f"Urgência: {tarefa[5]}")

def marcar_concluido(id_concluido):
    """Marca uma tarefa escolhida como concluída"""
    for tarefa in tarefas:
        if tarefa[0] == id_concluido:
            tarefa[3] = "Concluído"
            print(SEPARADOR)
            print(f"Tarefa ID {tarefa[0]} definida como concluída!")
            return
    print(SEPARADOR)
    print("Tarefa não encontrada.")

def remover_tarefa(id_remover):
    """Remove uma tarefa escolhida pelo usuário"""
    for tarefa in tarefas:
        if tarefa[0] == id_remover:
            tarefas.remove(tarefa)
            print(SEPARADOR)
            print(f"Tarefa ID {tarefa[0]} removida com sucesso.")
            return
    print(SEPARADOR)
    print("Tarefa não encontrada.")

def menu():
    """Menu de navegação para a gestão de tarefas"""
    while True:
        print(SEPARADOR)
        print("Gestão de tarefas:")
        print("1. para adicionar uma tarefa.")
        print("2. para listar as tarefas.")
        print("3. para Marcar como concluída.")
        print("4. para Remover uma tarefa.")
        print("0. para sair")

        try:
            escolha_usuario = int(input("Digite a opção desejada: "))
            print(SEPARADOR)
        except ValueError:
            print(SEPARADOR)
            print("Digite um número válido!")
            continue

        if escolha_usuario == 1:
            descricao = input("Digite a descrição da tarefa: ")
            prazo = input("Digite o prazo: ")
            urgencia = input("Digite a urgência da tarefa (Baixa/Média/Alta): ")
            adicionar_tarefa(descricao, prazo, urgencia)

        elif escolha_usuario == 2:
            listar_tarefas()

        elif escolha_usuario == 3:
            try:
                id_concluido = int(input("Digite o ID da tarefa que deseja marcar como concluído: "))
                marcar_concluido(id_concluido)
            except ValueError:
                print(SEPARADOR)
                print("ID Inválido, digite novamente.")

        elif escolha_usuario == 4:
            try:
                id_remover = int(input("Digite o ID da tarefa a ser removida: "))
                remover_tarefa(id_remover)
            except ValueError:
                print(SEPARADOR)
                print("ID Inválido, digite novamente.")

        elif escolha_usuario == 0:
            break

        else:
            print(SEPARADOR)
            print("Opção inválida.")

menu()