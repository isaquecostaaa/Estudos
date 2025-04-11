from src.utils.validar_data import validar_data
from src.crud.autores import adicionar_autor
from src.crud.livros_db import *
from src.crud.emprestimos_db import verificar_emprestimos_ativos

def consultar_livros():
    try:

        livros = consultar_livros_db()
        if not livros:
            print("\nNenhum livro encontrado.")
            return

        print("\nLISTA DE LIVROS")
        print("=" * 40)
        for livro in livros:
            id_livro, titulo, isbn, genero, data_publicacao, qtd_paginas, disponibilidade = livro
            print(f"ID: {id_livro}")
            print(f"Título: {titulo}")
            print(f"ISBN: {isbn}")
            print(f"Gênero: {genero}")
            print(f"Data de Publicação: {data_publicacao}")
            print(f"Páginas: {qtd_paginas}")
            print(f"Disponibilidade: {disponibilidade} unidades")
            print("=" * 40)

    except Exception as e:
        print(f"Erro ao consultar livros: {e}")

def adicionar_livro():
    try:
        titulo = input("Digite o título do livro: ")
        isbn = input("Digite o ISBN do livro: ")
        genero = input("Digite o gênero do livro: ")
        
        data_input = input("Digite a data de publicação do livro (ano-mês-dia): ")
        if not validar_data(data_input):
            return
        data_publicacao = data_input

        try:
            qtd_paginas = int(input("Digite a quantidade de páginas: "))
            disponibilidade = int(input("Digite a quantidade de livros disponíveis: "))
        except ValueError:
            print("Quantidade de páginas e disponibilidade devem ser números inteiros.")
            return

        nome_autor = input("Digite o nome do autor: ")
        pais_origem = input("Digite o país de origem do autor: ")

        id_autor = adicionar_autor(nome_autor, pais_origem)

        livro = verificar_livro_existente(isbn=isbn)

        if livro:
            id_livro = livro[0]
        else:
            id_livro = inserir_livro(titulo, isbn, genero, data_publicacao, qtd_paginas, disponibilidade)

        inserir_livros_autores(id_livro, id_autor)
        print("Livro adicionado com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar livro: {e}")

def atualizar_livro():
    try:
        from menus.menu_livros import menu_update_livros

        id_livro = int(input("\nDigite o ID do livro que deseja atualizar: ")) 
        livro = buscar_livro(id_livro)
        
        if not livro:
            print("Livro não encontrado.")
            return
        
        while True:
            opcao = menu_update_livros()
            match opcao:
                case "0":
                    break

                case "1":
                    novo_titulo = input("Digite o novo título: ")
                    if novo_titulo.strip():
                        atualizar_livro_db(id_livro, "titulo", novo_titulo)
                        print("Título atualizado com sucesso!")
                    else:
                        print("Título não pode ser vazio.")

                case "2":
                    novo_isbn = input("Digite o novo ISBN: ")
                    if novo_isbn.strip():
                        atualizar_livro_db(id_livro, "ISBN", novo_isbn)
                        print("ISBN atualizado com sucesso!")
                    else:
                        print("ISBN não pode ser vazio.")

                case "3":
                    novo_genero = input("Digite o novo gênero: ")
                    if novo_genero.strip():
                        atualizar_livro_db(id_livro, "genero", novo_genero)
                        print("Gênero atualizado com sucesso!")
                    else:
                        print("Gênero não pode ser vazio.")

                case "4":
                    nova_data = validar_data(input("Digite a nova data de publicação (AAAA-MM-DD): "))
                    if not nova_data == None:
                        atualizar_livro_db(id_livro, "data_publicacao", nova_data)
                        print("Data de publicação atualizada com sucesso!")
                    else:
                        print("Digite uma data válida.")

                case "5":
                    nova_qtd = int(input("Digite a nova quantidade de páginas: "))
                    if nova_qtd > 0:
                        atualizar_livro_db(id_livro, "qtd_paginas", nova_qtd)
                        print("Quantidade de páginas atualizada com sucesso!")
                    else:
                        print("A quantidade deve ser maior que zero.")

                case "6":
                        nova_disp = int(input("Digite a nova quantidade disponível: "))
                        if nova_disp >= 0:
                            emprestimos_ativos = verificar_emprestimos_ativos(id_livro)

                            if nova_disp >= emprestimos_ativos:
                                atualizar_livro_db(id_livro, "disponibilidade", nova_disp)
                                print("Quantidade disponível atualizada com sucesso!")
                            else:
                                print(f"Erro: Existem {emprestimos_ativos} empréstimos ativos para este livro.")
                                print(f"A quantidade disponível não pode ser menor que {emprestimos_ativos}.")
                        else:
                            print("A quantidade não pode ser negativa.")
                case _:
                    print("Opção inválida. Tente novamente.")
    except Exception as e:
        print(f"Erro ao atualizar livro: {e}")

def excluir_livro():
    try:
        id_livro = int(input("Digite o ID do livro que deseja excluir: "))

        emprestimos_ativos = verificar_emprestimos_ativos(id_livro=id_livro)
        if emprestimos_ativos > 0:
            print("Não é possível excluir, existem empréstimos ativos")
            return

        livro = buscar_livro(id_livro)

        if not livro:
            print("Nenhum livro encontrado com esse ID.")
            return

        excluir_livro_db(id_livro)
        print("Livro deletado com sucesso.")

    except Exception as e:
        print(f"Erro ao excluir livro: {e}")

