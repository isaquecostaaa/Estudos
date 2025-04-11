from src.database.banco import conectar
from src.crud.autores_db import *

def consultar_autores():
    try:
        autores = consultar_autores_db()

        print("\nAUTORES:")
        print("=" * 40)
        for autor in autores:
            id_autor, nome, pais = autor
            print(f"ID: {id_autor}")
            print(f"Nome: {nome}")
            print(f"País de nascimento: {pais}")
            print("=" * 40)
    except Exception as e:
        print(f"Erro ao consultar autores: {e}")

def adicionar_autor(nome=None, pais_origem=None):
    try:   
        if nome is None and pais_origem is None:
            nome = input("Digite o nome do autor: ")
            pais_origem = input("Digite o país de origem do autor: ")

        autor = buscar_autor_por_nome(nome, pais_origem)

        if autor:
            id_autor = autor[0]
            print(f"O autor '{nome}' já está cadastrado.")
        else:
            id_autor = inserir_autor(nome, pais_origem)
            print(f"Autor '{nome}' adicionado com sucesso.")
            return id_autor
    
    except Exception as e:
        print(f"Erro ao adicionar autor: {e}")

def atualizar_autor():
    try:
        from menus.menu_autores import menu_update_autores
        conn = conectar()
        c = conn.cursor()

        id_autor = int(input("Digite o ID do autor que deseja atualizar: "))
        autor = buscar_autor(id_autor)

        if not autor:
            print("Autor não encontrado")
            return
        
        while True:
            opcao = menu_update_autores()
            match opcao:
                case "0":
                    break

                case "1":
                    novo_nome = input("Digite o novo nome: ")
                    if novo_nome.strip():
                        atualizar_autor_db(id_autor, "nome", novo_nome)
                        print("Nome atualizado com sucesso!")
                    else:
                        print("Nome não pode ser vazio.")

                case "2":
                    novo_pais = input("Digite o novo país de origem: ")
                    if novo_pais.strip():
                        atualizar_autor_db(id_autor, "pais_origem", novo_pais)
                        print("País de origem atualizado com sucesso!")
                    else:
                        print("País de origem não pode ser vazio.")
                case _:
                    print("Opcão inválida, tente novamente")

    except Exception as e:
        print(f"Erro: houve um erro na atualização dos dados: {e}")

def excluir_autor():
    try:
        id_autor = int(input("Digite o ID do autor: "))
        autor = buscar_autor(id_autor)

        if not autor:
            print("Nenhum autor encontrado com esse ID.")
            return

        relacao = verificar_relacao_livro_autor(id_autor)
        if relacao:
            print(f"O autor '{autor[0]}' está vinculado a um ou mais livros e não pode ser excluído.")
            print("Para deletá-lo, delete os livros primeiro")
            return

        excluir_autor_db(id_autor)
        print("Autor deletado com sucesso.")

    except Exception as e:
        print(f"Erro ao excluir autor: {e}")

